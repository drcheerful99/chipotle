
library('TTR')
library('quantmod')

#pull stock data
df_cmg <- getSymbols('CMG',src='yahoo',auto.assign=FALSE)


#get class
class(df_cmg)

#number of rows
nrow(df_cmg)

#last rows
tail(df_cmg,2)



#cmg charts

plot(df_cmg$CMG.Close,main = 'Intel Stock Price')
chart_Series(df_cmg$CMG.Close,name="Intel Stock Price")
chartSeries(df_cmg,CMG="Intel Stock Price",theme = 'white')



