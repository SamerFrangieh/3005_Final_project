# FitForAll - Health and Fitness Club Management System

This project is designed for COMP 3005 - Winter 2024. It aims to create a comprehensive platform for managing the operations of a health and 
fitness club, catering to members, trainers, and administrative staff. The system allows members to register, set fitness goals, manage profiles, 
and schedule training sessions. Trainers can manage their schedules and view member profiles. Administrative staff can handle room bookings, 
equipment maintenance, class schedules, billing, and payments.


# Installation Instructions #

## Navigate to your destination directory for the project repository

## Clone the repository
- git clone <https://github.com/SamerFrangieh/FitForAll.git>
- cd FitForAll

## Navigate to the Project Directory
- C:\ ...\FitForAll> (you should be here)

## Execute the following commands to install the required packages
- pip install psycopg2
- pip install django

## Create a PostgreSQL Database with pgAdmin
- set the database name to 'fitforall'
- ensure DB_HOST = localhost
- ensure DB_PORT = 5432
- create a username of your choice
- create a password of your choice

## Edit the .env file to meet your Database login requirements
- set DB_USER to match the user corresponding to your Database
- set DB_PASSWORD to match the password corresponding to your Database

## Edit the .env file to meet your Database login credentials
- pip install psycopg2
- pip install django

## Navigate to the app directory within the project directory
- cd .\FitForAll\ 
- C:\ ...\FitForAll\FitForAll> (you should be here)

## Perform Database migrations
- python manage.py makemigrations
- python manage.py migrate

## Start the server
- python manage.py runserver

# Website Instructions #

## Member Registration
- Allows new users to register as members of the gym.
- Requires members to provide personal information, including name, password, height, weight, and fitness goals.
- Ensures that each member has a unique username or email for login purposes.

## Member Login / Member Dashboard
- Provides a login form for registered members to access their personalized dashboard.
- The dashboard includes features such as:
  - Scheduling, viewing, and cancelling personal training sessions
  - Checking available periods for personal training sessions. 
  - Enrolling and Unenrolling in Group Fitness Classes.
  - Access to workout history and upcoming scheduled sessions.
  - Ability to update personal information and fitness goals.
  - Submitting detailed health information to the member's profile (Blood Pressure readings, height, weight, age, fitness goals, exercise habits)
    which are useful for: 
      - creating a full exercise routine according to the member's body attributes and fitness goals
      - Calculating and displaying health statistics (BMI, Blood Pressure, and Basal Metabolic Rate)
      - Displaying Fitness Achievements to track the member's fitness journey

## Trainer Login / Trainer Dashboard
- **Secured Access**: Trainers log in with credentials issued by the gym management, ensuring that each trainer accesses only their designated information and tools.
- **Daily Scheduling and Availability**:
  - Trainers can update their daily availability by setting specific check-in and check-out times for each day of the week, providing flexibility and clear communication with clients and gym management.
  - Default times are set to '0:00' which indicates no availability unless updated.
- **Client Management**:
  - View and manage personal client lists which include client progress reports, scheduled sessions, and historical data.
  - Ability to add new workout plans, update existing ones, and monitor client adherence and progress.
- **Appointment Scheduling**:
  - Manage and schedule training sessions with an easy-to-use interface that shows daily, weekly, or monthly calendars.
  - Handle appointment changes, cancellations, and re-scheduling effortlessly.
- **Member Search Functionality**:
  - Search for members by name to quickly access their profiles, workout plans, and training history.
  - Useful for preparing personalized sessions and tracking long-term fitness goals.
- **Resource Access**:
  - Access to a library of training materials, exercises, dietary guidelines, and other resources to enhance the training experience for clients.
- **Feedback and Communication**:
  - Send and receive feedback directly through the dashboard to improve training strategies and client satisfaction.
  - Maintain active communication channels with clients and gym management for updates and notifications.

## Admin Login / Admin Dashboard
- Exclusively for gym administrators or management personnel.
- Allows management of the entire gym system, including:
  - Adding or removing equipment and scheduling maintenance.
  - Creating or updating class schedules and trainer assignments.

# ER-Diagram #
- https://github.com/SamerFrangieh/FitForAll/blob/main/ER-diagram.png

- # Video Demonstration #
- paste the link to the vid here




