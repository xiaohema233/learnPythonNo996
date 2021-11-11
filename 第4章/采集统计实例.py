import requests,xlwt,time, random
file = xlwt.Workbook()
month=["201903","201904","201905","201906","201907","201908",
"201909","201910","201911","201912","202001","202002","202003"]
for i in range(len(month)):
	params = {'m': 'QueryData','code': 'AA020B','wds': '[{"wdcode":"reg","valuecode":"000000"},{"wdcode":"sj","valuecode":'+month[i]+'}]'}
	r = requests.get("https://×.×.×.×",params= params)
	time.sleep(random.randint(5,10)+random.random())
	dict =r.json()
	data=dict["exceltable"]
	table = file.add_sheet(month[i])
	n=len(data)
	for j in range(n):
		row=data[j]['row']
		col=data[j]['col']
		value=data[j]['data']
		table.write(row,col,value)
file.save('工业增加值增长速度.xls')
