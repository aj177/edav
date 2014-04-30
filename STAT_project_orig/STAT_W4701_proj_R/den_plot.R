library (reshape2)
library(ggplot2)
library(KernSmooth)

# dataframe preparation
df = read.csv("~/Desktop/STAT_project/STAT_W4701_proj_py/nat_sum_cyc")
df$Year[df$Year == "0"] <- "2011"

df_mod = melt(df, id =c("Year"))
df_mod_fsh = df_mod[c(1:12),]

map <- setNames(c("35","37","40", "42","44", "46", "35","37","40", "42","44", "46"), df_mod_fsh$variable)
df_mod_fsh$variable <- map[unlist(df_mod_fsh$variable)]
df_mod_fsh$variable <- as.numeric(df_mod_fsh$variable)
df_mod_fsh$Year <- as.numeric(df_mod_fsh$Year)

x = df_mod_fsh$variable

# stat_function can be used in ggplot2
p1 = ggplot(df_mod_fsh, aes(x, colour="Year")) + geom_line(stat="density")


p1#p1 + geom_smooth(method = "ksmooth")

# ksmooth
#p2 = ksmooth(df_mod_fsh$variable, df_mod_fsh$value, kernel="normal", bandwidth=1.5)
#p3 = plot(df_mod_fsh$variable, df_mod_fsh$value); lines(p2)

#locpoly
#fit = locpoly(df_mod_fsh$variable, bandwidth=0.5)
#lines(fit)




