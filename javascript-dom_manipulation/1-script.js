document.addEventListener('DOMContentLoaded', function(){
    const red_header = document.querySelector('#red_header');
    const header = document.querySelector('header');

    red_header.addEventListener('click', function(){
        header.style.color = '#FF0000';
    });
});
