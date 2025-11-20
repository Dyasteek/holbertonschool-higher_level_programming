document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('add_item').addEventListener('click', function() {
        var ul = document.querySelector('ul');
        var li = document.createElement('li');
        li.innerText = 'Item';
        ul.appendChild(li);
    });
});
