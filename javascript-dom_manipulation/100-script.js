document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('add_item').addEventListener('click', function() {
        var list = document.querySelector('.my_list');
        var new_li = document.createElement('li');
        new_li.innerText = 'Item';
        list.appendChild(new_li);
    });

    document.getElementById('remove_item').addEventListener('click', function() {
        var list = document.querySelector('.my_list');
        var last_li = list.lastElementChild;
        list.removeChild(last_li);
    });

    document.getElementById('clear_list').addEventListener('click', function() {
        var list = document.querySelector('.my_list');
        while (list.firstChild) {
            list.removeChild(list.firstChild);
        }
    });
});
