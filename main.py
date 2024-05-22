import pprint

from PasswdMgmt import PasswdMgmt
from config import TEAM, TODO_DASHBOARD, OUT_OF_DATE_DASHBOARD, TREX_QUERY_FOR_ALL_CINERIN_TCS
from misc.dashboard import download_page, collect_teams_tests, parse_table_for_dash
from misc.eventviewer import download_page_w_cred_event, parse_table_for_event
from misc.logic import collect_all_our_tickets_with_their_last_build_and_run, \
    collect_the_tcs_which_will_td_in_next_sprint, build_array_for_csv_from_tc_list, write_out_array_to_csv
from misc.trex import download_page_w_cred_trex, parse_table_for_trex

if __name__ == '__main__':
    # ood_dash = download_page(OUT_OF_DATE_DASHBOARD)
    # print("outdated tests from dashboard: ")
    # pprint.pprint(collect_teams_tests(TEAM, parse_table_for_dash(ood_dash)))
    #
    # todo_dash = download_page(TODO_DASHBOARD)
    # print("to do tests from dashboard: ")
    # pprint.pprint(collect_teams_tests(TEAM, parse_table_for_dash(todo_dash)))

    credentials = PasswdMgmt()
    trex = download_page_w_cred_trex(TREX_QUERY_FOR_ALL_CINERIN_TCS, credentials)
    # print("all tests to cinerin from treq-s: ")
    # pprint.pprint(parse_table_for_trex(trex))
    write_out_array_to_csv(build_array_for_csv_from_tc_list(collect_the_tcs_which_will_td_in_next_sprint(collect_all_our_tickets_with_their_last_build_and_run(parse_table_for_trex(trex)))))

    # event = download_page_w_cred_event("TC1122.1.1.10.1", credentials)
    # print("TC1122.1.1.10.1 tests from event viewer: ")
    # pprint.pprint(parse_table_for_event(event))
