# moviedb
A simple webapp that turns a MovieLens dataset into a movie catalogue.

This web app is an extension of my Summer 2021 CISC. 3140 full-stack web application project which can be found [here](https://github.com/Mordyfier/CISC3140/tree/master/Lab%204.3).

While I am proud of what I was able to accomplish with that (especially with a very strict 3-day deadline to learn most of the things I used practically from scratch), 
I see a lot of room for improvement. This repository will track all related progress.

* First item on the agenda was getting rid of the admittedly barebones look that the placeholder images largely contributed to. Instead of displaying 'No image', the database
now includes URLs of movie posters in each entry, allowing the views to display them. The movie posters have been [scraped] from each movie's respective movie page using Python (BeautifulSoup).
