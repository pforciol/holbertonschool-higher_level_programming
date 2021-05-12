const url = 'https://fourtonfish.com/hellosalut/?lang=';

$(this).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    $.getJSON(url + $('INPUT#language_code').val(), function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
