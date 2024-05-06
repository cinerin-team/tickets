import pprint
import re
import time

import requests
from lxml import etree

from PasswdMgmt import PasswdMgmt
from config import TEAM, TODO_DASHBOARD, OUT_OF_DATE_DASHBOARD, TREX_QUERY_FOR_ALL_CINERIN_TCS, TREX_LOGIN


def download_page(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def download_page_w_cred(url, cred):
    from selenium import webdriver
    from selenium.webdriver.edge.options import Options
    from selenium.webdriver.common.by import By

    # Options objektum inicializálása
    edge_options = Options()

    # Edge WebDriver inicializálása Options objektummal
    driver = webdriver.Edge(options=edge_options)

    # Oldal betöltése
    driver.get(TREX_LOGIN)

    # Felhasználónév mező kiválasztása az id attribútum alapján
    username_field = driver.find_element(By.ID, 'edit-name')

    # Jelszó mező kiválasztása az id attribútum alapján
    password_field = driver.find_element(By.ID, 'edit-pass')

    # Bejelentkezés gomb kiválasztása az id attribútum alapján
    login_button = driver.find_element(By.ID, 'edit-submit')

    # Felhasználónév és jelszó beírása
    username_field.send_keys(cred.get_username())
    password_field.send_keys(cred.get_password())

    # Bejelentkezés gombra kattintás
    login_button.click()
    time.sleep(5)
    driver.get(url)
    time.sleep(20)

    # Oldal tartalmának lekérése
    page_source = driver.page_source

    # Oldal tartalmának kiíratása
    return page_source

    # Várakozás, hogy a bejelentkezés befejeződjön
    # (Itt érdemes hozzáadni egy várakozási időt, hogy biztosítsd a betöltődést)

    # import requests
    #
    # # A bejelentkezéshez szükséges adatok
    # login_url = TREX_LOGIN  # Bejelentkezési URL
    # username = cred.get_username()
    # password = cred.get_password()
    #
    # # Bejelentkezési adatok
    # login_data = {
    #     'name': username,
    #     'pass': password
    # }
    #
    # # Session létrehozása
    # session = requests.Session()
    #
    # # Bejelentkezési kérés küldése
    # login_response = session.post(login_url, data=login_data)
    #
    # # Ellenőrizzük, hogy sikeres volt-e a bejelentkezés
    # if login_response.status_code == 200:
    #     print("Sikeres bejelentkezés!")
    #
    #     # A tartalom letöltése a bejelentkezett felhasználó számára elérhető oldalról
    #     target_url = TREX_QUERY_FOR_ALL_CINERIN_TCS  # A letöltendő oldal URL-je
    #     content_response = session.get(target_url)
    #
    #     # A letöltött tartalom tárolása egy változóban
    #     web_content = content_response.text
    #
    #     # Az oldal tartalmának kiírása
    #     print(web_content)
    # else:
    #     print("Sikertelen bejelentkezés!")

    # import requests
    # values = {'edit-name': cred.get_username(),
    #           'edit-pass': cred.get_password()}
    #
    # r = requests.post(TREX_LOGIN, data=values)
    # return r.content


def process_downloaded_page_from_dashboard(string):
    string = string.replace("\n", "")
    m = re.search('(<table .*?>.+?</table>)', string)
    found = ' '.join(m.group(1).split())
    found = found.replace("<thead>", "").replace("</thead>", "").replace("<tbody>", "").replace("</tbody>", "")

    return found


def process_downloaded_page_from_trex(string):
    string = string.replace("\n", "")
    m = re.search('(<table class="table table-striped table-bordered table-hover sticky-enabled treqsTable sticky-table tableheader-processed" id="result-table">.+?</table>)', string)
    found = ' '.join(m.group(1).split())
    found = found.replace("<thead>", "").replace("</thead>", "").replace("<tbody>", "").replace("</tbody>", "")
    found = re.sub('<a .*?>', '', found)
    found = re.sub('</a>', '', found)

    return found


def parse_table_for_trex(string):
    dict_list = []
    dict_list.clear()
    table = etree.HTML(process_downloaded_page_from_trex(string)).find("body/table")
    rows = iter(table)
    headers = [col.text for col in next(rows)]
    for row in rows:
        values = [col.text for col in row]
        one_line = dict(zip(headers, values))
        clean_line = {k: v.strip() for k, v in one_line.items()}
        dict_list.append(clean_line)
    return dict_list


def parse_table_for_dash(string):
    dict_list = []
    dict_list.clear()
    table = etree.HTML(process_downloaded_page_from_dashboard(string)).find("body/table")
    rows = iter(table)
    headers = [col.text for col in next(rows)]
    for row in rows:
        values = [col.text for col in row]
        one_line = dict(zip(headers, values))
        clean_line = {k: v.strip() for k, v in one_line.items()}
        dict_list.append(clean_line)
    return dict_list


def collect_teams_tests(team, parsed_table):
    result = []
    for item in parsed_table:
        if item['Responsible Team'] == team:
            result.append(item)
    return result


if __name__ == '__main__':
    ood_dash = download_page(OUT_OF_DATE_DASHBOARD)

    print("outdated tests from dashboard: ")
    pprint.pprint(collect_teams_tests(TEAM, parse_table_for_dash(ood_dash)))

    todo_dash = download_page(TODO_DASHBOARD)

    print("to do tests from dashboard: ")
    pprint.pprint(collect_teams_tests(TEAM, parse_table_for_dash(todo_dash)))

    credentials = PasswdMgmt()
    trex = download_page_w_cred(TREX_QUERY_FOR_ALL_CINERIN_TCS, credentials)
    print("all tests from treq-s: ")
    pprint.pprint(parse_table_for_trex(trex))
