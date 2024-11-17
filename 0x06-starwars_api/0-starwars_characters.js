#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2] || '';

request(`https://swapi-api.alx-tools.com/api/films/${movieID}`, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
  } else if (response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, (err, response, body) => {
        if (err) {
          console.error('Error:', err);
        } else if (response.statusCode === 200) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
