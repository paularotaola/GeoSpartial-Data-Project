# GeoSpartial-Data-Project

![alt imagen](Input/Geospatial.jpg)
## Overview

The goal of this project is to find the best location for a new office by cleaning and filtering a database of company locations.


## Context. 


Our CEO is planning to expand to a new country. He has chosen Singapore as it is considered a great country for starting a tech company.

We have asked all the employees to show their preferences on where to place the new office. These were the results:

- Designers like to go to design talks and share knowledge. There must be some nearby companies that also do design.
- 30% of the company have at least 1 child.
- Developers like to be near successful tech startups that have raised at least 1 Million dollars.
- Executives like Starbucks A LOT. Ensure there's a starbucks not to far.
- Account managers need to travel a lot
- All people in the company have between 25 and 40 years, give them some place to go to party.
- The CEO is Vegan
- If you want to make the maintenance guy happy, a basketball stadium must be around 10 Km.
- The office dog "Pepe" needs a hairdresser every month. Ensure there's one not too far away.

The goal is to place the **new office** in the best place for the company to grow. 

### Analysis schema

Based on the employees preferences the scoring will be based on the relevance of the prerequisites, as we consider some more important than others.

- Very important: Will be counted as double (x2)
- Medium importance: Will count as one (x1)
- Low importance: will be counted as half (x0.5)

Additionally, each location will be weighted based on the number of people affected by the decision. The preferred location will be the one with a highest score.

### Result

The location with the highest score will be visualized in a map with the spots located nearby in order to be presented to the CEO.

​
## Links & Resources
​
- [https://developers-dot-devsite-v2-prod.appspot.com/maps/documentation/javascript/examples/geocoding-reverse]
- [https://docs.mongodb.com/manual/geospatial-queries/]
- [https://developers.google.com/maps/documentation/geocoding/intro]
- [https://developers.google.com/maps/documentation/geocoding/start]
- [https://data.crunchbase.com/docs]
- [https://developers.google.com/places/web-service/search]
- [https://www.youtube.com/watch?v=PtV-ZnwCjT0]
- [https://developer.foursquare.com/]
- [https://cloud.google.com/maps-platform/places/]
- [https://www.meetup.com/meetup_api/]