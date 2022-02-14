// Message variables
const messages = document.getElementById('msg');
const alert = new bootstrap.Alert(messages);

// vote variables
const upVote = document.getElementById('upVote');
const downVote = document.getElementById('downVote');
const voteForm = document.getElementById('voteForm');
const upThumb = document.getElementById('upThumb');
const downThumb = document.getElementById('downThumb');

if (messages)
  setTimeout(function () {
    alert.close();
  }, 2500);

if (upVote) {
  upThumb.addEventListener('click', (e) => {
    e.preventDefault();
    upVote.checked = true;
    voteForm.submit();
  });

  downThumb.addEventListener('click', (e) => {
    e.preventDefault();
    downVote.checked = true;
    voteForm.submit();
  });
}