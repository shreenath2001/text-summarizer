function eraseText() {
    document.getElementById("clear-text").value = "";
}

function eraseUrl() {
    document.getElementById("clear-url").value = "";
}

var classify = document.getElementById('classify');
var image = document.querySelector('#output');

var loadFile = function(event) {
    var image = document.getElementById('output');
    image.style.display = "block";
    image.style.margin = "auto";
    image.src = URL.createObjectURL(event.target.files[0]);
    classify.style.display = "block";
};

disp = () => {
    image.style.display = "none";
    classify.style.display = "none";
}