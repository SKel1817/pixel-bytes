<?php

require_once('connection.php');

$projectId = 'nielson-4160-f24';
$category = 'python';
$level = 1;
$query = "SELECT * FROM `pixelbytes.$category` WHERE Lvl = $level LIMIT 10";
// echo '<pre>' . print_r(selectTable($projectId, $query), true) . '</pre>';
$returned_arr = selectTable($projectId, $query);

// Print all questions
foreach ($returned_arr as $row) {
    echo '<h5>' . $row['Question'] . '</h5>';
    echo '<p>' . $row['Answer1'] . '</p>';
    echo '<p>' . $row['Answer2'] . '</p>';  
    echo '<p>' . $row['Answer3'] . '</p>';
    echo '<p>' . $row['Answer4'] . '</p>';
    echo '<p>' . $row['Answer'] . '</p>';
    echo '<br>';
}

// Print first question
echo '<h5>' . $returned_arr[0]['Question'] . '</h5>';
echo '<p>' . $returned_arr[0]['Answer1'] . '</p>';


?>