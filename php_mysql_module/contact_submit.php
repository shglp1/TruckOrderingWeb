<?php
include 'db_connect.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Read and trim inputs
    $full_name = trim($_POST['full_name']);
    $email = trim($_POST['email']);
    $message = trim($_POST['message']);

    // Validation
    if (empty($full_name) || empty($email) || empty($message)) {
        echo "Error: All fields are required.";
        exit;
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo "Error: Invalid email format.";
        exit;
    }

    // Prepare and bind
    $stmt = $conn->prepare("INSERT INTO contact_messages (full_name, email, message) VALUES (?, ?, ?)");
    $stmt->bind_param("sss", $full_name, $email, $message);

    // Execute and check
    if ($stmt->execute()) {
        echo "Success: Your message has been sent successfully!";
    } else {
        echo "Error: " . $stmt->error;
    }

    // Close statement and connection
    $stmt->close();
    $conn->close();
} else {
    echo "Error: Invalid request method.";
}
?>
