let slideIndex = 1;

document.addEventListener("DOMContentLoaded", function() {
  showSlides(slideIndex);
});

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("creature");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}

function saveAvatar() {
  // Get the selected avatar's data attribute (this is just an example)
  const selectedAnimal = document.querySelector('.creature.selected img').dataset.animal;

  if (!selectedAnimal) {
    alert('Please select an avatar.');
    return;
  }

  // Send the selected animal to the server
  fetch('save_avatar.php', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: new URLSearchParams({ animal: selectedAnimal }),
  })
    .then(response => response.json())
    .then(data => {
      if (data.status === 'success') {
        alert(`Avatar saved as ${data.animal}`);
      } else {
        alert('Failed to save avatar.');
      }
    })
    .catch(error => console.error('Error:', error));
}

// Example function to select an avatar (toggle selection for simplicity)
document.querySelectorAll('.creature').forEach(creature => {
  creature.addEventListener('click', () => {
    document.querySelectorAll('.creature').forEach(c => c.classList.remove('selected'));
    creature.classList.add('selected');
  });
});
/ ```````````````````````````````````````````````````````````````````````````````````````````````````` / 

var subjectObject = {
  "Coding": {
    "Beginner": ["Python", "Java", "C++"],
    "Intermediate":["Python", "Java", "C++"],
    "Advanced": ["Python", "Java", "C++"]
  },
  "Math": {
    "Beginner": ["Addition", "Subtraction", "Multiplication", "Division"],
    "Intermediate":["Addition", "Subtraction", "Multiplication", "Division"],
    "Advanced": ["Addition", "Subtraction", "Multiplication", "Division"]
  },
  "Fish" : {
    "Beginner": ["Habitat", "Food", "Species"],
    "Intermediate":["Habitat", "Food", "Species"],
    "Advanced": ["Habitat", "Food", "Species"]
  }
}
window.onload = function() {
  var subjectSel = document.getElementById("subject");
  var levelSel = document.getElementById("level");
  var categorySel = document.getElementById("category");
  for (var x in subjectObject) {
    subjectSel.options[subjectSel.options.length] = new Option(x, x);
  }
  subjectSel.onchange = function() {
    //empty Chapters- and Topics- dropdowns
    categorySel.length = 1;
    levelSel.length = 1;
    //display correct values
    for (var y in subjectObject[this.value]) {
      levelSel.options[levelSel.options.length] = new Option(y, y);
    }
  }
  levelSel.onchange = function() {
    //empty Chapters dropdown
    categorySel.length = 1;
    //display correct values
    var z = subjectObject[subjectSel.value][this.value];
    for (var i = 0; i < z.length; i++) {
      categorySel.options[categorySel.options.length] = new Option(z[i], z[i]);
    }
  }
}

