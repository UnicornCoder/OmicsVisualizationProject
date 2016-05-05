#!/usr/binpython
# -*- coding: utf-8 -*-  

import os
import shutil

"""
Program to filter the HGDP data for selecting only those SNPs of interest. In this case,
we are using the data collected from Eupedia to select the SNPs related to disease.
Author: Carmen Bravo
Version: 2.0
"""

#Open files.
HgdpSNP = open("HGDP_FinalReport_Forward.txt")
RiskSNP = open("RiskSNPs.txt", "U")
RiskSNPList = open("RiskSNPsList.txt", "U").read().split()

#Create new folder with output files. Delete the folder if it is already there.
dir = "/Users/MissBravo/Desktop/Omics Final Project/Data_treatment/SelectedSNPs"
if os.path.exists(dir):
    shutil.rmtree(dir)
os.makedirs(dir)
os.chdir("/Users/MissBravo/Desktop/Omics Final Project/Data_treatment/SelectedSNPs")
OutputHgdp = open("SelectedHgdpSNPs.txt", "w")
OutputRisk = open("SelectedRiskSNPs.txt", "w")
SelectedSNPsList = open("SelectedSNPsList.txt", "w")
RepeatedSNPs = open("RepeatedSNPsList.txt", "w")

#Add the header. The header contains the subjects' identifiers.
OutputHgdp.write(HgdpSNP.readline())

#Add the header. The header contains SNPs and disease information.
OutputRisk.write(RiskSNP.readline())

#Selecting the rows of interest (the ones that correspond to disease SNPs).
SNPList = [] #To avoid duplicates.
for row in HgdpSNP:
	if row.split()[0] in RiskSNPList:
			OutputHgdp.write(row)
			if row.split()[0] not in SNPList:
				SNPList.append(row.split()[0])
				SelectedSNPsList.write(row.split()[0] + "\n")
				
OutputHgdp.close()
SelectedSNPsList.close()

#Select SNPs from the risk alleles list.
RepeatedSNP = []
for row in RiskSNP:
	if row.split()[0] in SNPList:
		OutputRisk.write(row)
		if row.split()[0] in RepeatedSNP:
			RepeatedSNPs.write(row.split()[0] + "\n")
		else:
			RepeatedSNP.append(row.split()[0])
	
OutputRisk.close()
RepeatedSNPs.close()




