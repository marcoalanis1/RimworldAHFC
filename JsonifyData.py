import json
import copy
f = open("C:\\Users\\fucku\\Documents\\output.json", "w")
file = open("C:\\Users\\fucku\\Documents\\test.txt", "r")
n = 0
Hdone= False
for i in file:
	i = i.strip()
	
	if "!" in i and not Hdone:
		headers = i.strip().split("!")
		dataset = []
		data = {}
		for j in headers:
			if len(j) != 0:
				data[j.strip()] = ''
		Hdone = True
	elif "| " == i[0:2]:
		datapoint = i[2:]
		datapoint = datapoint.replace("[[","")
		datapoint = datapoint.replace("]]","")
		datapoint = datapoint.split("||")
		m = 0
		for k in headers:
			if len(k) != 0:
				data[k.strip()] = datapoint[m].strip()
				m+=1
		dataset.append(copy.copy(data))
f.write(json.dumps(dataset))
file.close()
f.close()
