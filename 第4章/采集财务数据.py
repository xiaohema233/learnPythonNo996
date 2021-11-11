import requests,time, random,re
r = requests.get("https://×.×.×.×")    
txt=r.text.split('<table id="Table0">')[1].split('<div class="name" id="fxxg">')[0].replace('\n', '').replace('\r', '').replace(' ', '')
lst = re.findall('<thclass="tips-fieldnameL".*?>(.*?)</th>.*?{{jbzl.(.*?)}}',txt)
dict_CompanySurvey=dict(lst)
r = requests.get("https://×.×.×.×")
txt=r.text.split('<script type="text/template" id="tmpl_dbfx">')[0].replace('\n', '').replace('\r', '').replace(' ', '')
lst = re.findall('<tdclass="tips-fieldname-Left"><span>(.*?)</span>.*?<tdclass="tips-data-Right"><span>{{value.(.*?)}}',txt)
dict_NewFinanceAnalysis=dict(lst)
codes=["SH600104","SH601238","SH600297","SH600418","SZ002594"]
for code in codes:
    r = requests.get("https://×.×.×.×"+code)
    time.sleep(random.randint(1,3)+random.random())
    dict_CompanySurvey_Value =r.json()
    r = requests.get("https://×.×.×.×"+code)
    time.sleep(random.randint(1,3)+random.random())
    dict_NewFinanceAnalysis_Value =r.json()
    with open(code+'基本资料.txt', 'w') as f: 
        for key,value in dict_CompanySurvey.items():
            f.write(key+'|'+dict_CompanySurvey_Value["jbzl"][value]+'\n')
    with open(code+'财务指标.txt', 'w') as f: 
        for key,value in dict_NewFinanceAnalysis.items():
            txt=key
            for Value in dict_NewFinanceAnalysis_Value:
                txt=txt+'|'+Value[value]
            f.write(txt+'\n')
