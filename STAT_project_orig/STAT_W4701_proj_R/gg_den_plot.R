library(ggplot2)
library (plyr)
library(KernSmooth)

#SUCCESS METRICS
df = read.csv("~/Desktop/STAT_project/sLB.csv")

#subset the dataframe on conditions
df_ND = subset(df, Donor==0)
df_ND = subset (df, Age < 46)
df_ND$row.names = NULL

# replace NaN with mean for that group
impute.mean = function(x) replace(x, is.na(x), mean(x, na.rm = TRUE))
df_ND_m <- ddply(df_ND, ~ Year, transform, B_rate = impute.mean(B_rate))

#kernel density plot
x = df_ND_m$B_rate
est = bkde (x, kernel="epanech")
plot(est, type="l")

#kernel density plot
#sLB = ggplot (df_ND_m, aes(B_rate)) +geom_line(stat ="density", kernel = "epanechnikov")

# estimate the regression function 
#x = df_ND_m$Age
#y = df_ND_m$B_rate
#plot(x,y)
#h <- dpill(x, y)
#fit <- locpoly(x, y, bandwidth = h)
#lines(fit)

#SURVEILLANCE METRICS
df = read.csv("~/Desktop/STAT_project/surveil.csv")

# replace NaN with mean for that group
impute.mean = function(x) replace(x, is.na(x), mean(x, na.rm = TRUE))
df_m <- ddply(df, ~ Year, transform, value = impute.mean(value))

#subset the dataframe on conditions
df_ND_multi = subset(df_m, Metric=="multi")
df_ND_cxld = subset(df_m, Metric=="cxld")
df_ND_multi$row.names = NULL
df_ND_cxld$row.names = NULL


#kernel density plot
x = df_ND_multi$value
est = bkde (x, kernel="epanech")
plot(est, type="l")

x = df_ND_cxld$value
est = bkde (x, kernel="normal")
plot(est, type="l")
