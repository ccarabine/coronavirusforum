const messages = document.getElementById('msg');
const alert = new bootstrap.Alert(messages);

if (messages)
  setTimeout(function () {
    alert.close();
  }, 2500);



// vote trigger
const upVote = document.getElementById('upVote')
const downVote = document.getElementById('downVote')
const upThumb = document.getElementById('upThumb')
const downThumb = document.getElementById('downThumb')
const voteForm = document.getElementById('voteForm')
const postId = document.getElementById('thumbs').getAttribute('data-value');

if (upVote) {
  console.log("here")
  upThumb.addEventListener('click', (e) => {
    e.preventDefault()
    if (upThumb.classList.contains('active')) {
      upVote = false
      upThumb.classList.remove('active')
      voteForm.submit()
    } else {
      upVote.checked = true
      upThumb.classList.add('active')
      voteForm.submit()
    }
  })

  downThumb.addEventListener('click', (e) => {
    e.preventDefault()
    downVote.checked = true
    downThumb.classList.add('active')
    voteForm.submit()
  })
}



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