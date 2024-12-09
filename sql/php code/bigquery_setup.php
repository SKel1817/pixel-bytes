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
            // echo '<pre>' . print_r($row, true) . '</pre>';
            array_push($output_arr, $row);
        }
        return $output_arr;
    } catch (Exception $e) {
        // echo 'Error: ' . $e->getMessage();
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

if (basename($_SERVER['PHP_SELF']) == basename(__FILE__)) {
    $projectId = 'nielson-4160-f24';
    $query = 'SELECT * FROM `pixelbytes.addition` LIMIT 10';
    // test update query
    //$query = "UPDATE `nielson-4160-f24.pixelbytes.addition` SET Correct = TRUE WHERE LearnID = 'AB5'";
    echo '<pre>' . print_r(selectTable($projectId, $query), true) . '</pre>';
    //echo '<pre>' . print_r(updateTable($projectId, $query), true) . '</pre>';
}

?>