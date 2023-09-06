from bs4 import BeautifulSoup
import requests
import random

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_webpage = response.text

soup = BeautifulSoup(movie_webpage, "html.parser")

title_tag = soup.find_all(name="h3")

movies = []
for tag in title_tag:
    titles = tag.getText().replace(":", ")")
    movies.append(titles)

reversed_list = []
for i in reversed(movies):
    reversed_list.append(i)

with open("movies.txt", mode="w") as file:
    for movie in reversed_list:
        file.write(f"{movie}\n")

random_index = random.randint(0, len(reversed_list))
random_movie = reversed_list[random_index]
print(f"Du kan se film nr. {random_movie}")
