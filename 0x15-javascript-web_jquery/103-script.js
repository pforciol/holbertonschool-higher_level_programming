const url = 'https://fourtonfish.com/hellosalut/?lang=';

$(this).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    $.getJSON(url + $('INPUT#language_code').val(), function (data) {
      $('DIV#hello').text(data.hello);
    });
  });

  $('INPUT#language_code').keyup(function (e) {
    if (e.keyCode === 13) {
      $.getJSON(url + $(this).val(), function (data) {
        $('DIV#hello').text(data.hello);
      });
    }
  });
});
