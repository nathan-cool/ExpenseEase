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

- **Expense Analytics**: Visual representations of expenses over time, categories, or other criteria to provide users with insights into their spending habits.

- **Budget Planning**: Tools to set monthly or annual budgets for various categories, with notifications for when spending approaches or exceeds these limits.

- **Expense Sharing**: Functionality for users to split and share expenses with others, useful for group activities or shared living arrangements.

- **Receipt Scanning**: Automatically populate expense entries by scanning receipts using OCR technology, reducing manual entry errors and saving time.

- **Multi-Currency Support**: Allow users to record expenses in different currencies, automatically converting them based on current exchange rates for easier management in a global context.



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

To clone this repository and run the Django expenses app locally, follow these steps:

1. **Open Terminal**: Open your terminal if you are on macOS or Linux, or open CMD or PowerShell if you are on Windows.

2. **Install Git**: Ensure you have Git installed on your system. You can download and install it from [Git's official site](https://git-scm.com/downloads).

3. **Clone the Repository**:
    Execute the following command in your terminal to clone the repository:

    ```bash
    git clone https://github.com/yourusername/django-expenses-app.git
    ```
    Replace `yourusername` with your GitHub username or the username of the repository owner. Adjust the repository URL if it is hosted on a different platform or has a different path.

4. **Navigate to the Project Directory**:
    After cloning, enter the directory where the repository has been cloned:

    ```bash
    cd django-expenses-app
    ```

5. **Create a Virtual Environment** (Recommended):
    To create a virtual environment, you need to have Python installed on your system. You can create a virtual environment by running:

    ```bash
    python -m venv venv
    ```

    Activate the virtual environment:

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

6. **Install Dependencies**:
    Install all the dependencies required for the project by running:

    ```bash
    pip install -r requirements.txt
    ```

7. **Set Environment Variables**:
    Create a `.env` file in the root directory of the project and add the necessary environment variables like `DJANGO_SECRET_KEY`, `DATABASE_URL`, and any other required API keys.

8. **Migrate Database**:
    Apply the migrations to create your database schema:

    ```bash
    python manage.py migrate
    ```

9. **Run the Development Server**:
    Start the Django development server:

    ```bash
    python manage.py runserver
    ```

    Once the server is running, you can access the Django expenses app at `http://127.0.0.1:8000` in your web browser.

10. **Access the Application**:
    Open a browser and go to `http://127.0.0.1:8000` to start using the Django expenses app.

Follow these steps to set up your local development environment for the Django expenses app. This will allow you to run the application on your local machine for development and testing purposes.

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
