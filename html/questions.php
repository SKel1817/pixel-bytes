<?php
require_once('../connection.php');

// Get the user inputs from the GET request
$subject = isset($_GET['subject']) ? $_GET['subject'] : '';
$level = isset($_GET['level']) ? $_GET['level'] : '';
$category = isset($_GET['category']) ? $_GET['category'] : '';

// Sanitize input values and extract the first letter of level and category
$subject = htmlspecialchars($subject, ENT_QUOTES, 'UTF-8');
$level = htmlspecialchars($level, ENT_QUOTES, 'UTF-8');
$category = htmlspecialchars($category, ENT_QUOTES, 'UTF-8');

//lowercase category
$category = strtolower($category);

// if statment where if level is b then = 1, level is I = 2, level is A = 3
if ($level == 'Beginner') {
  $level = 1;
} elseif ($level == 'Intermediate') {
  $level = 2;
} elseif ($level == 'Advanced') {
  $level = 3;
}
// Build the query
$projectId = 'nielson-4160-f24';
$query = "SELECT * FROM `pixelbytes.$category` 
          WHERE Lvl = $level AND Correct = False 
          LIMIT 10";

// echo '<pre>' . print_r(selectTable($projectId, $query), true) . '</pre>';
$returned_arr = selectTable($projectId, $query);
?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>PixelBytes</title>
    <!--Link to favicon-->
    <link rel="PixelBytes Icon" href="../media/gear.png" type="image/x-icon" />
    <link rel="stylesheet" href="../css/style.css" />
    <script src="../js/questionsScript.js"></script>
  </head>

<header>
    <nav class="nav">
        <a href="../index.php"><img src="../media/gear.png" alt="PixelBytes Logo" height="25px">
        <div class="logo">PixelBytes</div>
        <ul>
          <li><a href="../index.php">Home</a></li>
          <li><a href="./learn.php">Learn</a></li>
          <li><a href="./lessons.php">Lessons</a></li>
          <!-- <li><a href="./html/login.html">Login</a></li> ? -->
        </ul>
      </nav>
</header>

  <body class="body">
    <div class="questionContainer">
        <!-- replace each question, answer1, etc with the database results -->
      <div class="div8" id="question">Question</div>
      <div class="div9" id="answer1">Answer1</div>
      <div class="div10" id="answer2">Answer2</div>
      <div class="div11" id="answer3">Answer3</div>
      <div class="div12" id="answer4">Answer4</div>
      <div class="div13"><button class="submitBtn" id="submit">Submit</button></div>
  </div>
  </body>
</html>