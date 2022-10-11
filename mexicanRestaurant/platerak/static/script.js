$(document).ready(function () {
  $("#hide").click(function () {
    $("p").toggle();
  });
  $("#fade").click(function () {
    $("p").fadeToggle();
  });
  $("#slide").click(function () {
    $("p").slideToggle();
  });
  $("#btn1").click(function () {
    alert("Text: " + $("#test").text());
  });
  $("#btn2").click(function () {
    alert("HTML: " + $("#test").html());
  });
  $("#btn3").click(function () {
    alert("Value: " + $("#box").val());
  });
  $("#btn4").click(function () {
    alert($("#w3s").attr("href"));
  });

  $(".needs-validation").on("submit", function (e) {
    if (!this.checkValidity()) {
      e.preventDefault();
      e.stopPropagation();
    }
    $(this).addClass("was-validated");
  });

  $("p").each(function (i) {
    if (i % 2 == 0) {
      $(this).css("background-color", "#eee");
    } else {
      $(this).css("background-color", "#ccc");
    }
  });
  $("input:submit").click(function () {
    $("#bat").append("<p>Otro mas</p>");
  });

  $("div").each(function(i){
    elemento = $(this);
    if(elemento.html() == "white")
    return true;
    if(elemento.html() == "nada")
    return false;
    elemento.css("color", elemento.html());
    });
});