__author__ = 'Aarti'

import pandas as pd


year = 1999

# Surveillance measurement
# Triplet Live Births
# Cancellation Rate

# fresh NonDonor Triplet lb rate
df = pd.read_csv("1999.csv", usecols=["ClinStateCode","FshNDMultInfsRate1","FshNDMultInfsRate2","FshNDMultInfsRate3","FshNDMultInfsRate4"])
df.replace ("=", "0", inplace = True)
df["Year"] = year

# convert numeric columns from dtype object to float
df[["FshNDMultInfsRate1","FshNDMultInfsRate2","FshNDMultInfsRate3","FshNDMultInfsRate4"]] \
    = df[["FshNDMultInfsRate1","FshNDMultInfsRate2","FshNDMultInfsRate3","FshNDMultInfsRate4"]].astype(float)

# set display to 2 decimal points
pd.set_option('precision',3)

# pivot data by year
table_fshND = pd.pivot_table(df, values=["FshNDMultInfsRate1","FshNDMultInfsRate2","FshNDMultInfsRate3","FshNDMultInfsRate4"], rows=["Year"], aggfunc='mean', margins=False)



# fresh NonDonor Cancellation rate
df = pd.read_csv("1999.csv", usecols=["ClinStateCode","FshNDCansRate1","FshNDCansRate2","FshNDCansRate3","FshNDCansRate4"])
df.replace ("=", "0", inplace = True)
df["Year"] = year

# convert numeric columns from dtype object to float
df[["FshNDCansRate1","FshNDCansRate2","FshNDCansRate3","FshNDCansRate4"]] \
    = df[["FshNDCansRate1","FshNDCansRate2","FshNDCansRate3","FshNDCansRate4"]].astype(float)

# set display to 2 decimal points
pd.set_option('precision',3)

# pivot data by year
table_fshND_cxl = pd.pivot_table(df, values=["FshNDCansRate1","FshNDCansRate2","FshNDCansRate3","FshNDCansRate4"], rows=["Year"], aggfunc='mean', margins=False)



# # frozen NonDonor
# df = pd.read_csv("2010.csv", usecols=["ClinStateCode","ThwNDMultInfs_TransRate1","ThwNDMultInfs_TransRate2","ThwNDMultInfs_TransRate3","ThwNDMultInfs_TransRate4","ThwNDMultInfs_TransRate5"])
# df.replace ("=", "0", inplace = True)
# df["Year"] = year
#
# # convert numeric columns from dtype object to float
# df[["ThwNDMultInfs_TransRate1","ThwNDMultInfs_TransRate2","ThwNDMultInfs_TransRate3","ThwNDMultInfs_TransRate4","ThwNDMultInfs_TransRate5"]] = df[["ThwNDMultInfs_TransRate1","ThwNDMultInfs_TransRate2","ThwNDMultInfs_TransRate3","ThwNDMultInfs_TransRate4","ThwNDMultInfs_TransRate5"]].astype(float)
#
# # set display to 2 decimal points
# pd.set_option('precision',3)
#
# # pivot data by year
# table_thwND = pd.pivot_table(df, values=["ThwNDMultInfs_TransRate1","ThwNDMultInfs_TransRate2","ThwNDMultInfs_TransRate3","ThwNDMultInfs_TransRate4","ThwNDMultInfs_TransRate5","ThwNDMultInfs_TransRate6"], rows=["Year"], aggfunc='mean', margins=False)
#
#
#
# # fresh Donor
# df = pd.read_csv("2010.csv", usecols=["ClinStateCode","FshDnrSnglLB_TransRate", "FshDnrLvBirths_TransRate"])
# df.replace ("=", "0", inplace = True)
# df["Year"] = year
#
#
# # convert numeric columns from dtype object to float
# df[["FshDnrLvBirths_TransRate"]] = df[["FshDnrLvBirths_TransRate"]].astype(float)
# df[["FshDnrSnglLB_TransRate"]] = df[["FshDnrSnglLB_TransRate"]].astype(float)
#
# # compute FshDnrMultInfs_TransRate as difference between singleton and total live births
# df["FshDnrMultInfs_TransRate"] = df["FshDnrLvBirths_TransRate"] - df["FshDnrSnglLB_TransRate"]
#
# # set display to 2 decimal points
# pd.set_option('precision',3)
#
# # pivot data by year
# table_fshD = pd.pivot_table(df, values=["FshDnrMultInfs_TransRate"], rows=["Year"], aggfunc='mean', margins=False)
#
#
#
# # frozen Donor
# df = pd.read_csv("2010.csv", usecols=["ClinStateCode","ThwDnrSnglLB_TransRate", "ThwDnrLvBirths_TransRate"])
# df.replace ("=", "0", inplace = True)
# df["Year"] = year
#
# # convert numeric columns from dtype object to float
# df[["ThwDnrSnglLB_TransRate"]] = df[["ThwDnrSnglLB_TransRate"]].astype(float)
# df[["ThwDnrLvBirths_TransRate"]] = df[["ThwDnrLvBirths_TransRate"]].astype(float)
#
# # compute ThwDnrMultInfs_TransRate as difference between singleton and total live births
# df["ThwDnrMultInfs_TransRate"] = df["ThwDnrLvBirths_TransRate"] - df["ThwDnrSnglLB_TransRate"]
#
# # set display to 2 decimal points
# pd.set_option('precision',3)
#
# # pivot data by year
# table_thwD = pd.pivot_table(df, values=["ThwDnrMultInfs_TransRate"], rows=["Year"], aggfunc='mean', margins=False)
#


#output df to a SINGLE csv for dataviz in R
#table = pd.concat([table_fshND, table_thwND, table_fshD, table_thwD, table_fshND_cxl], axis=1)
table = pd.concat([table_fshND, table_fshND_cxl], axis=1)
#print table
#table.to_csv('nat_mean_surveil')



#append df for 2011
# df = pd.read_csv("2011.csv", usecols=["FshNDMultInfsRate1","FshNDMultInfsRate2","FshNDMultInfsRate3","FshNDMultInfsRate4","FshNDMultInfsRate5","FshNDMultInfsRate6",
# "ThwNDMultInfs_TransRate1","ThwNDMultInfs_TransRate2","ThwNDMultInfs_TransRate3","ThwNDMultInfs_TransRate4","ThwNDMultInfs_TransRate5","ThwNDMultInfs_TransRate6"])
#
# # compute FshDnrMultInfs_TransRate as difference between singleton and total live births
# comp_1 = pd.read_csv("2011.csv", usecols=["FshDnrSnglLB_TransRate", "FshDnrLvBirths_TransRate"])
# comp_1["FshDnrMultInfs_TransRate"] = comp_1["FshDnrLvBirths_TransRate"] - comp_1["FshDnrSnglLB_TransRate"]
# comp_1 = comp_1.drop(comp_1.columns[0:2], axis =1)
#
#
# # compute ThwDnrMultInfs_TransRate as difference between singleton and total live births
# comp_2 = pd.read_csv("2011.csv", usecols=["ThwDnrSnglLB_TransRate", "ThwDnrLvBirths_TransRate"])
# comp_2["ThwDnrMultInfs_TransRate"] = comp_2["ThwDnrLvBirths_TransRate"] - comp_2["ThwDnrSnglLB_TransRate"]
# comp_2 = comp_2.drop(comp_2.columns[0:2], axis =1)
#
# table = pd.concat([df, comp_1, comp_2], axis=1)
#
# table.insert(0, "Year", 2011)

table.to_csv('nat_mean_surveil', mode='a', header=True)