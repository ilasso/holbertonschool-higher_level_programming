// script that fetches and lists all movies title by using this
// URL: https://swapi-api.hbtn.io/api/films/?format=json
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, function (data) {
  const films = data.results;
  for (const film of films) {
    $('ul#list_movies').append(`<li>${film.title}</li>`);
  }
});
