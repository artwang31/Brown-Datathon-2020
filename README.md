# Brown-Datathon-2020

CHALLENGE:

Fidelity Investments is sponsoring a Corona Impact / Monitoring challenge in which participants look at travel data and make predictions on the potential impacts of the COVID-19 on tourist and traveler arrivals in the US. Participants are encouraged to consider both modeling and visualization projects.

BROWN DATATHON 2020
Team: Artemas Wang, Hariz Johnson, Manas Dresswala

PURPOSE: 
The goal of our data challenge was to look at travel data and make predictions on the potential impacts of the 
COVID-19 virus on tourist and traveler arrivals to the United States. 

METHODOLOGY: 
We began by processing traveler and tourism data into the United States (US) with data gathered from a 
variety of US governmental websites for the years 1996 - 2019. To more accurately predict potential impacts of COVID-19 
on US tourism, we modeled our assumptions on a previous pandemic that originated from Asia in 2003, 
Severe Acute Respiratory Syndrome (SARS). 

![International Arrivals into the US](https://github.com/artwang31/Brown-Datathon-2020/blob/master/flight_data.png)

We explored the impact this pandemic had on US tourism through visualizations 
that displayed the total foreign passport entries into the United States before and after the SARS outbreak.  
Additionally, two other factors were also considered in our prediction model. We considered the seasonality of travel 
and tourism and also accounted for the shifts of foreign currency exchange rates compared to the US dollar during this 
period of time. This allowed us to ascertain the nuances of variances among the three factors that could influence US tourism.

![Countries with Most Arrivals into US](https://github.com/artwang31/Brown-Datathon-2020/blob/master/top_countries_based_on_arrivals.png)

We then applied a regression model to predict the potential effects of COVID-19 on US tourism in 2020. 
The model was built on US tourism data from 1996-2003 considering the possible effects of SARS, the seasonality of travel, 
and foreign currency exchange rates to predict US tourism in 2004. The same model was applied on our COVID-19 prediction 
for US tourism in 2020. Because we are trying to predict the current COVID-19 pandemic on US tourism, 
it made sense for us to build this model on a previous pandemic, SARS, from 2003. 

![Arrivals by All Countries](https://github.com/artwang31/Brown-Datathon-2020/blob/master/arrivals_by_all_countries.png)

 RESULTS: 
 The visualization we produced indicated the number of Chinese nationals that visited the United States (US) 
 doubled in the years 2011-2019, however since 2017, the number of visitors have dipped significantly. 
 This reflected our findings on the amount of international flights into the US as the data indicated corresponding results. 
 Similarly, visitors to the US from other countries such as South Korea and the United Kingdom have also decreased, 
 particularly between 2018 and 2019. One possible explanation for this decrease in tourism could be the strengthening of 
 the US dollar. As our model regressed the volume of foreign visitors to historical foreign currency exchange rates, 
 the negative correlation indicates that this hypothesis could be the reason for the decrease in tourism. 
 
 ![Exchange Rates Compared to US Dollar](https://github.com/artwang31/Brown-Datathon-2020/blob/master/exchange_rates.png)
 
 Furthermore, when our model regressed on the effects of SARS on tourism in 2004, the model indicated no significant
 correlation. Thus, we infer that the fluctuations in US tourism is influenced less by the fear of contagious diseases but 
 more by a visitor’s purchasing powering parity. Also of note for such fluctuations of tourism could be the travel ban 
 enforced by many national governments of those who may have been in contact with COVID-19. 

  



