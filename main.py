import pprint

from PasswdMgmt import PasswdMgmt
from config import TEAM, TODO_DASHBOARD, OUT_OF_DATE_DASHBOARD, TREX_QUERY_FOR_ALL_CINERIN_TCS
from misc.dashboard import download_page, collect_teams_tests, parse_table_for_dash
from misc.eventviewer import download_page_w_cred_event, parse_table_for_event
from misc.trex import download_page_w_cred_trex, parse_table_for_trex

if __name__ == '__main__':
    ood_dash = download_page(OUT_OF_DATE_DASHBOARD)

    print("outdated tests from dashboard: ")
    pprint.pprint(collect_teams_tests(TEAM, parse_table_for_dash(ood_dash)))

    todo_dash = download_page(TODO_DASHBOARD)

    print("to do tests from dashboard: ")
    pprint.pprint(collect_teams_tests(TEAM, parse_table_for_dash(todo_dash)))

    credentials = PasswdMgmt()
    trex = download_page_w_cred_trex(TREX_QUERY_FOR_ALL_CINERIN_TCS, credentials)
    print("all tests to cinerin from treq-s: ")
    pprint.pprint(parse_table_for_trex(trex))

    event = download_page_w_cred_event("TC37540.1.6.16", credentials)
    print("TC37540.1.6.16 tests from event viewer: ")
    pprint.pprint(parse_table_for_event(event))
