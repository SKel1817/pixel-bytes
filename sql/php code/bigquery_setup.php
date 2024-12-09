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

if (basename($_SERVER['PHP_SELF']) == basename(__FILE__)) {
    $projectId = 'nielson-4160-f24';
    $query = 'SELECT * FROM `pixelbytes.addition` LIMIT 10';
    echo '<pre>' . print_r(selectTable($projectId, $query), true) . '</pre>';
}

?>