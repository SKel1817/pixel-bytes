<?php
require_once('./connection.php');
//write a query to get curr_avatar from most recent row
$projectId = 'nielson-4160-f24';
$query = "SELECT curr_avatar FROM `pixelbytes.user_data` ORDER BY DATE DESC LIMIT 1";
$returned_arr = selectTable($projectId, $query);
$curr_avatar = $returned_arr[0]['curr_avatar'];
?>


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>PixelBytes</title>
    <!--Link to favicon-->
    <link rel="PixelBytes Icon" href="./media/gear.png" type="image/x-icon" />
    <link rel="stylesheet" href="./css/style.css" />
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="./js/script.js"></script>
  </head>
  <script>
        document.addEventListener('DOMContentLoaded', function() {
            const urlParams = new URLSearchParams(window.location.search);
            const feedButton = document.getElementById('feed');
            if (urlParams.has('feed_enabled') && urlParams.get('feed_enabled') === 'true') {
                if (feedButton) {
                    feedButton.disabled = false;
                    feedButton.style.filter = 'none';
                    <?php
                    // write a query to insert question_answered in user_data
                    $projectId = 'nielson-4160-f24';
                    // date variable
                    $date = date("Y-m-d");
                    $query = "INSERT INTO `pixelbytes.user_data` (Date, question_answered) VALUES ($date, true)";
                    insertTable($projectId, $query);
                    ?>
                }
            }

            if (feedButton) {
                feedButton.addEventListener('click', function() {
                    feedButton.disabled = true;
                    feedButton.style.filter = 'grayscale(100%)';
                    // Optionally, you can add code here to handle the feed action
                });
            }
        });
  </script>
<header>
    <nav class="nav">
        <a href="./index.php"><img src="./media/gear.png" alt="PixelBytes Logo" height="25px" /></a>
        <div class="logo">PixelBytes</div>
        <div class="food">
            <img src="./media/gear.png" alt="PixelBytes Logo" height="20px" />
            <span id="hungerLevel"></span>
        </div>
        <ul>
          <li><a href="./index.php">Home</a></li>
          <li><a href="./html/learn.php">Learn</a></li>
          <li><a href="./html/lessons.php">Lessons</a></li>
          <!-- <li><a href="./html/login.php">Login</a></li> ? -->
        </ul>
      </nav>
</header>

  <body class="body">
    <div class="mainContainer">
        <div class="div1">
          <script>
          // assign $curr_avatar to apporpriate creature number (crab = 1, frog = 2, cat = 3, dog = 4)
          var curr_avatar = <?php echo $curr_avatar; ?>;
          //assign the current slide to the current avatar
          if curr_avatar == "crab" {
            var index = 1;
          }
          else if curr_avatar == "frog" {
            var index = 2;
          }
          else if curr_avatar == "cat" {
            var index = 3;
          }
          else if curr_avatar == "dog" {
            var index = 4;
          }
          else {
            var index = 1;
          }
          let slideIndex = index;

          </script>
          <div class="creatureContainer">
            <div class="creature">
              <img src="./media/Creature/Crab.png" style="width: 80%">
            </div>

            <div class="creature">
              <img src="./media/Creature/Frog.png" style="width: 80%">
            </div>

            <div class="creature">
              <img src="./media/Creature/Cat.png" style="width: 80%">
            </div>

            <div class="creature">
              <img src="./media/Creature/Dog.png" style="width: 80%">
            </div>

            <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
            <a class="next" onclick="plusSlides(1)">&#10095;</a>
          </div>
</br>
          <!-- <div style="text-align:center">
            <span class="dot" onclick="currentSlide(1)"></span>
            <span class="dot" onclick="currentSlide(2)"></span>
            <span class="dot" onclick="currentSlide(3)"></span>
            <span class="dot" onclick="currentSlide(4)"></span>
          </div> -->
        </div>

          <div class="div2">
            <button class="saveButton" onclick="saveAvatar()">Save Avatar</button>
          </div>

        <div class="div3">
          <div class="weatherContainer">
            <a class="weatherwidget-io" href="https://forecast7.com/en/42d66n83d15/rochester-hills/" data-label_1="ROCHESTER HILLS" data-label_2="WEATHER" data-icons="Climacons Animated" data-mode="Current" data-days="3" data-theme="original" >ROCHESTER HILLS WEATHER</a>
            <script>
            !function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src='https://weatherwidget.io/js/widget.min.js';fjs.parentNode.insertBefore(js,fjs);}}(document,'script','weatherwidget-io-js');
            </script>
          </div>
        </div>
        <div class="div4">
          <div class="learnBtnContainer">
            <a href="./html/learn.php"><button class="learnButton">LEARN</button></a>
          </div>
        </div>
        <div class="div5">
          <div class="feedContainer">
            <button id="feed" class="feedButton" disabled>FEED</button>
          </div>
        </div>
        <div class="divStarve">
          <div class="starveContainer">
            <button id="starve" class="starveButton">STARVE for testing only</button>
          </div>
        </div>
    </div>
  </body>
</html>