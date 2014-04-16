---

layout: post

title: Aarti[aj177] - Blog Post 2

description: blog post

---

#USDA Food Atlas 
###Motivation
The USDA assembled a [food environment atlas](http://www.ers.usda.gov/data-products/food-environment-atlas/go-to-the-atlas.aspx#.U0wd_dzirwI) to spur research on the determinants of food choices and diet quality, across the country. The EDAV for this project appear to be a work-in-progress. I chose to explore some correlations/interactions and possible causal relationships.

###Data Preparation
As a sample for this blog post, I decided to explore the effect of the following predictors on the health of the population. 


	1) (% change) in farmers' market availability

	2) (% change) in recreation facilities availability
	
	3) (% change) in fast-food restaurant availability
	
	4) (% change) in grocery store availability
	
	5) correlation between median income and obesity
	


I divided **population** into 3 categories: 

* <3m => less than 3 million 
* 3-10m => 3-10 million
* 10m+ => greater than 10 million

I divided **median income** into 4 categories:

* 30 => USD 30k to USD 40k
* 40 => USD 40k to USD 50k
* 50 => USD 50k to USD 60k
* 60 => greater than USD 60k



###Charts 
I represented the data as a combination of Lattice plots and rCharts. Specifically, in rCharts I used the interactive HighCharts and NVD3 and hosted the charts on gist.

**Lattice plots**: I grouped the data as a function of population size. 

**rCharts**: I grouped the data as a function of median income. 

#####**Graph1**
farmers' markets availability and obesity (%change), 2009-13 [grouped = pop size]
![Screenshot](/Users/Aarti/Desktop/blogpost2/lat_fmkt.png)


#####**Graph2**
rec facilities and obesity (%change), 2009-13 [grouped = pop size]
![Screenshot](/Users/Aarti/Desktop/blogpost2/lat_recFacil.png)

#####**Graph3**
fast-food restaurant availability (%change), 2007-11 and obesity 2010 [grouped = median income]

[rCharts HighCharts bubbleChart](http://rcharts.github.io/viewer/?10664997)

#####**Graph4**
grocery store availability (%change), 2007-11 and obesity 2010 [grouped = pop]

[rCharts NDV3 multibarChart](http://rcharts.github.io/viewer/?10743051)

#####**Graph5**
effect of median income on obesity with regression line + 95% confidence interval
![Screenshot](/Users/Aarti/Desktop/blogpost2/ggplot_l_reg.png)


###Insights
From Graph 5, I observe r value of ~ -0.7. This statistic implies a fairly strong inverse relation; specifically that obesity reduces with an increase in income level. This may suggest that people with higher income levels allocate expenditure to healthier food and/or health recreation. 

I did not glean sufficient correlation statistics in the interactions in Graphs 1-4. This could be owing to insufficient data points or perhaps the absence of a linear relation between food access and health factors, modeled here as obesity.

###R code

lattice charts
![Screenshot](/Users/Aarti/Desktop/blogpost2/lattice_code.png)

rCharts
![Screenshot](/Users/Aarti/Desktop/blogpost2/rCharts.png)

ggplot charts
![Screenshot](/Users/Aarti/Desktop/blogpost2/ggplot_chart.png)


