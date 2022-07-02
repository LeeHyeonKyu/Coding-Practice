from collections import defaultdict

def solution(id_list, report, k):
    rptd_rpt = defaultdict(set)
    for report_reported in report:
        rpt, rptd = report_reported.split()
        rptd_rpt[rptd].add(rpt)
    
    id_mail = defaultdict(int)
    for rptd, rpt in rptd_rpt.items():
        if len(rpt) >= k:
            for rpt_id in list(rpt):
                id_mail[rpt_id] += 1
    
    return [id_mail[id] for id in id_list]