document.addEventListener('DOMContentLoaded', function () {
  const langCode = document.querySelector('#language_code');
  const btnTranslate = document.querySelector('#btn_translate');
  const hello = document.querySelector('#hello');

  btnTranslate.addEventListener('click', function () {
    const lang = langCode.value;
    fetch(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`)
      .then(response => response.json())
      .then(data => {
        hello.innerHTML = data.hello;
      });
  });
});
