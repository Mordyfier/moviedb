# moviedb
## A simple webapp that turns the MovieLens small dataset into a movie catalog.

### This web app is an extension of my Summer 2021 CISC. 3140 full-stack web application project which can be found [here](https://github.com/Mordyfier/CISC3140/tree/master/Lab%204.3).

While I am proud of what I was able to accomplish with that (especially with a very strict 3-day deadline to learn most of the things I used practically from scratch), 
I see a lot of room for improvement. This repository will track all related progress. (The following milestones are planned in no particular order, though they are likely to follow the order in which they're listed.)

- [x] Getting rid of the admittedly barebones look that the placeholder images largely contributed to. Instead of displaying 'No image', the database
should include URLs of movie posters in each entry, allowing the views to display them. I think a simple way to obtain these could be scraping IMDb (given that their movie ids are readily available in the MovieLens dataset in [links.csv](https://github.com/Mordyfier/moviedb/blob/master/datasets/links.csv). 

#### Done! The movie posters have been scraped from each movie's respective IMDb page using [this](https://github.com/Mordyfier/moviedb/blob/master/scraper/moviedb_imdb_scraper.py) Python (BeautifulSoup) scraper.

- [x] Replacing the Postgres database with MongoDB. The goal for this change in database system is mainly for me to familiarize myself with the workings of a non-relational database, but there are also aspects of the BSON format that might fit better with what I want for this project. 

#### Done! The MovieLens dataset was reorganized and put together with another [Python script] (this would have probably been easier using Pandas, but core Python worked well enough). The resulting properly organized JSON file was easily read into a MongoDB database which is ready for the next step. 

- [ ] With a new database system in place, it would be great to implement a REST API that will serve data in JSON format to the frontend instead of the backend and the frontend being tightly-knit together the way they are now. This milestone will most likely come along with...

- [ ] Moving from Heroku to AWS. I mostly want to use this opportunity to explore the differences between the deployment processes as well as to get acquainted with AWS.

- [ ] React! It would be great to give this app a nice, modern, responsive look of a Single-Page App. With the REST API in place, using React for the frontend seems like a good bet given the framework's popularity.



