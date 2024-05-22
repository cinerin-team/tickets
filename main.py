import pprint

from PasswdMgmt import PasswdMgmt
from config import TEAM, TODO_DASHBOARD, OUT_OF_DATE_DASHBOARD, TREX_QUERY_FOR_ALL_CINERIN_TCS_MAIN, \
    TREX_QUERY_FOR_ALL_CINERIN_TCS_RELEASE, RELEASE_NEEDED, MAIN, RELEASE
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
    trex_main = download_page_w_cred_trex(TREX_QUERY_FOR_ALL_CINERIN_TCS_MAIN, credentials)
    parsed_array_main = parse_table_for_trex(trex_main)
    collected_TCs_main = collect_all_our_tickets_with_their_last_build_and_run(parsed_array_main)
    todo_tickets_main = collect_the_tcs_which_will_td_in_next_sprint(collected_TCs_main)
    array_for_csv = build_array_for_csv_from_tc_list(todo_tickets_main, MAIN)

    if RELEASE_NEEDED:
        trex_release = download_page_w_cred_trex(TREX_QUERY_FOR_ALL_CINERIN_TCS_RELEASE, credentials)
        parsed_array_release = parse_table_for_trex(trex_main)
        collected_TCs_release = collect_all_our_tickets_with_their_last_build_and_run(parsed_array_release)
        todo_tickets_release = collect_the_tcs_which_will_td_in_next_sprint(collected_TCs_release)
        array_for_csv += build_array_for_csv_from_tc_list(todo_tickets_release, RELEASE)

    write_out_array_to_csv(array_for_csv)
