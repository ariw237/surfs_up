# surfs_up
## Overview  
Using weather data stored in an SQLite database the climate_analysis jupyter notebook was used to query the database and generate temperature and precipitation statistics from various weather stations in the Oahu, Hawaii area. Having generated temperature and precipitation data over a one year period spanning 2016 to 2017, we are now interested in temperature data specifically for the months of June and December for all years and available stations with observations for comparison purposes.  
## Results  
* When viewed as a whole, there are more observations available for the month of June compared to December  
* Though largely inconsequential, mean temperatures for the month of June are slightly warmer but not significantly so
* There is very little variation between the warmest temperatuers observed when June and December are compared for all available stations but June is warmer  
* There is very little year to year variation in temperatures for the months of June and December

![june_hist](https://user-images.githubusercontent.com/60231630/143327171-8b331b84-fc63-4bd1-9b1f-4b690c03cfee.png)  



![december_hist](https://user-images.githubusercontent.com/60231630/143327191-ce2e26d4-a41c-43fc-a845-97ac2500b55e.png)  

## Summary  

Based on histograms of the data there appears to be slightly more spread in the June temperatures despite the average temperatures being warmer than those of December. Note the higher frequencies of more temperatures during the month of June. This is likely due to higher amounts of precipitation during the month of June.  Along these lines, additional queries to examine precipitation statistics (Measurement.prcp) for these two months is warranted.  Additionally since rainfall tends to be scattered, there is likely variation in precipitation amounts between the weather stations. Therefore, additional queries looking at stations with higher numbers of observations and comparison of precipitation amounts between weather stations (by grouping stats by available weather stations) may also be warranted. This is especially true of  those stations closest to the desired ideal location for opening the business in question.


