# PHP and MySQL Support Module

This module is a separate component of the TruckingPro Logistics project, added to satisfy course requirements for PHP and MySQL integration. It handles support messages independently from the main Django application.

## Purpose
A simple "Contact Admin" module where users can submit their name, email, and a message. The data is processed using PHP and stored in a MySQL database.

## Prerequisites
- A local PHP server (e.g., XAMPP, WAMP, or PHP Built-in server).
- A MySQL server (typically included with XAMPP/WAMP).

## Setup Instructions

1.  **Database Configuration**:
    - Open your MySQL administration tool (like phpMyAdmin).
    - Import the `contact_messages.sql` file provided in this folder.
    - This will create a database named `truckingpro_db` and a table named `contact_messages`.

2.  **PHP Configuration**:
    - Ensure `db_connect.php` has the correct credentials.
    - Default settings:
        - Host: `localhost`
        - User: `root`
        - Password: `` (empty)
        - Database: `truckingpro_db`

3.  **Running the Module**:
    - Place the `php_mysql_module` folder in your server's root directory (e.g., `C:/xampp/htdocs/`).
    - Navigate to `http://localhost/php_mysql_module/contact.html` in your web browser.
    - Fill out the form and submit it to test the integration.

## Features
- **Secure Processing**: Uses PHP prepared statements (`mysqli_stmt`) to prevent SQL injection.
- **Input Validation**: Validates required fields and email formats on the server side.
- **Standalone**: Does not interfere with the main Django application.
