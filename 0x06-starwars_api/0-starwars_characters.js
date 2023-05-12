#!/usr/bin/node

import requests
import sys

base_url = "https://swapi-api.alx-tools.com/api/"

# If a movie ID is provided as an argument, print its characters
if len(sys.argv) > 1:
    movie_id = sys.argv[1]
    movie_url = base_url + movie_id + "/"
    try:
        response = requests.get(movie_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    else:
        movie_data = response.json()
        character_urls = movie_data["characters"]
        for character_url in character_urls:
            try:
                response = requests.get(character_url)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
            else:
                character_data = response.json()
                print(character_data["name"])
# If no movie ID is provided, print the characters for all movies
else:
    for i in range(1, 8):
        movie_url = base_url + str(i) + "/"
        try:
            response = requests.get(movie_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        else:
            movie_data = response.json()
            print(f"Characters for {movie_data['title']}:")
            character_urls = movie_data["characters"]
            for character_url in character_urls:
                try:
                    response = requests.get(character_url)
                    response.raise_for_status()
                except requests.exceptions.RequestException as e:
                    print(f"An error occurred: {e}")
                else:
                    character_data = response.json()
                    print(character_data["name"])
            print()
