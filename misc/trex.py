import re
import time

from lxml import etree

from config import TREX_LOGIN


def download_page_w_cred_trex(url, cred):
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


def process_downloaded_page_from_trex(string):
    string = string.replace("\n", "")
    m = re.search(
        '(<table class="table table-striped table-bordered table-hover sticky-enabled treqsTable sticky-table tableheader-processed" id="result-table">.+?</table>)',
        string)
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
