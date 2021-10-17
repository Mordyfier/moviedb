from bs4 import BeautifulSoup
import requests
import csv
url = "https://www.imdb.com/title/" 
# the class of div containing the poster element
poster_class = "ipc-media ipc-media--poster-27x40 ipc-image-media-ratio--poster-27x40 ipc-media--baseAlt ipc-media--poster-l ipc-poster__poster-image ipc-media__img"

def poster_scraper(id):
  text = requests.get(url + id).text # gets the movie page as html doc
  soup = BeautifulSoup(text, 'html5lib') # parses the html
  div = soup.find(class_= poster_class) # finds the right div tag
  if div == None: # in case the movie page is gone for some reason
      return ""
  img_url = div.find('img').get('src') # extracts the image url
  return img_url

# using the links.csv file from the MovieLens dataset, a dictionary is produced that associates movielens_id with imdb_id
# this association will be essential for later merging of the .csv files in the broader data cleaning script
def main():  
  with open('links.csv', 'r', newline='') as links:
    reader = csv.reader(links)
    next(reader)
    links = dict()
    for row in reader:
        movielens_id = row[0]
        imdb_id = row[1]
        while 7 - len(imdb_id) > 0: # fixing imdb_id length (leading zeroes are omitted in the dataset)
            imdb_id = '0' + imdb_id
        imdb_id = 'tt' + imdb_id 
        links[movielens_id] = imdb_id

  # once the imdb_ids are ready, scraping and writing into a file can commence:
  with open('poster_links.csv', 'w', newline='') as poster_links:
    writer = csv.writer(poster_links)
    writer.writerow(['movieId', 'imdbId', 'poster_link'])
    for id in links.items():
      row = [id[0], id[1], poster_scraper(id[1])] # movielens_id, imdb_id, poster_link to be printed to .csv 
      writer.writerow(row)

##### Sample Input #####
# sample = ['tt0110912','tt0133093', 'tt0137523', 'tt0120737', 'tt0119217']
# for id in sample:
#   print(poster_scraper(id))
##### Sample Output #####
# https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_QL75_UY281_CR2,0,190,281_.jpg
# https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_QL75_UX190_CR0,2,190,281_.jpg
# https://m.media-amazon.com/images/M/MV5BMmEzNTkxYjQtZTc0MC00YTVjLTg5ZTEtZWMwOWVlYzY0NWIwXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_QL75_UX190_CR0,2,190,281_.jpg
# https://m.media-amazon.com/images/M/MV5BN2EyZjM3NzUtNWUzMi00MTgxLWI0NTctMzY4M2VlOTdjZWRiXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_QL75_UX190_CR0,0,190,281_.jpg
# https://m.media-amazon.com/images/M/MV5BOTI0MzcxMTYtZDVkMy00NjY1LTgyMTYtZmUxN2M3NmQ2NWJhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_QL75_UX190_CR0,4,190,281_.jpg


if __name__ == "__main__":
  main()

