#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2] || '';

function requestPromise(url) {
    return new Promise((resolve, reject) => {
      request(url, (err, response, body) => {
        if (err) {
          reject(err); // Reject the promise if an error occurs
        } else if (response.statusCode === 200) {
          resolve(body); // Resolve the promise with the response body
        } else {
          reject(new Error(`Failed with status code: ${response.statusCode}`));
        }
      });
    });
  }
  
  // Main function to fetch characters synchronously
  async function fetchCharacters() {
    try {
      // Fetch movie details
      const movieResponse = await requestPromise(`https://swapi-api.alx-tools.com/api/films/${movieID}`);
      const movie = JSON.parse(movieResponse);
  
      const characters = movie.characters;
  
      // Process each character sequentially
      for (const character of characters) {
        const charResponse = await requestPromise(character);
        const characterData = JSON.parse(charResponse);
        console.log(characterData.name);
      }
    } catch (error) {
      console.error('Error:', error);
    }
  }
  
  fetchCharacters();