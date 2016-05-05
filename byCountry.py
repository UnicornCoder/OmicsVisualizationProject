#!/usr/binpython
# -*- coding: utf-8 -*-  

from decimal import Decimal, ROUND_HALF_UP

"""
Program to group the columns by country. Values are divided by the total number of samples per country.
Author: Carmen Bravo
Version: 2.0
"""

#Open files.
PointsMatrix = open("PointsMatrix.txt")
IDCountry = open("ID-country.txt")
Output = open("CountryMatrix.txt", "w")


#Create a dictionary with the patients ID as key and his/her country as value.
#HGDP00597 is not included in the extra information file from HGDP.
map={"Type" : "Type", "Disease" : "Disease", "HGDP00597" : "Unknown"}
for line in IDCountry:
	split = line.split("\r")
	for tuple in split:
		list = tuple.split("\t")
		map[list[0]]=list[1]


#Create header with countries instead of patient IDs.
header = PointsMatrix.readline().split("\t")
header.pop(2)
header[-1] = header[-1].replace("\r\n", "")
header = [map[ID] for ID in header]

#TandD collects the type, disease per row. The matrix collects the punctuation for each row.
TandD = [["Type", "Disease"]]
Matrix = []
for line in PointsMatrix:
	row = line.split("\t")
	row[-1] = row[-1].replace("\n", "")
	TandD.append([row[0], row[1]])
	row = [int(x) for x in row[2:]]
	Matrix.append(row)


#Obtain list of countries present in the study. 	
countryList =[]
for country in header:
	if country not in countryList and country != "Type" and country != "Disease" and country != "Unknown":
		countryList.append(country)
	
#Sum up the points corresponding to patients from the same country and divide by the number
#of subjects in that country.
Matrixcol=[]
for country in countryList:
	column = [0]*len(Matrix)
	indices = [i for i, x in enumerate(header) if x == country]
	for index in indices:
		handle = []
		for row in Matrix:
			handle.append(row[index-2])
		column = [x + y for x,y in zip(handle, column)]
	column = [Decimal(float(x)/len(indices)) for x in column]
	column.insert(0, country)
	Matrixcol.append(column)
	

#Create rows with type, disease and points per country and subject in that country. 
#Each number is expressed with 2 decimals.
i=0
while i < len(TandD):
 	for column in Matrixcol:
 		if i != 0:
 			value = Decimal(column[i].quantize(Decimal('.01'), rounding=ROUND_HALF_UP))
 		else:
 			value = column[i]
 		TandD[i].append(value)
 	i += 1			

#Write a header with numbers from 0 to 24. Necessary for working afterwards with p5.
x = [str(i) for i in xrange(len(Matrixcol) + 2)]
x[-1] = x[-1] + "\n"
Output.write("\t".join(x))
	
#Write the rows in the output file. 
for row in TandD:
	row = [str(x) for x in row]
	row[-1] = row[-1] + "\n"
	Output.write("\t".join(row))
	
Output.close()
	

		
	
