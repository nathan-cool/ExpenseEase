# ExpenseEase

[View the live project here](...)

## Table of Contents
- [User Experience (UX)](#user-experience-ux)
  - [Overview](#overview)
  - [User Stories](#user-stories)
  - [Developer Tasks](#developer-tasks)
  - [Agile](#agile)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)
- [Design](#design)
  - [Wireframes](#wireframes)
  - [Database Schema](#database-schema)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
  - [How to Clone the Repository](#how-to-clone-the-repository)
  - [Create Application and Postgres DB on Heroku](#create-application-and-postgres-db-on-heroku)
- [Credits](#credits)
  - [Code](#code)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgments](#acknowledgments)


## User Experience (UX)

### Overview
The ExpenseEase project was created to offer a user-friendly and secure way to manage personal expenses. It aims to streamline tracking daily financial activities and includes advanced features like Google OAuth integration and AI-driven expense descriptions. This app is designed for anyone looking to take control of their finances and better understand their spending habits.

### User Stories
- As a user, I would like to know when I reach a page I don't have access to.
- As a user, I would like to log in so that I can access my account.
- As a user, I would like to register for a new account so that I can create my profile and start managing my expenses.
- As a user, I would like the ability to add an expense to keep track of my expenses.
- As a user, I want the ability to view my expenses.
- As a user, I want the ability to edit my expenses.
- As a user, I want the ability to delete an expense.
- As a user, I would like to log out of my account.

### Developer Tasks
- As a developer, I need to create a readme file.
- As a developer, I need to set up my project.
- As a developer, I need to deploy my project to Heroku.
- As a developer, I need to create a base HTML page and structure.
- As a developer, I need to integrate Google authentication.


### Agile

The Agile methodology was employed to plan and manage the development of the ExpenseEase project. GitHub was used as the primary tool to demonstrate the Agile approach.

User Stories were then created as GitHub Issues, linked to the Epics. Custom issue templates were used to ensure consistency and clarity in describing the User Stories. Each User Story followed a specific format, including a title, and description.

A link to my Kanban board can be found [here](https://github.com/users/nathan-cool/projects/2/views/1?pane=issue&itemId=55533266)

![image](https://github.com/nathan-cool/django-expense-organizer/assets/127421398/035d6f2e-927e-4062-8ffd-3d0639c2d248)

## Features

### Existing Features

#### Authentication System and Security
- **Registration System**: Allows users to create a new account by providing their name, email, and password. The registration view splits the user's name into first and last names, validates the provided information, and if valid, sends a verification email to activate the account.
- **Login System**: Users can log in to their account using their email and password. The system checks if the account is active and has correct credentials before granting access.
- **Logout System**: Logged-in users can log out of their account, which redirects them to the login page with a success message.
- **Google OAuth Integration**: Users have the option to authenticate using Google, simplifying the login process without the need for a password.
- **Email Validation**: Validates email in real-time during registration to ensure they are not already in use and follow the correct format.
- **Password Validation**: Checks password strength to ensure it meets the required criteria for security.
- **Account Verification**: After registration, users receive an email with a link to verify their account, ensuring the email address belongs to them.

To restrict access to certain views and features, the Django `@login_required` decorator is used. This ensures that only registered and authenticated users can access these views. If an unauthenticated user tries to reach these views, they will be redirected to the login page.

#### Expense Management
- **View Expenses**: Users can view all their recorded expenses on the main expense dashboard.
- **Add Expenses**: Users can add new expenses by filling out a form that captures essential details such as the amount, date, category, and a description.
- **Edit Expenses**: Each expense can be edited using the edit functionality. Users can update the amount, date, category, description, and other relevant details.
- **Delete Expenses**: Expenses can be deleted with a confirmation step to prevent accidental deletions.
- **Generate Expense Descriptions Using AI**: Utilizes OpenAI's API to generate descriptive texts for expenses based on minimal input.
- **Multi-Currency Support**: Allow users to record expenses in different currencies, automatically converting them based on current exchange rates.
- **Search Expenses**:
- **pagination**:


### Future Features
- **Password Reset**: Allows users to reset their password if forgotten, via a link sent to their registered email.
- **Two-Factor Authentication**: Adds an extra layer of security by requiring a second form of identification beyond just the username and password.
- **Expense Analytics**: Visual representations of expenses over time, categories, or other criteria to provide users with insights into their spending habits.
- **Budget Planning**: Tools to set monthly or annual budgets for various categories, with notifications for when spending approaches or exceeds these limits.
- **Expense Sharing**: Functionality for users to split and share expenses with others, useful for group activities or shared living arrangements.
- **Receipt Scanning**: Automatically populate expense entries by scanning receipts using OCR technology.





## The Skeleton Plain

### Wireframes

<details>
<summary>Main User Panel Wireframe</summary>
<br>
<img src="https://github.com/nathan-cool/django-expense-organizer/assets/127421398/bd58da71-5489-4f9f-a3ee-5acfe4f9a446" alt="Main User Panel">
</details>

<details>
<summary>Login Screen Wireframe</summary>
<br>
<img src="https://github.com/nathan-cool/django-expense-organizer/assets/127421398/aa88acc9-0e5f-45aa-80c9-d30c2b398442" alt="Login Screen">
</details>

<details>
<summary>Sign Up Screen Wireframe</summary>
<br>
<img src="https://github.com/nathan-cool/django-expense-organizer/assets/127421398/ea565ffb-fce8-40f4-8c36-68b1510cd27b" alt="Sign Up Screen">
</details>

<details>
<summary>Edit/Add Expense Screen Wireframe</summary>
<br>
<img src="https://github.com/nathan-cool/django-expense-organizer/assets/127421398/f1b00191-8bb1-4f60-b347-95b7e0aacde1" alt="Edit/Add Expense Screen">
</details>

### Database Schema

The database schema for this project is as follows: 

- **User Model (Built-in Django User Model)**
 - Fields:
   - `username`: CharField for storing the username (unique).
   - `email`: EmailField for storing the user's email address (unique).
   - `first_name`: CharField for storing the user's first name.
   - `last_name`: CharField for storing the user's last name.
   - `password`: CharField for storing the hashed password.
   - `is_active`: BooleanField indicating whether the user account is active.

- **Category Model**
 - Fields:
   - `name`: CharField for storing the name of the expense category.

- **Expenses Model**
 - Fields:
   - `owner`: ForeignKey relationship with the User model (on_delete=models.CASCADE).
   - `amount`: DecimalField for storing the expense amount.
   - `date`: DateField for storing the expense date.
   - `category`: CharField for storing the expense category.
   - `description`: TextField for storing the expense description.
   - `invoice_number`: CharField for storing the invoice number (optional).
   - `reference`: CharField for storing the reference (optional).

- **Preferences Model**
 - Fields:
   - `currency`: Allows users to change currency from the settings tab

  

## The Surface Plane

### Design

#### Colour Scheme

- **White (#FFFFFF)**: The main background color, offering a clean and bright look.
- **Dark Grey (#333533)**: Used for main text and key elements, providing high readability and contrast.
- **Violet (#712cf9)**: Adds vibrancy to buttons and interactive components.
- **Dark (#202020)**: Enhances visual feedback with button hover states.
- **Green (#1f7c4d)**: Signifies success messages and confirmations.
- **Purple (#5a23c8)**: Adds depth to design elements with shadow effects.

#### Typography

I've chosen **Nunito** as our primary font. It's clean, modern, and easy to read, making for a pleasant user experience.

#### Layout and Elements

- **Input Fields**: Rounded for a modern look.
- **Cards**: Custom widths and shadows enhance visual appeal.
- **Forms and Buttons**: Clean and simple, with hover effects to improve interaction feedback.
- **Responsive Design**: The app adapts to different screen sizes, ensuring a consistent experience whether you're on a phone, tablet, or desktop.

#### Special Elements

- **Alerts**: Success alerts are styled in green with white text to clearly indicate positive actions.
- **Password Toggle**: Conveniently placed for easy access, blending seamlessly with the form.
- **Navbar**: Simple and functional, with text styled for readability and a polished look.

#### Imagery

I've used background patterns and radial gradients to add depth and texture, creating a visually appealing and modern interface.

These design choices ensure the ExpenseEase looks great and is easy to use, no matter what device you're on.


## Planning

## Technologies Used

### Languages Used
- **Python 3**: The core backend programming language used for the application.
- **HTML5**: Used for structuring the web pages of the application.
- **CSS3**: Used to style the HTML content.
- **JavaScript**: Employed for adding interactive behaviors to web pages.

### Frameworks, Libraries & Programs Used
- **Django**: A high-level Python web framework used for developing the web application.
- **Python Standard Library**: Various modules such as `os`, `json`, and `re`.
- **dotenv**: Used for loading environment variables from a `.env` file.
- **OpenAI**: API used to generate descriptions for expenses.
- **Google OAuth**: Used for Google OAuth authentication.
- **JSON Web Tokens (JWT)**: Used for authentication and authorization.
- **Django Messages Framework**: Used to display success and error messages.
- **Django Authentication System**: For user registration, login, and logout functionality.
- **Django Email**: Used to send verification emails.

### Software & Web Applications Used
- **Git**: Used for version control.
- **GitHub**: For hosting Git repositories.
- **Visual Studio Code**: A code editor used for development.
- **Heroku**: Cloud platform used for deploying and hosting the web application.
- **PostgreSQL**: Used as the primary database.
- **Google Fonts**: Used for typography.
- **Balsamiq**: Used for creating mockups and prototypes.
- **Draw.io**: Used for creating visual representations of the application's architecture and user flows.


## Testing

### Validator Testing 

### Automated Testing

### Browser Compatibility


![Browser Testing](https://github.com/nathan-cool/django-expense-organizer/assets/127421398/803a96f7-b3be-4628-9c2b-2927e985ca0e)



### Manual Testing with User Storeys 

<details>
 
<summary>Social Authentication</summary>

<table>
<tr><th>Test</th><th>Result</th></tr>
<tr><td>Test successful Google OAuth authentication and user creation</td><td>✓</td></tr>
<tr><td>Test successful Google OAuth authentication with existing user</td><td>✓</td></tr>
<tr><td>Test failed Google OAuth authentication</td><td>✓</td></tr>
</table>

</details>

<details>
 
<summary>User Registration</summary>

<table>
<tr><th>Test</th><th>Result</th></tr>
<tr><td>Test successful user registration with valid data</td><td>✓</td></tr>
<tr><td>Test registration with invalid password</td><td>✓</td></tr>
<tr><td>Test registration with invalid name</td><td>✓</td></tr>
<tr><td>Test registration with invalid email</td><td>✓</td></tr>
<tr><td>Test registration with existing email</td><td>✓</td></tr>
</table>

</details>

<details>
 
<summary>Email Validation</summary>

<table>
<tr><th>Test</th><th>Result</th></tr>
<tr><td>Test email validation with empty email</td><td>✓</td></tr>
<tr><td>Test email validation with existing email</td><td>✓</td></tr>
<tr><td>Test email validation with invalid email format</td><td>✓</td></tr>
<tr><td>Test email validation with valid email</td><td>✓</td></tr>
</table>

</details>

<details>
 
<summary>Name Validation</summary>

<table>
<tr><th>Test</th><th>Result</th></tr>
<tr><td>Test name validation with empty name</td><td>✓</td></tr>
<tr><td>Test name validation with invalid characters</td><td>✓</td></tr>
<tr><td>Test name validation with valid name</td><td>✓</td></tr>
</table>

</details>

<details>
 
<summary>Password Validation</summary>

<table>
<tr><th>Test</th><th>Result</th></tr>
<tr><td>Test password validation with short password</td><td>✓</td></tr>
<tr><td>Test password validation with password missing required characters</td><td>✓</td></tr>
<tr><td>Test password validation with valid password</td><td>✓</td></tr>
</table>

</details>

<details>
 
<summary>User Verification</summary>

<table>
<tr><th>Test</th><th>Result</th></tr>
<tr><td>Test successful user verification</td><td>✓</td></tr>
<tr><td>Test verification with invalid token</td><td>✓</td></tr>
<tr><td>Test verification of already active user</td><td>✓</td></tr>
</table>

</details>

<details>
<summary>User Login and Logout</summary>

<table>
<tr><th>Test</th><th>Result</th></tr>
<tr><td>Test successful user login</td><td>✓</td></tr>
<tr><td>Test login with inactive account</td><td>✓</td></tr>
<tr><td>Test login with invalid credentials</td><td>✓</td></tr>
<tr><td>Test successful user logout</td><td>✓</td></tr>
</table>

</details>

<details>
<summary>Expense Management</summary>

<table>
<tr><th>Test</th><th>Result</th></tr>
<tr><td>Test adding expense with valid data</td><td>✓</td></tr>
<tr><td>Test adding expense with missing required fields</td><td>✓</td></tr>
<tr><td>Test editing expense with valid data</td><td>✓</td></tr>
<tr><td>Test editing expense with missing required fields</td><td>✓</td></tr>
<tr><td>Test deleting expense</td><td>✓</td></tr>
</table>

</details>

<details>
 
<summary>Description Generation</summary>

<table>
<tr><th>Test</th><th>Result</th></tr>
<tr><td>Test generating description with valid expense details</td><td>✓</td></tr>
<tr><td>Test handling error during description generation
</table>
</details>

### Device Testing
<details>
<summary>Responsivness</summary>

<table>
  <thead>
    <tr>
      <th>Device</th>
      <th>Test One</th>
      <th>Test Two</th>
      <th>Result One</th>
      <th>Result Two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>iPhone SE</td>
      <td>Responsiveness</td>
      <td>Buttons/Features</td>
      <td>Pass</td>
      <td>Pass</td>
    </tr>
    <tr>
      <td>iPhone X</td>
      <td>Responsiveness</td>
      <td>Buttons/Features</td>
      <td>Pass</td>
      <td>Pass</td>
    </tr>
    <tr>
      <td>iPhone 14</td>
      <td>Responsiveness</td>
      <td>Buttons/Features</td>
      <td>Pass</td>
      <td>Pass</td>
    </tr>
    <tr>
      <td>iPhone 6</td>
      <td>Responsiveness</td>
      <td>Buttons/Features</td>
      <td>Pass</td>
      <td>Pass</td>
    </tr>
    <tr>
      <td>Galaxy Fold</td>
      <td>Responsiveness</td>
      <td>Buttons/Features</td>
      <td>Pass</td>
      <td>Pass</td>
    </tr>
    <tr>
      <td>24-inch Monitor</td>
      <td>Responsiveness</td>
      <td>Buttons/Features</td>
      <td>Pass</td>
      <td>Pass</td>
    </tr>
    <tr>
      <td>13-inch Laptop</td>
      <td>Responsiveness</td>
      <td>Buttons/Features</td>
      <td>Pass</td>
      <td>Pass</td>
    </tr>
  </tbody>
</table>
</details>




### Known bugs

#### Generate Expense Descriptions Using AI

- When attempting to create a new invoice, users are expected to be able to use AI to generate descriptive texts based on minimal input. However, this functionality does not trigger during the invoice creation process, although it operates correctly during the editing of invoices.

## Deployment

### How to Clone the Repository
<details>
<summary>Click to expand</summary>

To clone this repository and run the Django expenses app locally, follow these steps:

1. **Open Terminal**: Open your terminal if you are on macOS or Linux, or open CMD or PowerShell if you are on Windows.
2. **Install Git**: Ensure you have Git installed on your system. You can download and install it from [Git's official site](https://git-scm.com/downloads).
3. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/django-expenses-app.git
    ```
    Replace `yourusername` with your GitHub username or the username of the repository owner.
4. **Navigate to the Project Directory**:
    ```bash
    cd django-expenses-app
    ```
5. **Create a Virtual Environment** (Recommended):
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
    ```bash
    pip install -r requirements.txt
    ```
7. **Set Environment Variables**: Create a `.env` file in the root directory of the project and add the necessary environment variables like `DJANGO_SECRET_KEY`, `DATABASE_URL`, and any other required API keys.
8. **Migrate Database**:
    ```bash
    python manage.py migrate
    ```
9. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```
    Once the server is running, you can access the Django expenses app at `http://127.0.0.1:8000` in your web browser.
10. **Access the Application**: Open a browser and go to `http://127.0.0.1:8000` to start using the Django expenses app.

</details>

### Create Application and Postgres DB on Heroku
<details>
<summary>Click to expand</summary>

1. **Sign Up or Log In to Heroku**:
    - Sign up at [Heroku's website](https://signup.heroku.com/) or log in if you already have an account.
2. **Create a New Application**:
    - Navigate to your Heroku dashboard.
    - Click on the "New" button and select "Create new app."
    - Enter a name for your application and select the region closest to your users.
    - Click on "Create app."
3. **Add a PostgreSQL Database**:
    - Go to the "Resources" tab in your Heroku dashboard.
    - In the "Add-ons" section, start typing "Heroku Postgres" and select it.
    - Choose the free "Hobby Dev" plan for development purposes.
    - Click "Submit Order Form" to add the PostgreSQL add-on to your application.
4. **Configure Environment Variables**:
    - Go to the "Settings" tab in your Heroku dashboard.
    - Under the "Config Vars" section, click on "Reveal Config Vars."
    - Add the necessary configuration variables such as `DJANGO_SECRET_KEY`, `DEBUG`, etc.
5. **Deploy Your Application**:
    - Connect your GitHub account under the "Deploy" tab by selecting "GitHub" as the deployment method.
    - Search for your repository and connect to it.
    - Enable Automatic Deploys or use the "Manual Deploy" section to deploy a specific branch.
6. **Run Migrations**:
    - After deploying, run your database migrations.
    - In the "More" dropdown menu, select "Run console."
    - Type `python manage.py migrate` and click "Run."
7. **Open Your App**: Click on the "Open app" button in the top right corner of the dashboard.

</details>

### Executing automated tests

### Final Deployment steps

## Credits 

### Code 

### Content 

### Media 

### Acknowledgments

I would like to express my gratitude to the Slack Community for their invaluable assistance. Stephen Seagrave for helping me throughout my coding. My mentor Brian Macharia.
