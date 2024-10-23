<?php
header('Content-Type: application/json');

// File to store the selected avatar
$file = 'selected_avatar.json';

// Check if the request method is POST and if data is received
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['animal'])) {
    $animal = $_POST['animal'];

    // Save the selected avatar to a JSON file
    file_put_contents($file, json_encode(['animal' => $animal]));

    echo json_encode(['status' => 'success', 'animal' => $animal]);
} else {
    // Read the selected avatar from the JSON file
    if (file_exists($file)) {
        $data = json_decode(file_get_contents($file), true);
        echo json_encode(['status' => 'success', 'animal' => $data['animal']]);
    } else {
        echo json_encode(['status' => 'error', 'message' => 'No animal selected']);
    }
}
?>
