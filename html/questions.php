<?php
require_once('../connection.php');

// Get the user inputs from the GET request
$subject = isset($_GET['subject']) ? strtolower($_GET['subject']) : '';
$level = isset($_GET['level']) ? $_GET['level'] : '';
$category = isset($_GET['category']) ? $_GET['category'] : '';

// Sanitize and process inputs
$subject = htmlspecialchars($subject, ENT_QUOTES, 'UTF-8');
$level = htmlspecialchars($level, ENT_QUOTES, 'UTF-8');
$category = htmlspecialchars($category, ENT_QUOTES, 'UTF-8');

// make category lowercase
$category = strtolower($category);

if ($level == 'Beginner') {
    $level = 1;
} elseif ($level == 'Intermediate') {
    $level = 2;
} elseif ($level == 'Advanced') {
    $level = 3;
}

// Query to fetch questions
$projectId = 'nielson-4160-f24';
$query = "SELECT * FROM `pixelbytes.$category` 
          WHERE Lvl = $level AND Correct = False 
          LIMIT 10";

$returned_arr = selectTable($projectId, $query);

// Ensure $returned_arr is properly structured
if (!is_array($returned_arr) || empty($returned_arr)) {
    echo '<script>alert("No questions available."); window.location.href = "../index.php";</script>';
    exit;
}

// Get the current question index (default to 0)
$current_question_index = isset($_POST['current_question_index']) ? (int)$_POST['current_question_index'] : 0;

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $selected_answer = isset($_POST['answer']) ? (int)$_POST['answer'] : null;

    if ($selected_answer === (int)$returned_arr[$current_question_index]['Answer']) {
        // Correct answer: Call the JavaScript feed() function and redirect
        echo "<script>
                feed();
                setTimeout(function() {
                    window.location.href = '../index.php';
                }, 1000);
              </script>";
        exit;
    } else {
        // Incorrect answer: Increment index for the next question
        $current_question_index++;
        if ($current_question_index >= count($returned_arr)) {
            echo '<script>alert("Incorrect. No more questions available!"); window.location.href = "../index.php";</script>';
            exit;
        }
    }
}

// Get the current question after form submission or initialization
$current_question = $returned_arr[$current_question_index];
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>PixelBytes</title>
    <link rel="PixelBytes Icon" href="../media/gear.png" type="image/x-icon" />
    <link rel="stylesheet" href="../css/style.css" />
</head>
<header>
    <nav class="nav">
        <a href="../index.php"><img src="../media/gear.png" alt="PixelBytes Logo" height="25px">
        <div class="logo">PixelBytes</div>
        <ul>
            <li><a href="../index.php">Home</a></li>
            <li><a href="./learn.php">Learn</a></li>
            <li><a href="./lessons.php">Lessons</a></li>
        </ul>
    </nav>
</header>
<body class="body">
    <div class="questionContainer">
        <form method="POST" action="./questions.php">
            <div class="div8" id="question"><?= htmlspecialchars($current_question['Question'], ENT_QUOTES, 'UTF-8') ?></div>
            <div class="div9">
                <input type="radio" name="answer" value="0" id="answer1" required />
                <label for="answer1"><?= htmlspecialchars($current_question['Answer1'], ENT_QUOTES, 'UTF-8') ?></label>
            </div>
            <div class="div10">
                <input type="radio" name="answer" value="1" id="answer2" />
                <label for="answer2"><?= htmlspecialchars($current_question['Answer2'], ENT_QUOTES, 'UTF-8') ?></label>
            </div>
            <div class="div11">
                <input type="radio" name="answer" value="2" id="answer3" />
                <label for="answer3"><?= htmlspecialchars($current_question['Answer3'], ENT_QUOTES, 'UTF-8') ?></label>
            </div>
            <div class="div12">
                <input type="radio" name="answer" value="3" id="answer4" />
                <label for="answer4"><?= htmlspecialchars($current_question['Answer4'], ENT_QUOTES, 'UTF-8') ?></label>
            </div>
            <input type="hidden" name="current_question_index" value="<?= $current_question_index ?>" />
            <div class="div13"><button class="submitBtn" type="submit">Submit</button></div>
        </form>
    </div>
</body>
</html>
