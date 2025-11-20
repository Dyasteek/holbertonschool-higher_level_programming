document.addEventListener('DOMContentLoaded', function() {
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
        var hello = document.getElementById('hello');
        hello.innerText = data.hello;
    });
});
