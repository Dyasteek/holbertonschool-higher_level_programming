document.addEventListener('DOMContentLoaded', function() {
    fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
        const movies = data.results;
        const list = document.getElementById('list_movies');
        movies.forEach(movie => {
            const li = document.createElement('li');
            li.innerText = movie.title;
            list.appendChild(li);
        });
    });
});
