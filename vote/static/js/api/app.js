const party = document.getElementById("party");
var info = document.getElementById("info");

const form = document.getElementById("vote_form");

form.addEventListener("click", function(e) {
  $.ajax({
    type: "post",
    url: "home",
    data: {
      party: party.value,
      csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
    },
    beforeSend: function(xhr) {
      info.innerText = "Sending vote";
    },
    success: function() {
      info.innerText = "Congratulations, you've voted successfully! Cheers.";
    }
  });
});
