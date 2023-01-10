from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2"

response = requests.get(URL)
empire_web = response.text

soup = BeautifulSoup(empire_web, "html.parser")

titles = soup.find_all(name="h3", class_="jsx-4245974604")

movie_titles = [title.getText() for title in titles]
movies = movie_titles[::-1] #cambiar el orden de atrás para adelante de la lista

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
