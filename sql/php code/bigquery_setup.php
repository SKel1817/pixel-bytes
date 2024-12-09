<?php

error_reporting(E_ALL);
ini_set('display_errors', 'On');

require 'vendor/autoload.php'; // Ensure the autoload file is included

use Google\Cloud\BigQuery\BigQueryClient;

putenv('GOOGLE_APPLICATION_CREDENTIALS=/home/nielsontaylor1103/nielson-4160-f24-fc7ef783ed23.json');

function selectTable($projectId, $query)
{
    try {
        $output_arr = array();
        // Initialize BigQuery client
        $bigQuery = new BigQueryClient([
            'projectId' => $projectId,
        ]);

        // Run the query
        $queryJob = $bigQuery->runQuery($bigQuery->query($query));

        // Fetch results
        foreach ($queryJob->rows() as $row) {
            array_push($output_arr, $row);
        }
        return $output_arr;
    } catch (Exception $e) {
        array_push($output_arr, 'Error: ' . $e->getMessage());
        return $output_arr;
    }
}

function updateTable($projectId, $query)
{
    try {
        // Initialize BigQuery client
        $bigQuery = new Google\Cloud\BigQuery\BigQueryClient([
            'projectId' => $projectId,
        ]);

        // Execute the query
        $queryJob = $bigQuery->runQuery($bigQuery->query($query));

        // Wait for the query to complete
        $queryJob->waitUntilComplete();

        // Check if the query was successful
        if (!$queryJob->isComplete()) {
            throw new Exception('Query did not complete successfully.');
        }

        return true; // Indicate success
    } catch (Exception $e) {
        // Handle errors
        return 'Error: ' . $e->getMessage();
    }
}

function insertTable($projectId, $query)
{
    try {
        // Initialize BigQuery client
        $bigQuery = new Google\Cloud\BigQuery\BigQueryClient([
            'projectId' => $projectId,
        ]);

        // Execute the query
        $queryJob = $bigQuery->runQuery($bigQuery->query($query));

        // Wait for the query to complete
        $queryJob->waitUntilComplete();

        // Check if the query was successful
        if (!$queryJob->isComplete()) {
            throw new Exception('Query did not complete successfully.');
        }

        return true; // Indicate success
    } catch (Exception $e) {
        // Handle errors
        return 'Error: ' . $e->getMessage();
    }
}

if (basename($_SERVER['PHP_SELF']) == basename(__FILE__)) {
    $projectId = 'nielson-4160-f24';
    
    // Test SELECT query
    $selectQuery = 'SELECT * FROM `pixelbytes.addition` LIMIT 10';
    echo '<pre>' . print_r(selectTable($projectId, $selectQuery), true) . '</pre>';
    
    // Test UPDATE query
    //$updateQuery = "UPDATE `nielson-4160-f24.pixelbytes.addition` SET Correct = TRUE WHERE LearnID = 'AB5'";
    //echo '<pre>' . print_r(updateTable($projectId, $updateQuery), true) . '</pre>';
    
    // Test INSERT query
    $insertQuery = "INSERT INTO `nielson-4160-f24.pixelbytes.user_data` (Date, question_answered) VALUES ('2024-10-01', true)";
    echo '<pre>' . print_r(insertTable($projectId, $insertQuery), true) . '</pre>';
}

?>
