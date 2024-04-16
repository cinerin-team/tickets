import re

import requests
from lxml import etree

from config import TEAM


def download_page(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def process_downloaded_page(string):
    string = string.replace("\n", "")
    m = re.search('(<table .*?>.+?</table>)', string)
    found = ' '.join(m.group(1).split())
    found = found.replace("<thead>", "").replace("</thead>", "").replace("<tbody>", "").replace("</tbody>", "")

    return found


def parse_table(string):
    dict_list = []
    dict_list.clear()
    table = etree.HTML(process_downloaded_page(string)).find("body/table")
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
    content1 = download_page(
        "https://dashboards.sero.wh.rnd.internal.ericsson.com/epg_st_passrates/epg_st_passrates_weekly_master_not_run_team.html")

    print("outdated tests: ")
    print(collect_teams_tests(TEAM, parse_table(content1)))

    content2 = download_page(
        "https://dashboards.sero.wh.rnd.internal.ericsson.com/epg_st_passrates/epg_st_passrates_weekly_master_to_do_team.html")

    print("to do tests: ")
    print(collect_teams_tests(TEAM, parse_table(content2)))

