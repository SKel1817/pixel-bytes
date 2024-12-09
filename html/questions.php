<?php
require_once('../connection.php');

// Get user inputs and sanitize
$subject = isset($_GET['subject']) ? strtolower($_GET['subject']) : '';
$level = isset($_GET['level']) ? $_GET['level'] : (isset($_POST['level']) ? $_POST['level'] : '');
$category = isset($_GET['category']) ? strtolower($_GET['category']) : (isset($_POST['category']) ? strtolower($_POST['category']) : '');

// Convert level to integer
$level_map = ['Beginner' => 1, 'Intermediate' => 2, 'Advanced' => 3];
$level = $level_map[$level] ?? 1; // Default to 1 if no valid level

// Build and execute query
$projectId = 'nielson-4160-f24';
$query = "SELECT * FROM `pixelbytes.$category` WHERE Lvl = $level AND Correct  != true LIMIT 10";
$returned_arr = selectTable($projectId, $query);

// Check if the returned data is valid
if (!is_array($returned_arr) || empty($returned_arr)) {
    echo '<script>alert("No questions available."); window.location.href = "../index.php";</script>';
    exit;
}

// Manage current question index
$current_question_index = isset($_POST['current_question_index']) ? (int)$_POST['current_question_index'] : 0;

// Validate the current question index
if (!isset($returned_arr[$current_question_index])) {
    echo '<script>alert("No more questions available from spot ' . $current_question_index . '"); window.location.href = "../index.php";</script>';
    exit;
}

// Retrieve the current question
$current_question = $returned_arr[$current_question_index];

// Validate the question structure
if (empty($current_question) || !isset($current_question['Question'], $current_question['Answer1'], $current_question['Answer2'], $current_question['Answer3'], $current_question['Answer4'], $current_question['Answer'])) {
    echo '<pre>Debug: Invalid question format</pre>';
    var_dump($current_question);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $selected_answer = isset($_POST['answer']) ? (int)$_POST['answer'] : null;

    // Check if the selected answer matches the correct answer index
    if ($selected_answer === (int)$current_question['Answer']) {
        echo '<script>alert("Correct!");</script>';

        // Construct the UPDATE query
        $learnID = $current_question['LearnID']; // Use the LearnID of the current question
        $update_query = "UPDATE `nielson-4160-f24.pixelbytes.$category` SET Correct = TRUE WHERE LearnID = '$learnID'";

        // Execute the update query
        $update_result = updateTable('nielson-4160-f24', $update_query);

        if ($update_result === true) {
            echo '<script>console.log("Database updated successfully.");</script>';
        } else {
            echo '<script>console.error("Error updating database: ' . $update_result . '");</script>';
        }
        //return to home
        echo '<script>window.location.href = "../index.php";</script>';
    } else {
        echo '<script>alert("Incorrect. Try the next question!");</script>';
    }

    // Increment the question index for the next question
    $current_question_index++;

    // Check if the next question exists
    if (isset($returned_arr[$current_question_index])) {
        $current_question = $returned_arr[$current_question_index];
    } else {
        echo '<script>alert("You have completed all the questions!"); window.location.href = "../index.php";</script>';
        exit;
    }
    }
    else {
        echo '<script>alert("Incorrect. Try the next question!");</script>';
    }

    // Increment the question index for the next question
    $current_question_index++;

    // Check if the next question exists
    if (isset($returned_arr[$current_question_index])) {
        $current_question = $returned_arr[$current_question_index];
    } else {
        echo '<script>alert("You have completed all the questions!"); window.location.href = "../index.php";</script>';
        exit;
    }
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
    <div>
        <form method="POST" action="./questions.php" class="questionContainer">
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
            <!-- Persisting parameters -->
            <input type="hidden" name="current_question_index" value="<?= $current_question_index ?>" />
            <input type="hidden" name="category" value="<?= htmlspecialchars($category, ENT_QUOTES, 'UTF-8') ?>" />
            <input type="hidden" name="level" value="<?= htmlspecialchars($level, ENT_QUOTES, 'UTF-8') ?>" />
            <div class="div13"><button class="submitBtn" type="submit">Submit</button></div>
        </form>
    </div>
</body>
</html>
