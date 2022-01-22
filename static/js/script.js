const messages = document.getElementById('msg');
const alert = new bootstrap.Alert(messages);

if (messages)
  setTimeout(function () {
    alert.close();
  }, 2500);

/*  Code taken from https://www.youtube.com/watch?v=onZ69P9wS2o */
/*
$(document).ready(function () {
  $('.thumbaction').click(function (e) {
    e.preventDefault();
    var postid = document.getElementById('votes').getAttribute('data-value');
    var button = $(this).attr("value");
    $.ajax({
      type: 'POST',
      url: '{% url "accounts:votes" %}',
      data: {
        postid: postid,
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        action: 'votes',
        button: button,
      },
      success: function (json) {
        if (json.length < 1 || json == undefined) {
          //empty
        }
        document.getElementById("up").innerHTML = json['upvote']
        document.getElementById("down").innerHTML = json['downvote']
        $("svg").removeClass("thumb-active");

        if (json['remove'] == 'none') {
          $("#" + button).removeClass("thumb-active");
        } else {
          $("#" + button).addClass("thumb-active");
        }
      },
      error: function (xhr, errmsg, err) {}
    });
  });
});*/