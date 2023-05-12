#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

// Fetch the movie data from the API
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
request.get(movieUrl, (error, response, body) => {
  if (error) {
    console.error(`Error fetching movie data: ${error}`);
    return;
  }

  const movieData = JSON.parse(body);

  // Extract the character URLs from the movie data
  const characterUrls = movieData["characters"];

  // Fetch the character data from the API and print their names
  characterUrls.forEach((characterUrl) => {
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        console.error(`Error fetching character data: ${error}`);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData["name"]);
    });
  });
});
