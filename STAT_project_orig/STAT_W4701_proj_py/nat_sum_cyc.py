__author__ = 'Aarti'

import pandas as pd

year = 1999

#Live Births

# fresh NonDonor
df = pd.read_csv("1999.csv", usecols=["ClinStateCode","FshNDCycle1","FshNDCycle2","FshNDCycle3","FshNDCycle4"])
df.replace ("=", "0", inplace = True)
df["Year"] = year

# convert numeric columns from dtype object to float
df[["FshNDCycle1","FshNDCycle2","FshNDCycle3","FshNDCycle4"]] \
    = df[["FshNDCycle1","FshNDCycle2","FshNDCycle3","FshNDCycle4"]].astype(float)

# set display to 2 decimal points
pd.set_option('precision',3)

# pivot data by year
table_fshND = pd.pivot_table(df, values=["FshNDCycle1","FshNDCycle2","FshNDCycle3","FshNDCycle4"], rows=["Year"], aggfunc='sum', margins=False)



# frozen NonDonor
df = pd.read_csv("1999.csv", usecols=["ClinStateCode","ThwNDTransfers1","ThwNDTransfers2","ThwNDTransfers3","ThwNDTransfers4"])
df.replace ("=", "0", inplace = True)
df["Year"] = year

# convert numeric columns from dtype object to float
df[["ThwNDTransfers1","ThwNDTransfers2","ThwNDTransfers3","ThwNDTransfers4"]] \
    = df[["ThwNDTransfers1","ThwNDTransfers2","ThwNDTransfers3","ThwNDTransfers4"]].astype(float)

# set display to 2 decimal points
pd.set_option('precision',3)

# pivot data by year
table_thwND = pd.pivot_table(df, values=["ThwNDTransfers1","ThwNDTransfers2","ThwNDTransfers3","ThwNDTransfers4"], rows=["Year"], aggfunc='sum', margins=False)



# fresh Donor
df = pd.read_csv("1999.csv", usecols=["ClinStateCode","FshDnrTransfers"])
df.replace ("=", "0", inplace = True)
df["Year"] = year

# convert numeric columns from dtype object to float
df[["FshDnrTransfers"]] = df[["FshDnrTransfers"]].astype(float)

# set display to 2 decimal points
pd.set_option('precision',3)

# pivot data by year
table_fshD = pd.pivot_table(df, values=["FshDnrTransfers"], rows=["Year"], aggfunc='sum', margins=False)



# frozen Donor
df = pd.read_csv("1999.csv", usecols=["ClinStateCode","ThwDnrTransfers"])
df.replace ("=", "0", inplace = True)
df["Year"] = year

# convert numeric columns from dtype object to float
df[["ThwDnrTransfers"]] = df[["ThwDnrTransfers"]].astype(float)

# set display to 2 decimal points
pd.set_option('precision',3)

# pivot data by year
table_thwD = pd.pivot_table(df, values=["ThwDnrTransfers"], rows=["Year"], aggfunc='sum', margins=False)



#output df to a SINGLE csv for dataviz in R
table = pd.concat([table_fshND, table_thwND, table_fshD, table_thwD], axis=1)
#print table
#table.to_csv('nat_sum_cyc')



#append df for 2011
#df = pd.read_csv("2011.csv", usecols=["FshNDCycle1","FshNDCycle2","FshNDCycle3","FshNDCycle4","FshNDCycle5","FshNDCycle6",
#"ThwNDTotCycles1","ThwNDTotCycles2","ThwNDTotCycles3","ThwNDTotCycles4","ThwNDTotCycles5","ThwNDTotCycles6","FshDnrTotCycles","ThwDnrTotCycles"])
#print df
#df.to_csv('nat_sum_cyc', mode='a', header=False)



#append df for for 2010 thru 1999
table.to_csv('nat_sum_cyc', mode='a', header=True)