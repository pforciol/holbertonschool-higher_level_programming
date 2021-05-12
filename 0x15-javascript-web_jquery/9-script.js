const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

$(this).ready(function () {
  $.getJSON(url, function (data) {
    $('DIV#hello').text(data.hello);
  });
});
