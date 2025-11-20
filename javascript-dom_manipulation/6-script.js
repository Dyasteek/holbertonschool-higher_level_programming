document.addEventListener('DOMContentLoaded', function() {
    fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => response.json())
    .then(data => {
        document.getElementById('character').innerText = data.name;
    });
});