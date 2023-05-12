#!/usr/bin/node

const requests = require('requests');
const sys = require('sys');

const base_url = "https://swapi-api.alx-tools.com/api/films/";

// If a movie ID is provided as an argument, print its characters
if (sys.argv.length > 2) {
    const movie_id = sys.argv[2];
    const movie_url = base_url + movie_id + "/";
    requests.get(movie_url, (err, response, body) => {
        if (response.statusCode === 404) {
            console.log("Movie not found");
        } else {
            const movie_data = JSON.parse(body);
            const character_urls = movie_data["characters"];
            character_urls.forEach(character_url => {
                requests.get(character_url, (err, response, body) => {
                    const character_data = JSON.parse(body);
                    console.log(character_data["name"]);
                });
            });
        }
    });
}
// If no movie ID is provided, print the characters for all movies
else {
    for (let i = 1; i <= 7; i++) {
        const movie_url = base_url + i + "/";
        requests.get(movie_url, (err, response, body) => {
            if (response.statusCode === 404) {
                console.log(`Movie ID ${i} not found`);
            } else {
                const movie_data = JSON.parse(body);
                console.log(`Characters for ${movie_data['title']}:`);
                const character_urls = movie_data["characters"];
                character_urls.forEach(character_url => {
                    requests.get(character_url, (err, response, body) => {
                        const character_data = JSON.parse(body);
                        console.log(character_data["name"]);
                    });
                });
                console.log();
            }
        });
    }
}
