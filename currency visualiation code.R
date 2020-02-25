library(tidyverse)
library(ggplot2)
library(data.table)

#data_currency <- "currency_exchange_rates_02-01-1995_-_02-05-2018.csv"

data_currency <-fread(paste0("currency_exchange_rates_02-01-1995_-_02-05-2018.csv"), header = T, stringsAsFactors = F, data.table = T)
data_currency <- na.omit(data_currency)
data_scaled <- data_currency
date <- data.frame(data_currency$Date)
#data_currency$Euro <- (data_currency$Euro - mean(data_currency$Euro)) / sqrt(var(data_currency$Euro))
#data_currency$`Chinese Yuan` <- (data_currency$`Chinese Yuan` - mean(data_currency$`Chinese Yuan`)) / sqrt(var(data_currency$`Chinese Yuan`))

data_scaled <- data.frame(scale(data_scaled[ , 2:52]))
final <- bind_cols(date, data_scaled)
str(data_scaled)

ggplot(final, aes(x = final$data_currency.Date)) + 
  geom_line(aes(y = data_scaled$Chinese.Yuan, group = 1), color = "red") +
  geom_line(aes(y = data_scaled$U.K..Pound.Sterling, group = 1), color = "green") +
  geom_line(aes(y = data_scaled$Euro, group = 1), color = "blue") +
  geom_line(aes(y = data_scaled$Japanese.Yen, group = 1), color = "orange") +
  geom_line(aes(y = data_scaled$Indian.Rupee, group = 1), color = "green")

write.csv(final, file = 'data_scaled_final.csv')
