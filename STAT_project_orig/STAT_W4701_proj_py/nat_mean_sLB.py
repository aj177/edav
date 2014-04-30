__author__ = 'Aarti'

import pandas as pd

year = 1999

# Success measurement
#SINGLE Live Births

# fresh NonDonor
df = pd.read_csv("1999.csv", usecols=["ClinStateCode","FshNDLvBirthsRate1","FshNDLvBirthsRate2","FshNDLvBirthsRate3","FshNDLvBirthsRate4"])
df.replace ("=", "0", inplace = True)
df["Year"] = year

# convert numeric columns from dtype object to float
df[["FshNDLvBirthsRate1","FshNDLvBirthsRate2","FshNDLvBirthsRate3","FshNDLvBirthsRate4"]] \
    = df[["FshNDLvBirthsRate1","FshNDLvBirthsRate2","FshNDLvBirthsRate3","FshNDLvBirthsRate4"]].astype(float)

# set display to 2 decimal points
pd.set_option('precision',3)

# pivot data by year
table_fshND = pd.pivot_table(df, values=["FshNDLvBirthsRate1","FshNDLvBirthsRate2","FshNDLvBirthsRate3","FshNDLvBirthsRate4"], rows=["Year"], aggfunc='mean', margins=False)



# frozen NonDonor
df = pd.read_csv("1999.csv", usecols=["ClinStateCode","ThwNDLvBirthsRate1","ThwNDLvBirthsRate2","ThwNDLvBirthsRate3","ThwNDLvBirthsRate4"])
df.replace ("=", "0", inplace = True)
df["Year"] = year

# convert numeric columns from dtype object to float
df[["ThwNDLvBirthsRate1","ThwNDLvBirthsRate2","ThwNDLvBirthsRate3","ThwNDLvBirthsRate4"]] = df[["ThwNDLvBirthsRate1","ThwNDLvBirthsRate2","ThwNDLvBirthsRate3","ThwNDLvBirthsRate4"]].astype(float)

# set display to 2 decimal points
pd.set_option('precision',3)

# pivot data by year
table_thwND = pd.pivot_table(df, values=["ThwNDLvBirthsRate1","ThwNDLvBirthsRate2","ThwNDLvBirthsRate3","ThwNDLvBirthsRate4"], rows=["Year"], aggfunc='mean', margins=False)



# fresh Donor
df = pd.read_csv("1999.csv", usecols=["ClinStateCode","FshDnrLvBirthsRate"])
df.replace ("=", "0", inplace = True)
df["Year"] = year

# convert numeric columns from dtype object to float
df[["FshDnrLvBirthsRate"]] = df[["FshDnrLvBirthsRate"]].astype(float)

# set display to 2 decimal points
pd.set_option('precision',3)

# pivot data by year
table_fshD = pd.pivot_table(df, values=["FshDnrLvBirthsRate"], rows=["Year"], aggfunc='mean', margins=False)



# frozen Donor
df = pd.read_csv("1999.csv", usecols=["ClinStateCode","ThwDnrLvBirthsRate"])
df.replace ("=", "0", inplace = True)
df["Year"] = year

# convert numeric columns from dtype object to float
df[["ThwDnrLvBirthsRate"]] = df[["ThwDnrLvBirthsRate"]].astype(float)

# set display to 2 decimal points
pd.set_option('precision',3)

# pivot data by year
table_thwD = pd.pivot_table(df, values=["ThwDnrLvBirthsRate"], rows=["Year"], aggfunc='mean', margins=False)



#output df to a SINGLE csv for dataviz in R
table = pd.concat([table_fshND, table_thwND, table_fshD, table_thwD], axis=1)
#print table
#table.to_csv('nat_mean_sLB')



#append df for 2011
# df = pd.read_csv("2011.csv", usecols=["FshNDSnglLBRate1","FshNDSnglLBRate2","FshNDSnglLBRate3","FshNDSnglLBRate4","FshNDSnglLBRate5","FshNDSnglLBRate6",
# "ThwNDLvBirthsRate1","ThwNDLvBirthsRate2","ThwNDLvBirthsRate3","ThwNDLvBirthsRate4","ThwNDLvBirthsRate5","ThwNDLvBirthsRate6",
# "FshDnrLvBirthsRate", "ThwDnrLvBirthsRate"])
# df.insert(0, "Year", 2011)
# print df
# df.to_csv('nat_mean_sLB', mode='a', header=False)



#append df for for 2010 thru 1999
table.to_csv('nat_mean_sLB', mode='a', header=True)

