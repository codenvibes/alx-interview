#!/usr/bin/node
/**
 * A script that fetches and prints the names of characters from a Star Wars film using the SWAPI.
 */
const util = require('util');
const request = util.promisify(require('request'));
const filmID = process.argv[2];

/**
 * Fetches and prints the names of characters from a specified Star Wars film.
 *
 * @param {string} filmId - The ID of the Star Wars film to fetch characters from.
 */
async function starwarsCharacters (filmId) {
  const endpoint = 'https://swapi-api.hbtn.io/api/films/' + filmId;
  let response = await (await request(endpoint)).body;
  response = JSON.parse(response);
  const characters = response.characters;

  for (let i = 0; i < characters.length; i++) {
    const urlCharacter = characters[i];
    let character = await (await request(urlCharacter)).body;
    character = JSON.parse(character);
    console.log(character.name);
  }
}

starwarsCharacters(filmID);
