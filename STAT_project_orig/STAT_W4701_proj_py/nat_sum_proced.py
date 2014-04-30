__author__ = 'Aarti'

import pandas as pd

year = 2012

#implantation procedures categories ONLY FOR fresh NonDonor eggs
df = pd.read_csv("2012.csv", usecols=["ClinStateCode","IVF_Rate","PGD_Rate"])
df.replace ("=", "0", inplace = True)
df["Year"] = year


# convert numeric columns from dtype object to float
df[["IVF_Rate","PGD_Rate"]] = df[["IVF_Rate","PGD_Rate"]].astype(float)
#print df.dtypes

# set display to 2 decimal points
pd.set_option('precision',3)

# pivot data by year
table_procd = pd.pivot_table(df, values=["IVF_Rate","PGD_Rate"], rows=["Year"], aggfunc='mean', margins=False)
print table_procd



# output procedure summary to a SINGLE csv for dataviz in R
table_procd.to_csv('procd_sum')