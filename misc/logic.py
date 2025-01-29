from datetime import datetime, timedelta

from config import TCS, SPRINT_START_DATE, SPRINT_WEEKS, SCOPE_MAPPING, SPRINT_ID, MAIN, TEAM, SM, SPRINT_FILE_NAME


def collect_all_our_tickets_with_their_last_build_and_run_from_the_TREQ(trex_arr):
    result = []
    for tc in TCS.keys():
        for trex in trex_arr:
            if trex['Testcase Id'] == tc:
                result.append({"Testcase Id": tc, "Build": trex['Build Time'].split(" ")[0]})
                continue

    return result


def collect_the_tcs_which_will_todo_in_next_sprint(tc_w_last_run):
    result = []
    end_of_sprint = datetime(int(SPRINT_START_DATE.split("-")[0]), int(SPRINT_START_DATE.split("-")[1]),
                             int(SPRINT_START_DATE.split("-")[2])) + timedelta(days=SPRINT_WEEKS * 7)
    for tc in tc_w_last_run:
        if tc["Testcase Id"] not in TCS.keys():
            continue
        for i in range(SPRINT_WEEKS):
            final_date = datetime(int(tc["Build"].split("-")[0]), int(tc["Build"].split("-")[1]),
                                  int(tc["Build"].split("-")[2])) + timedelta(
                days=SCOPE_MAPPING[TCS[tc["Testcase Id"]]["scope"]] + i * SCOPE_MAPPING[
                    TCS[tc["Testcase Id"]]["scope"]])
            if final_date < end_of_sprint:
                result.append((tc["Testcase Id"], " scope: " + str(SCOPE_MAPPING[
                                                                             TCS[tc["Testcase Id"]][
                                                                                 "scope"]]) + " days"))

    return result


def build_array_for_csv_from_tc_list(arr, branch):
    result = []
    for item in arr:
        result.append(
            [item[0] + item[1], str(SPRINT_ID), "Task", "High", TCS[item[0]]["owner"], SM, branch, TEAM,
             TCS[item[0]]["Label1"], TCS[item[0]]["Label2"], TCS[item[0]]["Label3"], TCS[item[0]]["Label4"],
             TCS[item[0]]["Original Estimate"], TCS[item[0]]["Story Points"]])

    return result


def write_out_array_to_csv(arr):
    clear_and_start_file()
    write_additional_tickets()
    with open(SPRINT_FILE_NAME, 'a+') as file:
        for row in arr:
            file.write(';'.join(map(str, row)) + '\n')


def clear_and_start_file():
    with open(SPRINT_FILE_NAME, 'w') as file:
        file.write(
            "Summary;Sprint;Issue Type;Priority;Assignee;Reporter;Fix Version/s;Team;Labels;Labels;Labels;Labels;Original Estimate;Story Points\n")


def write_additional_tickets():
    with open(SPRINT_FILE_NAME, 'a+') as file:
        file.write(
            "EP handling;" + str(SPRINT_ID) + ";Task;High;ecsiger;" + SM + ";;Cinerin;ST;;;;;\n" +
            "EP handling;" + str(SPRINT_ID) + ";Task;High;etotist;" + SM + ";;Cinerin;ST;;;;;\n" +
            "CI Monitor - EVEN WEEK;" + str(SPRINT_ID) + ";Task;High;ERKMIAP;" + SM + ";;Cinerin;CI;;;;162000;5\n" +
            "CI Monitor - ODD WEEK;" + str(SPRINT_ID) + ";Task;High;ETHNYZ;" + SM + ";;Cinerin;CI;;;;162000;5\n" +
            "EPG stportal node maintenance - ODD WEEK;" + str(
                SPRINT_ID) + ";Task;High;ERKMIAP;" + SM + ";;Cinerin;CI;;;;108000;3.75\n" +
            "EPG stportal node maintenance - EVEN WEEK;" + str(
                SPRINT_ID) + ";Task;High;ETHNYZ;" + SM + ";;Cinerin;CI;;;;108000;3.75\n" +
            "Main Track Releasability reporting, monitoring W3;" + str(
                SPRINT_ID) + ";Task;High;etotist;" + SM + ";" + MAIN + ";Cinerin;Other;;;;14400;0.5\n" +
            "Main Track Releasability reporting, monitoring W2;" + str(
                SPRINT_ID) + ";Task;High;ethnyz;" + SM + ";" + MAIN + ";Cinerin;Other;;;;14400;0.5\n" +
            "Main Track Releasability reporting, monitoring W1;" + str(
                SPRINT_ID) + ";Task;High;ecsiger;" + SM + ";" + MAIN + ";Cinerin;Other;;;;14400;0.5\n")
