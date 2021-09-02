# Honolulu, Here I Come!

I have decided to take a trip to Honolulu, Hawaii. I thought that decided where to go would be the hard part, but I still have so many questions left to answer. 

When should I go? What is the weather like? What do I wear?

To answer these questions, I looked at temperature and precipitation records from nine different weather stations around Oahu. 

First, I needed to decide when to go. A t-test comparing temperatures between different months showed no statistically significant temperature changes through out the year. However, I really like rain, so I want to go when there is the most rain. I created a bar chart to see which months have the highest average precipitation, and found that to be March and December, though December was slightly higher, so I set my trip for December 12 - December 19. I then looked at the average temperatures for those dates, and found them to be in the low to mid 60's. Now I know what to wear! 

![alt text](https://github.com/KStrange89/sqlalchemy-challenge/blob/main/images/month_prcp.png)

![alt text](https://github.com/KStrange89/sqlalchemy-challenge/blob/main/images/trip_prcp.png)

I used SQLAlchemy, Pandas, and Matplotlib to complete my analysis. Once my analysis was complete, I designed a Flask API with information regarding the climate. This API returns a JSON.