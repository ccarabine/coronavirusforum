const messages = document.getElementById('msg');
const alert = new bootstrap.Alert(messages);

if (messages)
setTimeout(function () {
  alert.close();
}, 2500);