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

$(document).ready(function() {
    // Update hunger level immediately upon page load and every 12 hours
    function updateHungerLevel() {
        $.ajax({
            url: 'https://hunger-tracker-770213444308.us-central1.run.app/manage_hunger',
            method: 'GET',
            dataType: 'json',
            success: function(data) {
                const hungerLevel = data.hunger_level;
                $('#hungerLevel').text(hungerLevel);
            },
            error: function(jqXHR, textStatus, errorThrown) {
                console.error('There was a problem with the AJAX operation:', textStatus, errorThrown);
            }
        });
    }

    updateHungerLevel();
    setInterval(updateHungerLevel, 43200000); // 12 hours in milliseconds

    // Feed Function
    function feed() {
        $.ajax({
            url: 'https://hunger-tracker-770213444308.us-central1.run.app/manage_hunger',
            method: 'POST',
            success: function(data) {
                console.log('Feed success:', data);

                // Update hunger level immediately after feeding
                if (data.hunger_level !== undefined) {
                    $('#hungerLevel').text(data.hunger_level);
                }
            },
            error: function(jqXHR, textStatus, errorThrown) {
                console.error('Feed error:', textStatus, errorThrown);
            }
        });
    }

    // Starve Function
    function starve() {
        $.ajax({
            url: 'https://hunger-tracker-770213444308.us-central1.run.app/manage_hunger',
            method: 'DELETE',
            success: function(data) {
                console.log('Starve success:', data);

                // Update hunger level immediately after starving
                if (data.hunger_level !== undefined) {
                    $('#hungerLevel').text(data.hunger_level);
                }
            },
            error: function(jqXHR, textStatus, errorThrown) {
                console.error('Starve error:', textStatus, errorThrown);
            }
        });
    }

    // Assign button click events
    $('#feed').on('click', feed);
    $('#starve').on('click', starve);
});



// Function to save the current avatar
function saveAvatar() {
  // Get the animal name based on the currently displayed slide
  const creatures = ['crab', 'frog', 'cat', 'dog']; // List should match the order of your slides
  const selectedAnimal = creatures[slideIndex - 1];

  if (!selectedAnimal) {
    alert('Could not find the selected animal.');
    return;
  }

  // Send a POST request to the PHP script to save the selected animal
  fetch('../save_avatar.php', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: new URLSearchParams({ animal: selectedAnimal }),
  })
  .then(response => response.json())
  .then(data => {
    if (data.status === 'success') {
      alert(`Saved animal to be: ${data.animal}`);
    } else {
      alert(`Failed to save animal: ${data.message}`);
    }
  })
  .catch(error => {
    console.error('Error:', error);
    alert('An error occurred while saving the animal.');
  });
}
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