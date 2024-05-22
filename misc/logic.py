from datetime import datetime, timedelta

from config import TCS, SPRINT_START_DATE, SPRINT_WEEKS, SCOPE_MAPPING, SPRINT_ID, MAIN, TEAM


def collect_all_our_tickets_with_their_last_build_and_run(trex_arr):
    result = []
    for tc in TCS.keys():
        for trex in trex_arr:
            if trex['Testcase Id'] == tc:
                result.append({"Testcase Id": tc, "Build": trex['Build Time'].split(" ")[0]})
                continue

    return result


def collect_the_tcs_which_will_td_in_next_sprint(tc_w_last_run):
    result = []
    end_of_sprint = datetime(int(SPRINT_START_DATE.split("-")[0]), int(SPRINT_START_DATE.split("-")[1]),
                             int(SPRINT_START_DATE.split("-")[2])) + timedelta(days=SPRINT_WEEKS * 7)
    for tc in tc_w_last_run:
        if tc["Testcase Id"] not in TCS.keys():
            continue
        for i in range(SPRINT_WEEKS):
            if datetime(int(tc["Build"].split("-")[0]), int(tc["Build"].split("-")[1]),
                        int(tc["Build"].split("-")[2])) + timedelta(
                days=SCOPE_MAPPING[TCS[tc["Testcase Id"]]["scope"]] + i * SCOPE_MAPPING[
                    TCS[tc["Testcase Id"]]["scope"]]) < end_of_sprint:
                result.append(tc["Testcase Id"])

    return result


def build_array_for_csv_from_tc_list(arr, branch):
    result = []
    for item in arr:
        result.append([item, str(SPRINT_ID), "Task", "High", TCS[item]["owner"], "erkmiap", branch, TEAM, TCS[item]["Label1"], TCS[item]["Label2"], TCS[item]["Label3"], TCS[item]["Label4"], TCS[item]["Original Estimate"], TCS[item]["Story Points"]])

    return result


def write_out_array_to_csv(arr):
    with open('sprint.csv', 'w') as file:
        file.write(
            "Summary;Sprint;Issue Type;Priority;Assignee;Reporter;Fix Version/s;Team;Labels;Labels;Labels;Labels;Original Estimate;Story Points\n" +
            "EP handling;" + str(SPRINT_ID) + ";Task;High;ecsiger;erkmiap;;Cinerin;ST;;;;;\n" +
            "EP handling;" + str(SPRINT_ID) + ";Task;High;etotist;erkmiap;;Cinerin;ST;;;;;\n" +
            "CI Monitor;" + str(SPRINT_ID) + ";Task;High;erkmiap;erkmiap;;Cinerin;CI;;;;162000;5\n" +
            "CI Monitor;" + str(SPRINT_ID) + ";Task;High;ETHNYZ;erkmiap;;Cinerin;CI;;;;162000;5\n" +
            "EPG stportal node maintenance;" + str(SPRINT_ID) + ";Task;High;erkmiap;erkmiap;;Cinerin;CI;;;;108000;3.75\n" +
            "EPG stportal node maintenance;" + str(SPRINT_ID) + ";Task;High;ETHNYZ;erkmiap;;Cinerin;CI;;;;108000;3.75\n" +
            "Main Track Releasability reporting, monitoring W3;" + str(SPRINT_ID) + ";Task;High;etotist;erkmiap;"+MAIN+";Cinerin;Other;;;;14400;0.5\n" +
            "Main Track Releasability reporting, monitoring W2;" + str(SPRINT_ID) + ";Task;High;ethnyz;erkmiap;"+MAIN+";Cinerin;Other;;;;14400;0.5\n" +
            "Main Track Releasability reporting, monitoring W1;" + str(SPRINT_ID) + ";Task;High;ecsiger;erkmiap;"+MAIN+";Cinerin;Other;;;;14400;0.5\n")
        for row in arr:
            file.write(';'.join(map(str, row)) + '\n')
