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

// Extract the first letters if values are provided
$level_initial = !empty($level) ? substr($level, 0, 1) : '';
$category_initial = !empty($category) ? substr($category, 0, 1) : '';

// Construct the LearnID pattern
$learn_id_pattern = $category_initial . $level_initial . '_';

// Build the query
$projectId = 'nielson-4160-f24';
$query = "SELECT * FROM `pixelbytes.articles` 
          WHERE LearnID LIKE '$learn_id_pattern' 
          ORDER BY LearnID 
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
  <script src="../js/script.js"></script>
</head>

<header>
  <nav class="nav">
      <a href="../index.php"><img src="../media/gear.png" alt="PixelBytes Logo" height="25px" /></a>
      <div class="logo">PixelBytes</div>
      <div class="food">
       <div>
      <ul>
        <li><a href="../index.php">Home</a></li>
        <li><a href="./learn.php">Learn</a></li>
        <li><a href="./lessons.php">Lessons</a></li>
        <!-- <li><a href="./html/login.html">Login</a></li> ? -->
      </ul>
    </nav>
</header>

<body class="body">
  <div class="learnContainer">
    <div class="learnTxt">
    <!-- place for text or whatever -->
    <!-- add header that is the category and level -->
     <?php
        echo '<h2>' . $category . ' ' . $level . '</h2>';
        foreach ($returned_arr as $row) {
            echo '<p>' . $row['Article'] . '</p>';
            echo '<br>';
        }
     ?>
  </div>
  </div>
</body>
</html>