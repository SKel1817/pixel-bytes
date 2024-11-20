var subjectObject = {
    "Coding": {
        "Beginner": ["Python", "Java", "C++"],
        "Intermediate": ["Python", "Java", "C++"],
        "Advanced": ["Python", "Java", "C++"]
    },
    "Math": {
        "Beginner": ["Addition", "Subtraction", "Multiplication", "Division"],
        "Intermediate": ["Addition", "Subtraction", "Multiplication", "Division"],
        "Advanced": ["Addition", "Subtraction", "Multiplication", "Division"]
    },
    "Fish": {
        "Beginner": ["Habitat", "Food", "Species"],
        "Intermediate": ["Habitat", "Food", "Species"],
        "Advanced": ["Habitat", "Food", "Species"]
    }
};

window.onload = function() {
    var subjectSel = document.getElementById("subject");
    var levelSel = document.getElementById("level");
    var categorySel = document.getElementById("category");

    for (var x in subjectObject) {
        subjectSel.options[subjectSel.options.length] = new Option(x, x);
    }

    subjectSel.onchange = function() {
        // Empty Level and Category dropdowns
        levelSel.length = 1;
        categorySel.length = 1;
        // Display correct values
        for (var y in subjectObject[this.value]) {
            levelSel.options[levelSel.options.length] = new Option(y, y);
        }
    };

    levelSel.onchange = function() {
        // Empty Category dropdown
        categorySel.length = 1;
        // Display correct values
        var z = subjectObject[subjectSel.value][this.value];
        for (var i = 0; i < z.length; i++) {
            categorySel.options[categorySel.options.length] = new Option(z[i], z[i]);
        }
    };
};