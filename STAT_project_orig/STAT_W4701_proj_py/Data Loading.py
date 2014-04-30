__author__ = 'Aarti'

import pandas as pd
import numpy as np
import locale


# Assemble all of the data files into a single DataFrame + add a year field

# years = range(1999, 2012)
#
# for year in years:
#path = 2012.csv

year = 2012

#eggs categories
# fresh Non-Donor
fshNDcyc = ["FshNDCycle1","FshNDCycle2","FshNDCycle3","FshNDCycle4","FshNDCycle5","FshNDCycle6"]
fshNDsB = ["FshNDSnglLBRate1","FshNDSnglLBRate2","FshNDSnglLBRate3","FshNDSnglLBRate4","FshNDSnglLBRate5","FshNDSnglLBRate6"]
fshNDtB = ["FshNDTripLBRate1","FshNDTripLBRate2","FshNDTripLBRate3","FshNDTripLBRate4","FshNDTripLBRate5","FshNDTripLBRate6"]

# frozen Non-Donor
thwNDcyc = ["ThwNDTotCycles1","ThwNDTotCycles2","ThwNDTotCycles3","ThwNDTotCycles4","ThwNDTotCycles5","ThwNDTotCycles6"]
thwNDsB = ["ThwNDSnglLB_TransRate1","ThwNDSnglLB_TransRate2","ThwNDSnglLB_TransRate3","ThwNDSnglLB_TransRate4","ThwNDSnglLB_TransRate5","ThwNDSnglLB_TransRate6"]
thwNDtB = ["ThwNDTripLB_TransRate1","ThwNDTripLB_TransRate2","ThwNDTripLB_TransRate3","ThwNDTripLB_TransRate4","ThwNDTripLB_TransRate5","ThwNDTripLB_TransRate6"]

# fresh Donor
fshDcyc = ["FshDnrTotCycles"]
fshDsB = ["FshDnrSnglLB_TransRate"]
fshDb = ["FshDnrLvBirths_TransRate"]

# frozen Donor
thwDcyc = ["ThwDnrTotCycles"]
thwDsB = ["ThwDnrSnglLB_TransRate"]
thwDb = ["ThwDnrLvBirths_TransRate"]

#implantation procedures categories
imp_procd = ["IVF_Rate","PGD_Rate"]


df = pd.read_csv("2012.csv", usecols=["ClinStateCode","IVF_Rate","PGD_Rate","FshNDCycle1","FshNDCycle2","FshNDCycle3",
"FshNDCycle4",
"FshNDCycle5",
"FshNDCycle6",
"FshNDSnglLBRate1",
"FshNDSnglLBRate2",
"FshNDSnglLBRate3",
"FshNDSnglLBRate4",
"FshNDSnglLBRate5",
"FshNDSnglLBRate6",
"FshNDTripLBRate1",
"FshNDTripLBRate2",
"FshNDTripLBRate3",
"FshNDTripLBRate4",
"FshNDTripLBRate5",
"FshNDTripLBRate6",
"ThwNDTotCycles1",
"ThwNDTotCycles2",
"ThwNDTotCycles3",
"ThwNDTotCycles4",
"ThwNDTotCycles5",
"ThwNDTotCycles6",
"ThwNDSnglLB_TransRate1",
"ThwNDSnglLB_TransRate2",
"ThwNDSnglLB_TransRate3",
"ThwNDSnglLB_TransRate4",
"ThwNDSnglLB_TransRate5",
"ThwNDSnglLB_TransRate6",
"ThwNDTripLB_TransRate1",
"ThwNDTripLB_TransRate2",
"ThwNDTripLB_TransRate3",
"ThwNDTripLB_TransRate4",
"ThwNDTripLB_TransRate5",
"ThwNDTripLB_TransRate6",
"FshDnrTotCycles",
"ThwDnrTotCycles",
"FshDnrSnglLB_TransRate",
"ThwDnrSnglLB_TransRate",
"FshDnrLvBirths_TransRate",
"ThwDnrLvBirths_TransRate",])


# convert object fields into float
#df["IVF_Rate"] = df["IVF_Rate"].apply(locale.atof)

# df.replace('%','',regex=True).astype('float')/100
# print df

#insert year field to the dataframe
df["Year"] = year


# pivot tables
#ANNUAL
# by state
# table = pd.pivot_table(df, values=["FshNDCycle1","FshNDCycle2","FshNDCycle3","FshNDCycle4","FshNDCycle5","FshNDCycle6"], rows =['ClinStateCode', "Year"], aggfunc='mean', margins=False)
# print str(year) + ' pivot' + str(table)

#output df to csv for dataviz in R
#table.to_csv('fshND')

#NATIONAL SUMMARY
#nat_table = pd.pivot_table(df, values=["FshNDSnglLBRate1","FshNDSnglLBRate2","FshNDSnglLBRate3","FshNDSnglLBRate4","FshNDSnglLBRate5","FshNDSnglLBRate6"], rows =["Year"], aggfunc='mean', margins=False)
#print nat_table



# #output df to a SINGLE csv for dataviz in R
# nat_table.to_csv('nat_sum')


#procd_table = pd.pivot_table(df, values=['IVF_Rate'], rows =["ClinStateCode", "Year"], aggfunc='mean', margins=False)
#print procd_table


