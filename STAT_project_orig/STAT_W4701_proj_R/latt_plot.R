library(lattice)
library(plyr)
library(ggplot2)

#SUCCESS METRICS
# num of cycles
df = read.csv("~/Desktop/STAT_project/cyc.csv")

#subset the dataframe on conditions
df_ND = subset(df, Donor==0)
df_ND$row.names = NULL

df_D = subset(df, Donor==1)
df_D$row.names = NULL


#scatter plot [lattice]
cyc_ND_age = xyplot (cyc_num ~ Age | factor(Year), df_ND, groups = Egg_Type, plot.points = FALSE, auto.key = TRUE)
cyc_ND_age = update(cyc_ND_age, main="Number of cycles[Non Donor] by Egg Type", ylab="Num of cycles")
cyc_ND_age = update(cyc_ND_age, type = c("p", "l"))

#scatter plot [ggplot]
cyc_D_age = ggplot(df_D, aes(Year, cyc_num)) + geom_smooth(method = "lm") + geom_point(aes(colour=Egg_Type)) + facet_grid(~Egg_Type) 
cyc_D_age + ylab("Num of cycles")


# singleton live births by Age group [ggplot]
lB_ND_age = ggplot(df_ND, aes(Age, singl_b)) + geom_smooth(method = "lm") + geom_point(aes(colour=Egg_Type)) + facet_grid(~Year) 
lB_ND_age + ylab("Num of singleton children")

lB_ND_age = ggplot(df_ND, aes(Age, singl_b)) + geom_violin(aes(fill = Egg_Type))+ facet_grid(~Year) 
lB_ND_age + ylab("Num of singleton children")


#singleton live birth rate
df = read.csv("~/Desktop/STAT_project/sLB.csv")

#subset the dataframe on conditions
df_ND = subset(df, Donor ==0)
df_ND$row.names = NULL

#kernel density plot
#sLB = densityplot (~ B_rate | factor(Donor), df, groups = Egg_Type, plot.points = FALSE, auto.key = TRUE)

#scatter plot
s_ND_age = xyplot (B_rate~Age | factor(Year), df_ND, groups = Egg_Type, plot.points = FALSE, auto.key = TRUE)
s_ND_age = update(s_ND_age, main="Singleton Live Birth rate[Non Donor] by Egg Type", ylab="Birth rate")
s_ND_age = update(s_ND_age, type = c("p", "l"))



#SURVEILLANCE METRICS
df = read.csv("~/Desktop/STAT_project/surveil.csv")

# replace NaN with mean for that group
impute.mean = function(x) replace(x, is.na(x), mean(x, na.rm = TRUE))
df_m <- ddply(df, ~ Year, transform, value = impute.mean(value))

# surveillance metric by Year, by Age
surveil_ND_age = xyplot (value~Age | factor(Year), df_m, groups = Metric, plot.points = FALSE, auto.key = TRUE)
surveil_ND_age = update(mul_ND_age, main="Surveillance metric for fresh Non Donor eggs", ylab="Birth rate")
surveil_ND_age = update(mul_ND_age, type = c("p", "l"))

