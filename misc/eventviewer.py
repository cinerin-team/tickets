import re
import time

from lxml import etree

from config import EVENT_LOGIN, EVENT_QUERY


def download_page_w_cred_event(tcid, cred):
    from selenium import webdriver
    from selenium.webdriver.edge.options import Options
    from selenium.webdriver.common.by import By

    # Options objektum inicializálása
    edge_options = Options()

    # Edge WebDriver inicializálása Options objektummal
    driver = webdriver.Edge(options=edge_options)

    # Oldal betöltése
    driver.get(EVENT_LOGIN)

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

    driver.get(EVENT_QUERY)
    time.sleep(5)
    tc_field = driver.find_element(By.ID, 'eventsearch_label')
    tc_field.send_keys(tcid)
    driver.find_element(By.XPATH, "//input[@type='submit']").click()

    time.sleep(10)

    # Oldal tartalmának lekérése
    page_source = driver.page_source

    # Oldal tartalmának kiíratása
    return page_source


def process_downloaded_page_from_event(string):
    string = string.replace("\n", "")
    string = re.sub('<a class="cimsui-tooltip cimsui-tooltip-processed".*?</span></a>', '', string)
    string = re.sub('<span class="cimsui-popover cimsui-popover-processed".*?</div></span>', '', string)
    string = re.sub('<span class="cims-icons-15 cims-icons-inconc" title="Inconclusive">&nbsp;</span>', 'Inconclusive',
                    string)
    string = re.sub('<span class="cims-icons-15 cims-icons-fail" title="Failed">&nbsp;</span>', 'Failed', string)
    string = re.sub('<span class="cims-icons-15 cims-icons-ok" title="Passed">&nbsp;</span>', 'Passed', string)
    string = re.sub('<span class="cims-icons-15 cims-icons-error" title="Error">&nbsp;</span>', 'Error', string)
    string = re.sub('<span class="cims-icons-15 cims-icons-interrupt" title="Interrupted">&nbsp;</span>', 'Interrupted',
                    string)
    string = re.sub('<span class="cims-icons-15 cims-icons-fail-inverted" title="Failed with TR">&nbsp;</span>',
                    'Failed with TR', string)
    string = re.sub('<span class="cims-icons-15 cims-icons-timeout" title="Timed out">&nbsp;</span>', 'Timed out',
                    string)
    m = re.search(
        '(<table id="cimsui-EventHistoryViewer-event-history-viewer-" class="cimsui-datatable table table-striped dataTable no-footer" role="grid" aria-describedby="cimsui-EventHistoryViewer-event-history-viewer-_info" style="opacity: 1;">.+?</table>)',
        string)
    found = ' '.join(m.group(1).split())
    found = found.replace("<thead>", "").replace("</thead>", "").replace("<tbody>", "").replace("</tbody>", "")
    found = re.sub('<a .*?>', '', found)
    found = re.sub('</a>', '', found)
    found = re.sub('<tr id="" class="dataTables_row_group">.*?</tr>', '', found)

    return found


def parse_table_for_event(string):
    dict_list = []
    dict_list.clear()
    table = etree.HTML(process_downloaded_page_from_event(string)).find("body/table")
    rows = iter(table)
    headers = [col.text for col in next(rows)]
    for row in rows:
        values = [col.text for col in row]
        one_line = dict(zip(headers, values))
        clean_line = {k: v for k, v in one_line.items()}
        dict_list.append(clean_line)
    return dict_list
