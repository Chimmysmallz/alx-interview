#!/usr/bin/node

import requests
import sys

movie_id = sys.argv[1]

# Fetch the movie data from the API
movie_url = f"https://swapi-api.alx-tools.com/api/films/3/"
response = requests.get(movie_url)
movie_data = response.json()

# Extract the character URLs from the movie data
character_urls = movie_data["characters"]

# Fetch the character data from the API and print their names
for character_url in character_urls:
    response = requests.get(character_url)
    character_data = response.json()
    print(character_data["name"])
