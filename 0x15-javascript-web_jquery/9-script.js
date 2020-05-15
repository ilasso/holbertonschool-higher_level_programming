// Write a Javascript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr
// and displays the value of hello from that fetch in the HTML’s tag DIV#hello
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.get(url, function (data) {
  $('div#hello').text(data.hello);
}
);
