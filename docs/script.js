function toggleMode() {
    var body = document.body;
    var header = document.querySelector('header');
    var footer = document.querySelector('footer');

    // Toggle dark mode class on body
    body.classList.toggle("dark-mode");

    // Toggle dark mode class on header
    header.classList.toggle("dark-mode");

    // Toggle dark mode class on footer
    footer.classList.toggle("dark-mode");
}

function filterContent() {
    var input = document.getElementById('search-input');
    var filter = input.value.toUpperCase();
    var sections = document.getElementsByTagName('section');

    for (var i = 0; i < sections.length; i++) {
        var h2 = sections[i].getElementsByTagName('h2')[0];
        if (h2) {
            var textValue = h2.textContent || h2.innerText;
            if (textValue.toUpperCase().indexOf(filter) > -1) {
                sections[i].style.display = "";
            } else {
                sections[i].style.display = "none";
            }
        }
    }
}
