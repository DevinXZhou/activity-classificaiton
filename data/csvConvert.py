import csv
import numpy as np
name = 'subject10'
header = ['time', 'label', 'bpm', 'h0', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10', 'h11',
	'h12', 'o0', 'o1', 'o2', 'o3', 'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11',
	'c12', 'o4', 'o5', 'o6', 'o7', 'a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11',
	'a12', 'o8', 'o9', 'o10', 'o11']
additionalHeader = ['age', 'height', 'weight','minBPM', 'maxBPM']
#not adding sex information because there is only on female
#not adding dominant hand because there is only one left dominant han
#format: [age, height, weight, resting bpm, max bpm]
subjectInfor = [None, [27,182,83,75,193], [25,169,78,74,195], [31,187,92,68,189],
				[24,194,95,58,196],[26,180,73,70,194],[26,183,69,60,194],[23,173,86,60,197],
				[32,179,87,66,188],[31,168,65,54,189]]

header += additionalHeader
#process all files into one csv file
with open('subjectAll.csv','w', newline='') as writeFile:
	arr = [header]
	w = csv.writer(writeFile, delimiter = ',')
	
	for idx in range(1,10):	
		with open(name + str(idx) + '.dat') as readFile:
			for line in readFile:
				y = [] 
				for i in line.rstrip().split(' '):
					if i == 'NaN':
						y.append(None)
					else:
						y.append(i)
				y += subjectInfor[idx]
				arr.append(y)	
	w.writerows(arr)



#process all .dat files into single csv file

for idx in range(1,10):
	with open(name + str(idx) + '.dat') as readFile:
		arr = [header]
		for line in readFile:
			y = [] 
			for i in line.rstrip().split(' '):
				if i == 'NaN':
					y.append(None)
				else:
					y.append(i)
			y += subjectInfor[idx]
			arr.append(y)
		with open(name + str(idx) + '.csv','w', newline='') as writeFile:
			w = csv.writer(writeFile, delimiter = ',')
			w.writerows(arr)


	

#calculate mean in a time window
# output = [header]
# arr = []
# takeAvg = False
# for i in range(1,10):
# 	L = 0
# 	with open(name + str(i) + '.dat') as readFile:
# 		for line in readFile:
# 			L += 1
# 	print(L)
# 	with open(name + str(i) + '.dat') as readFile:
# 		idx = 0
# 		for line in readFile:
# 			y = []
# 			for i in line.rstrip().split(' '):
# 				if i == 'NaN':
# 					y.append(np.nan)
# 				else:
# 					y.append(float(i))

# 			if len(arr)>0 and (not np.isnan(y[2]) or idx+1 == L):
# 				arr.append(y)
# 				takeAvg = True

				
# 			if takeAvg:
# 				means = np.nanmean(arr, axis=0)
# 				lab = means[1]
# 				if lab == int(lab):
# 					strMean = []
# 					for m in means:
# 						if m == np.nan:
# 							strMean.append(None)
# 						else:
# 							strMean.append(format(m, '.4f'))
# 					output.append(strMean)
# 				arr = []
# 				takeAvg = False
# 			else:
# 				arr.append(y)
# 			idx += 1

# with open('dataMean.csv','w', newline='') as writeFile:
# 	w = csv.writer(writeFile, delimiter = ',')
# 	w.writerows(output)

					
	