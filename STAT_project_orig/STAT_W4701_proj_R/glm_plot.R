library (reshape2)
library(ggplot2)
library(glm)
library(fitdistrplus)

# dataframe preparation
df = read.csv("~/Desktop/STAT_project/glm_temp.csv")


df_mod = melt(df, id =c("Year"))
df_mod_fsh = df_mod[c(1:24),]

x = df_mod_fsh$value
fitg = fitdistr(x, "gamma")
plot(fitg)
