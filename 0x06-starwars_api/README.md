# Star Wars Characters
This script is used to retrieve and display all characters from a given Star Wars movie. The script uses the Star Wars API and the request module to make HTTP requests to the API.

## Prerequisites
* Node.js (version 10.14.x)
* npm package manager
* request module

## Installation
1. Clone the repository

git clone https://github.com/Chimmysmallz/alx-interview/0x06-starwars.api.git

2. Navigate to the project directory
cd star-wars-characters

3. install dependencies
npm install

## Usage
Run the script with the movie ID as the first positional argument. For example, to retrieve characters from "Return of the Jedi", use a movie ID of 3:

./characters.js 3

The script will display one character name per line in the same order as the "characters" list in the /films/ endpoint.
