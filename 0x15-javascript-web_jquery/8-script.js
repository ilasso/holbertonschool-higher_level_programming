// script that fetches and lists all movies title by using this 
// URL: https://swapi-api.hbtn.io/api/films/?format=json
let url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, function (data) {
  let films = data.results;
  for (let film of films) {
    $('ul#list_movies').append(`<li>${film.title}</li>`);
  }
});