const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

$.getJSON(url, function (data) {
  $.each(data.results, function (i, movie) {
    $('UL#list_movies').append('<li>' + movie.title + '</li>');
  });
});
