# these variables should be updated!!!
SPRINT_ID = 21678
TREX_QUERY_FOR_ALL_CINERIN_TCS_RELEASE = 'https://epgweb.sero.wh.rnd.internal.ericsson.com/treqsviewer/viewer?{%22product_part%22:%22build%22,%22product%22:%22EPG_3.38_28%22,%22build%22:%22latest%22,%22type%22:%22testcase%22,%22selected%22:[%22testcase_id%22,%22build_time%22,%22job_time%22],%22filters%22:{%22parent_revision%22:[%22true%22]}}'
SPRINT_START_DATE = "2024-07-29"
SPRINT_WEEKS = 3
MAIN = "EPG3.40"
RELEASE = "EPG3.39"
RELEASE_NEEDED = True

# these variables should not be updated
TREX_QUERY_FOR_ALL_CINERIN_TCS_MAIN = 'https://epgweb.sero.wh.rnd.internal.ericsson.com/treqsviewer/viewer?{%22product_part%22:%22build%22,%22product%22:%22EPG_MASTER_28%22,%22build%22:%22latest%22,%22type%22:%22testcase%22,%22selected%22:[%22testcase_id%22,%22build_time%22,%22job_time%22],%22filters%22:{%22parent_revision%22:[%22true%22],%22Responsible_Team%22:%22Cinerin%22}}'
TEAM = "Cinerin"
TODO_DASHBOARD = "https://dashboards.sero.wh.rnd.internal.ericsson.com/epg_st_passrates/epg_st_passrates_weekly_master_to_do_team.html"
OUT_OF_DATE_DASHBOARD = "https://dashboards.sero.wh.rnd.internal.ericsson.com/epg_st_passrates/epg_st_passrates_weekly_master_not_run_team.html"
TREX_LOGIN = 'https://epgweb.sero.wh.rnd.internal.ericsson.com/treqsviewer/viewer?{%22product_part%22:%22build%22,%22product%22:%22EPG_MASTER_28%22,%22build%22:%22latest%22,%22type%22:%22testcase%22,%22selected%22:[%22testcase_id%22,%22build_time%22,%22job_time%22],%22filters%22:{%22parent_revision%22:[%22true%22]}}'
EVENT_LOGIN = 'https://epgweb.sero.wh.rnd.internal.ericsson.com/eventhistory/name'
EVENT_QUERY = 'https://epgweb.sero.wh.rnd.internal.ericsson.com/eventhistory/name?failure_reason=&product=&parent=&include_rerun=on&hostname=&stream=&label=&verdict_skipped=on&verdict_failed=on&verdict_FAIL=on&verdict_ERROR=on&verdict_INTERRUPT=on&verdict_TIMEOUT=on&verdict_UNSTABLE=on&verdict_passed=on&verdict_PASS=on&verdict_WARNING=on&verdict_INCONC=on'
TCS = {
    "TC37512.4.6.1.53": {"scope": "2Extended", "owner": "ETOTIST", "Label1": "REGRESSION", "Label2": "CAPACITY", "Label3": "ST_2EXTENDED", "Label4": "ST_BI-WEEKLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37540.1.6.11": {"scope": "2Extended", "owner": "ETOTIST", "Label1": "REGRESSION", "Label2": "STABILITY", "Label3": "ST_2EXTENDED", "Label4": "ST_BI-WEEKLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37540.40.6.1": {"scope": "2Extended", "owner": "ETOTIST", "Label1": "REGRESSION", "Label2": "STABILITY", "Label3": "ST_2EXTENDED", "Label4": "ST_BI-WEEKLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37512.4.6.1.53.1": {"scope": "Dynamic", "owner": "ETOTIST", "Label1": "REGRESSION", "Label2": "CAPACITY", "Label3": "ST_DYNAMIC", "Label4": "ST_MONTHLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37485.1.6.1": {"scope": "2Extended", "owner": "ETOTIST", "Label1": "REGRESSION", "Label2": "MAINTAINABILITY", "Label3": "ST_2EXTENDED", "Label4": "ST_BI-WEEKLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37512.4.6.10.1": {"scope": "2Extended", "owner": "ECSIGER", "Label1": "REGRESSION", "Label2": "CAPACITY", "Label3": "ST_2EXTENDED", "Label4": "ST_BI-WEEKLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37515.8.1.5.1": {"scope": "Basic", "owner": "ECSIGER", "Label1": "REGRESSION", "Label2": "CAPACITY", "Label3": "ST_BASIC", "Label4": "ST_DAILY", "Original Estimate": 86400, "Story Points": 3},
    "TC37512.4.4.18.23": {"scope": "Basic", "owner": "ECSIGER", "Label1": "REGRESSION", "Label2": "CAPACITY", "Label3": "ST_BASIC", "Label4": "ST_DAILY", "Original Estimate": 86400, "Story Points": 3},
    "TC37512.4.6.10.11": {"scope": "Dynamic", "owner": "ECSIGER", "Label1": "REGRESSION", "Label2": "CAPACITY", "Label3": "ST_DYNAMIC", "Label4": "ST_BI-WEEKLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37512.4.6.17.1": {"scope": "Dynamic", "owner": "ECSIGER", "Label1": "REGRESSION", "Label2": "CAPACITY", "Label3": "ST_DYNAMIC", "Label4": "ST_BI-WEEKLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37512.6.6.17.5": {"scope": "Dynamic", "owner": "ECSIGER", "Label1": "REGRESSION", "Label2": "CAPACITY", "Label3": "ST_DYNAMIC", "Label4": "ST_BI-WEEKLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37512.6.6.17.12": {"scope": "Dynamic", "owner": "ECSIGER", "Label1": "REGRESSION", "Label2": "CAPACITY", "Label3": "ST_DYNAMIC", "Label4": "ST_BI-WEEKLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC2020.5.6.9.5": {"scope": "2Extended", "owner": "ETHNYZ", "Label1": "REGRESSION", "Label2": "ROBUSTNESS", "Label3": "ST_2EXTENDED", "Label4": "ST_BI-WEEKLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC2020.5.6.14.1": {"scope": "Dynamic", "owner": "ETHNYZ", "Label1": "REGRESSION", "Label2": "ROBUSTNESS", "Label3": "ST_DYNAMIC", "Label4": "ST_BI-WEEKLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC1123.1.6.1.1": {"scope": "Dynamic", "owner": "ETHNYZ", "Label1": "REGRESSION", "Label2": "ROBUSTNESS", "Label3": "ST_DYNAMIC", "Label4": "ST_BI-WEEKLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC22687.1.1.2.1": {"scope": "Dynamic", "owner": "ETHNYZ", "Label1": "REGRESSION", "Label2": "ROBUSTNESS", "Label3": "ST_DYNAMIC", "Label4": "ST_BI-WEEKLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC22711.2.2.2.1": {"scope": "Extended", "owner": "ETHNYZ", "Label1": "REGRESSION", "Label2": "ROBUSTNESS", "Label3": "ST_EXTENDED", "Label4": "ST_WEEKLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37553.1.6.8": {"scope": "Dynamic", "owner": "ERKMIAP", "Label1": "REGRESSION", "Label2": "STABILITY", "Label3": "ST_DYNAMIC", "Label4": "ST_MONTHLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37512.6.6.11.25": {"scope": "2Dynamic", "owner": "ERKMIAP", "Label1": "REGRESSION", "Label2": "CAPACITY", "Label3": "ST_2DYNAMIC", "Label4": "ST_BI-MONTHLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37540.1.6.16": {"scope": "2Extended", "owner": "ERKMIAP", "Label1": "REGRESSION", "Label2": "STABILITY", "Label3": "ST_2EXTENDED", "Label4": "ST_BI-WEEKLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC1122.1.1.10.1": {"scope": "Extended", "owner": "ERKMIAP", "Label1": "REGRESSION", "Label2": "ROBUSTNESS", "Label3": "ST_EXTENDED", "Label4": "ST_WEEKLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37548.3.6.1": {"scope": "Extended", "owner": "ERKMIAP", "Label1": "REGRESSION", "Label2": "STABILITY", "Label3": "ST_EXTENDED", "Label4": "ST_WEEKLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37548.3.6.2": {"scope": "Extended", "owner": "ERKMIAP", "Label1": "REGRESSION", "Label2": "STABILITY", "Label3": "ST_EXTENDED", "Label4": "ST_WEEKLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37548.3.6.3": {"scope": "Extended", "owner": "ERKMIAP", "Label1": "REGRESSION", "Label2": "STABILITY", "Label3": "ST_EXTENDED", "Label4": "ST_WEEKLY", "Original Estimate": 14400, "Story Points": 0.5}
}
SCOPE_MAPPING = {
    "2Extended": 14,
    "Basic": 7 * SPRINT_WEEKS, # as only one ticket is needed per week
    "Dynamic": 14,
    "Extended": 7,
    "2Dynamic": 56
}
