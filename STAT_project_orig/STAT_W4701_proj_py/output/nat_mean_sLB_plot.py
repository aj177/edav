__author__ = 'Aarti'

import pandas as pd
import matplotlib.pyplot as plt
#from ggplot import *



# 2) Data preparation + exploration
df = pd.read_csv("sLB.csv")
#print df

#replace NaN in birth rate col with the mean
avg = round(df["B_rate"].mean(),0)
df["B_rate"].fillna(avg, inplace=True)


df["B_rate"].plot(kind='kde', style='r', xlim=(0,50),linewidth = 2)
plt.title('Singleton live birth distribution')



# descriptive statistics
#print train.describe()
#print train

# plots
# surv_1 = pd.crosstab([train.Sex], train.Survived.astype(bool))
# surv_1.plot(kind='bar', stacked=False, color=['red','green'], grid=False)
# plt.ylabel('count')
# plt.title('Survivors by Sex')
plt.show()