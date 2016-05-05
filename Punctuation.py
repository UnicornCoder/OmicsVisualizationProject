#!/usr/binpython
# -*- coding: utf-8 -*-  

"""
Program to create a numeric punctuation matrix, where columns are the patients and rows 
diseases.
Author: Carmen Bravo
Version: 2.0
"""

#Open files.
RiskMatrix = open("RiskMatrix.txt")
Output = open("PointsMatrix.txt", "w")

header = RiskMatrix.readline().split("\t")
header.pop(2)
Output.write("\t".join(header))

#Create an array with the rows of the risk matrix.
Matrix1 = []
for row in RiskMatrix:
	row.split("\n")
	Matrix1.append(row.split("\t"))
	
"""
Give a numerical punctuation to the genotypes. We will consider ++ as -3 (the genotype
reduces more than 3 times the chances of developing the disease), + as -1 (the genotype
reduces less than 3 times the chances of developing the disease), . as 0 (no effect), - as 1 
(the genotype increases less than 3 times the chances of developing the disease) and
-- as 3 (the genotype reduces more than 3 times the chances of developing the disease).
"""
for row in Matrix1:
	row[-1] = row[-1].replace("\n", "")
	row.pop(2)
	i = 0
	while i < len(row):
		if row[i] == "++": #Less likely to present the trait/disease.
			row[i] = -3
		if row[i] == "+":
			row[i] = -1
		if row[i] == ".":
			row[i] = 0
		if row[i] == "-":
			row[i] = 1
		if row[i] == "--":
			row[i] = 3	#More likely to present the trait/disease.
		i += 1

		
#Aggregate SNPs corresponding to the same disease. We suppose additive effects.
DiseaseList = []
Matrix2 = []
for row in Matrix1:
	row2 = []
	for element in row:
		row2.append(element)
	if row[1] in DiseaseList:
		Matrix2[-1][2:] = [x+y for x,y in zip(row2[2:], Matrix2[-1][2:])]
	if row[1] not in DiseaseList:
		Matrix2.append(row2)
		DiseaseList.append(row2[1])


#Produce "All traits/diseases" row for each type, which corresponds to the aggregation 
#of all diseases corresponding to a type.
TypeList = []
Matrix3 = []
for row in Matrix2:
	row2 = []
	for element in row:
		row2.append(element)
	if row[0] in TypeList:
		Matrix3[-1][2:] = [x+y for x,y in zip(row2[2:], Matrix3[-1][2:])]
	if row[0] not in TypeList:
		row2[1] = "All traits/diseases"
		Matrix3.append(row2)
		TypeList.append(row2[0])

#Put all rows together and sort them by alphabetical order.
for row in sorted(Matrix2+Matrix3):
	row = [str(x) for x in row]
	row[-1] = row[-1] + "\n"
	Output.write("\t".join(row))
	
Output.close()
	



