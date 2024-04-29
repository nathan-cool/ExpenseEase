# Django expenses app 

[View the live project here](...)

## Index – Table of Contents
* [User Experience (UX)](#user-experience-ux) 
* [Features](#features)
* [Design](#design)
* [Planning](#planning)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## User Experience (UX)

### User stories :
- As a user, I want to be able to easily register and log in, so that I can manage my expenses securely.

## Features

### Existing Features

#### Authentication System

- **Registration System**: Allows users to create a new account by providing their name, email, and password. The registration view splits the user's name into first and last names, validates the provided information, and if valid, sends a verification email to activate the account.

- **Login System**: Users can log in to their account using their email and password. The system checks if the account is active and has correct credentials before granting access.

- **Logout System**: Logged-in users can log out of their account, which redirects them to the login page with a success message.

- **Google OAuth Integration**: Users have the option to authenticate using Google, simplifying the login process without the need for a password.

- **Email Validation**: Validates emails in real-time during registration to ensure they are not already in use and follow the correct format.

- **Password Validation**: Checks password strength to ensure it meets the required criteria for security.

- **Account Verification**: After registration, users receive an email with a link to verify their account, ensuring the email address belongs to them.

 #### Expense Management

- **View Expenses**: Users can view all their recorded expenses on the main expense dashboard. This feature ensures easy tracking and management of daily expenses.

- **Add Expenses**: Users can add new expenses by filling out a form that captures essential details such as the amount, date, category, and a description. If the required fields are not filled, the system prompts the user with error messages, ensuring data integrity.

- **Edit Expenses**: Each expense can be edited using the edit functionality. Users can update the amount, date, category, description, and other relevant details. The system validates the input before saving to maintain accurate and up-to-date records.

- **Delete Expenses**: Expenses can be deleted with a confirmation step to prevent accidental deletions. This function improves data management by allowing users to remove erroneous or outdated entries.

- **Generate Expense Descriptions Using AI**: A unique feature that utilizes OpenAI's API to generate descriptive texts for expenses based on minimal input. This helps users quickly fill in detailed descriptions without needing to manually type extensive details.

### Features which could be implemented in the future

- **Password Reset**: Allows users to reset their password if forgotten, via a link sent to their registered email.
- **Two-Factor Authentication**: Adds an extra layer of security by requiring a second form of identification beyond just the username and password.



## Design

-   ### Wireframes

-   ### Entity-Relationship diagrams for DBMS

## Planning

## Technologies Used

### Languages Used

### Frameworks, Libraries & Programs Used

## Testing

### Validator Testing 

### Automated Testing

### Browser Compatibility

### Manual Testing Test Cases and Results

### Known bugs

## Deployment

### How to Clone the Repository 

### Create Application and Postgres DB on Heroku

### Configure Cloudinary to host images used by the application

### Connect the Heroku app to the GitHub repository

### Executing automated tests

### Final Deployment steps

## Credits 

### Code 

### Content 

### Media 

### Acknowledgments
