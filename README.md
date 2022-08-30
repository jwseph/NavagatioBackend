# WanderLag
 Wanderlagging behind

Wanderlag is a Travel Iternary and planning webapp which serves as a "proof of concept" product for the much better and cleaner RYOKEI app. Literally just me building something with react and flask.

Design Idea:
User enters city name -> city name is processed and nearby attractions/eateries/hotels are scraped and returned as an array.

Returned array is used to obtain google places API data on each attraction. Data is displayed on the frontend by being sent from the flask API.

Trip/User data is stored in SQLite database