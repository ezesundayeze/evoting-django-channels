const party = document.getElementById("party");
var info = document.getElementById("info");

const form = document.getElementById("vote_form");

form.addEventListener("submit", function(e) {
  e.preventDefault();
  $.ajax({
    type: "post",
    url: "home/",
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

document.addEventListener("DOMContentLoaded", function() {
  const webSocketBridge = new ChannelSplitterNode.WebSocketBridge();
  const nl = document.querySelector("#votes");
  webSocketBridge.connect("/home/");
  webSocketBridge.listen(function(action, stream) {
    console.log("Response:", action);
    if (action.event === "new vote") {
      const li = document.createElement("li");
      li.innerHTML = `new vote from ${action.name}`;
    }
  });
});
