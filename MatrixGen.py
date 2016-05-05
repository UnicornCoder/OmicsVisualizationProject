#!/usr/binpython
# -*- coding: utf-8 -*-  

"""
Program to create a symbolic punctuation matrix, where columns are the patients and rows SNPs.
Author: Carmen Bravo
Version: 2.0
"""

#Open files.
Patient = open("SelectedHgdpSNPs.txt")
Disease = open("SelectedRiskSNPs.txt")
Output = open("RiskMatrix.txt", "w")

#Add header to the file. Creates a list with the id of the patient.
patientList = Patient.readline().split("\t")
patientList.pop(0)
header = "Type" + "\t" + "Disease" + "\t" + "SNP" + "\t" + "\t".join(patientList)
Output.write(header)
patientList[-1] = patientList[-1].replace("\r\n", "") 
Disease.readline()

#Collect the SNP genotypes for each patient.
patientArray=[]
for line1 in Patient:
	Prow = line1.split("\t")
	Prow[-1] = Prow[-1].replace("\r\n", "") 
	patientArray.append(Prow)

#Collect the SNP name, type of disease, disease, possible alleles and value (++, +, ., -, --).
diseaseArray=[]
for line2 in Disease:
	Drow = line2.split("\t")
	Drow[-1] = Drow[-1].replace("\n", "")
	diseaseArray.append(Drow)


#Create matrix with SNPs (id + type of disease + disease) as rows and the value for each 
#patient (column). Column names(patients) were included before as header. If the genotype
#is unknown for a patient, we will consider no effect (.).
Matrix=[]
for Prow in patientArray:
	for Drow in diseaseArray:
		if Drow[0] == Prow[0]:
			row = [None]*len(Prow)
			row[0] = Drow[1]	
			i = 1
			while i < len(Prow):
				if Prow[i] == Drow[3] or Prow[i] == Drow[3][::-1]:
					row[i] = Drow[6]
				if Prow[i] == Drow[4].replace(" ", "") or Prow[i] == Drow[4].replace(" ", "")[::-1]: 
					row[i] = Drow[7]
				if Prow[i] == Drow[5].replace(" ", "") or Prow[i] == Drow[5].replace(" ", "")[::-1]:
					row[i] = Drow[8]
				if Prow[i] == "--":
					row[i] = "."
				i = i + 1
			row.insert(1, Drow[2])
			row.insert(2, Prow[0])
			row[-1] = row[-1] + "\n"
			Matrix.append(row)
			
#Write rows in the file.
for row in sorted(Matrix):
	Output.write("\t".join(row))
	
Output.close()
