### example 1 ###########################################################
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors
# https://medium.com/@devkosal/scraping-data-with-beautifulsoup-and-selectorgadget-in-python-3-decf798e1a1e

from bs4 import BeautifulSoup
import requests

# Load the url into BeautifulSoup
url = "https://www.imdb.com/search/title?genres=drama&groups=top_250&sort=user_rating,desc"

html = requests.get(url)
soup = BeautifulSoup(html.text,'lxml')
# print(soup.prettify())

# Use our CSS Selector to extract a list of all the movies
movies = soup.select(".lister-item-header a")

movies_titles = [title.text for title in movies]
movies_links = ["http://imdb.com"+title["href"] for title in movies]

print(movies_titles)
print(movies_links)

### example 2 ###########################################################
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors
# https://develop--notesayushsharma.netlify.com/2018/09/a-guide-to-web-scraping-in-python-using-beautifulsoup

url = 'https://twitter.com/TheOnion'

html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
# print(soup.prettify())

# From the image above, we can see that the tweets are nested within a div with id=“timeline”, and the tweets themselves are within li tags with class=“stream-item”. 
all_tweets = []

timeline = soup.select('#timeline li.stream-item')

for tweet in timeline:

    tweet_id = tweet['data-item-id']
    tweet_text = tweet.select('p.tweet-text')[0].get_text()

    all_tweets.append({"id": tweet_id, "text": tweet_text})
# timeline
