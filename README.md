# TruckingPro Logistics Web Application

Welcome to the **TruckingPro Logistics** project! This is a modern, web-based platform for ordering and managing truck shipments. We built it using the Django framework.

## 1. Project Description
TruckingPro Logistics is a simple and reliable web application. It connects people who need to ship items (Customers) with the logistics team (Admins). The system allows users to create new truck requests, enter shipment details, and track the status of their orders. 

## 2. Why We Chose Django?
We chose Django for this project because:
- **Fast Development:** Django has built-in tools (like authentication and admin panels) that save a lot of time.
- **Security:** It is very secure and protects the website from common attacks (like SQL injection and cross-site scripting).
- **Database Management:** Django uses an Object-Relational Mapper (ORM). This means we can write Python code instead of complex SQL queries to manage the database.
- **Scalability:** Django is strong enough to handle a large number of users and orders if the business grows.

## 3. Features
- **User Accounts:** Users can register, log in, and manage their personal profile.
- **Create Orders:** Customers can submit new truck requests. They can add route information, shipment size, weight, and preferred schedule.
- **Dashboard Tracking:** Customers have a beautiful dashboard to monitor all their orders. They can see summary statistics and check if an order is *Pending*, *In Progress*, *Delivered*, or *Cancelled*.
- **Admin Management:** The logistics team has a powerful admin panel. They can view all orders, change the order status, and leave comments for the customer.
- **Email Notifications:** The system sends an email to the admin when a new order is created. It also sends an email to the customer when the admin changes the order status or adds a comment.

## 4. Technical Structure
The application follows Django's **MVT (Model-View-Template)** structure:

### Models (The Database)
We use models to define the structure of our data.
- **User Model:** We use Django's built-in User model for authentication.
- **TruckOrder Model:** This model saves all information about the order. It has fields for pickup location, delivery location, shipment details, schedule, status, and admin comments.

### Views (The Controllers)
Views are the "brain" of the application. They take the user's request, talk to the database (Models), and send back the correct page (Template).
- `home`: Shows the landing page.
- `dashboard`: Gets the user's orders, calculates the statistics, and shows the dashboard.
- `create_order`: Handles the form submission to save a new truck request.
- `profile`: Allows the user to update their personal information.

### Templates (The Frontend)
Templates are the HTML files that the user sees. 
- We designed the website using **Vanilla CSS** to make it look professional and corporate (orange and charcoal colors). 
- We use a `base.html` file to keep the navigation bar and footer consistent across all pages.

### How the Request is Moving?
1. The user clicks a button or types a URL in the browser.
2. Django's `urls.py` looks at the URL and sends the request to the correct **View**.
3. The **View** talks to the **Model** to get or save data in the database.
4. The **View** sends the data to the **Template**.
5. The **Template** builds the final HTML page and sends it back to the user's browser.

## PHP and MySQL Module
In addition to the Django-based truck ordering system, this project includes a separate PHP and MySQL module located in the `php_mysql_module` folder. This module contains a Contact Admin form processed by PHP and stored in a MySQL database using prepared statements. It demonstrates PHP backend processing and MySQL database integration while keeping the main Django application unchanged.

## 5. Actors of the System
There are two main actors in this system:
1. **The Customer (User):** They can register, log in, create truck orders, update their profile, and view their dashboard.
2. **The Administrator (Logistics Team):** They log into the secret `/admin` panel. They read the orders, assign drivers in real life, update the status in the system, and write comments.

## 6. How to Set Up the Project
If you want to open this project on your local device, follow these steps:

**Prerequisites:**
You need to install Python (version 3.8 or higher) on your computer.

**Step 1: Open the Terminal**
Open your terminal (Command Prompt, PowerShell, or bash) and navigate to the project folder.

**Step 2: Create a Virtual Environment**
It is good practice to use a virtual environment.
```bash
python -m venv venv
```

**Step 3: Activate the Virtual Environment**
- On Windows: `.\venv\Scripts\activate`
- On Mac/Linux: `source venv/bin/activate`

**Step 4: Install Django**
```bash
pip install django
```

**Step 5: Apply Database Migrations**
This command builds the database tables from our models.
```bash
python manage.py makemigrations
python manage.py migrate
```

**Step 6: Create an Admin Account (Superuser)**
You need this account to access the admin panel.
```bash
python manage.py createsuperuser
```
Follow the instructions to set a username, email, and password.

**Step 7: Run the Server**
```bash
python manage.py runserver
```

**Step 8: Open the Browser**
- **User Website:** Go to `http://127.0.0.1:8000/`
- **Admin Panel:** Go to `http://127.0.0.1:8000/admin/`

**Test Accounts:**
To quickly test the application, you can use these default accounts (you can log in using either the username or the email address):

- **Admin Account (Logistics Team)**
  - Username: `admin`
  - Email: `admin@example.com`
  - Password: `123456`
  - *Note: Logging in with this account will automatically direct you to the admin panel.*

- **Regular User Account (Customer)**
  - Username: `user`
  - Email: `user@example.com`
  - Password: `123456`

## 7. Testing
We wrote automated unit tests to make sure the application works very well. We tested the models, the forms, and all the views.

To run the tests, open your terminal and type:
```bash
python manage.py test truck_app
```
You will see an `OK` message if everything is working correctly!

## 8. Development Team
This project was developed by UPMers: 
- **Salem Shurrab**
- **Hamidullah Abduljabar S. Saifudin**
- **ALOUH F. FOAD**
