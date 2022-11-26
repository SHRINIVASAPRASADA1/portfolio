var docs = document.getElementById("nav").style;
var litems = document.getElementById("lists").style;
var bar = document.getElementById("bar").style;
var closenav = document.getElementById("close").style;

function open_nav() {
  if ((docs.display = "block")) {
    // docs.display = "none";
    litems.display = "block";
    bar.display = "none";
    closenav.display = "block";
  }
}

function show_close() {
  closenav.display = "none";
  bar.display = "block";
  litems.display = "none";
}
