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

### Overview
The Django Expense Organizer project was created to offer a user-friendly and secure way to manage personal expenses. It aims to streamline tracking daily financial activities and includes advanced features like Google OAuth integration and AI-driven expense descriptions.

This app is designed for anyone looking to take control of their finances and better understand their spending habits. By centralizing expense recording and analysis, it helps users make informed financial decisions and achieve their financial goals.

### User Stories:

- As a user, I would like to know when I reach a page I don't have access to.
- As a user, I would like to log in so that I can access my account.
- As a user, I would like to register for a new account so that I can create my profile and start managing my expenses.
- As a user, I would like the ability to add an expense to keep track of my expenses.
- As a user, I want the ability to view my expenses.
- As a user, I want the ability to edit my expenses.
- As a user, I want the ability to delete an expense.
- As a user, I would like to log out of my account.

### Developer Tasks:

- As a developer, I need to create a readme file.
- As a developer, I need to set up my project.
- As a developer, I need to deploy my project to Heroku.
- As a developer, I need to create a base HTML page and structure.
- As a developer, I need to Integrate Google authentication.


### Agile

The Agile methodology was employed to plan and manage the development of the Django Expense Organizer project. GitHub was used as the primary tool to demonstrate the Agile approach.

User Stories were then created as GitHub Issues, linked to the Epics. Custom issue templates were used to ensure consistency and clarity in describing the User Stories. Each User Story followed a specific format, including a title, description.

A link to my Kanban board can be found [here](https://github.com/users/nathan-cool/projects/2/views/1?pane=issue&itemId=55533266)

![image](https://github.com/nathan-cool/django-expense-organizer/assets/127421398/035d6f2e-927e-4062-8ffd-3d0639c2d248)



## Features

### Existing Features

#### Authentication System and security 

- **Registration System**: Allows users to create a new account by providing their name, email, and password. The registration view splits the user's name into first and last names, validates the provided information, and if valid, sends a verification email to activate the account.

- **Login System**: Users can log in to their account using their email and password. The system checks if the account is active and has correct credentials before granting access.

- **Logout System**: Logged-in users can log out of their account, which redirects them to the login page with a success message.

- **Google OAuth Integration**: Users have the option to authenticate using Google, simplifying the login process without the need for a password.

- **Email Validation**: Validates emails in real-time during registration to ensure they are not already in use and follow the correct format.

- **Password Validation**: Checks password strength to ensure it meets the required criteria for security.

- **Account Verification**: After registration, users receive an email with a link to verify their account, ensuring the email address belongs to them.

To restrict access to certain views and features, the Django @login_required decorator is used. This ensures that only registered and authenticated users can access these views. If an unauthenticated user tries to reach these views, they will be redirected to the login page.

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

## Design

#### **Colour Scheme**

- `#FFFFFF` ![Colour](place) - Primary background color for pages, offering a bright and clean canvas.
- `#333533` ![Colour](place) - Main text and primary elements color, providing a stark, readable contrast.
- `#712cf9` ![Colour](place) - Accent colour for buttons and interactive elements, adding vibrancy and emphasis.
- `#202020` ![Colour](place) - Hover states for buttons, deepening the visual interaction feedback.
- `#1f7c4d` ![Colour](place) - Success messages and confirmations, associating with positive actions.
- `#5a23c8` ![Colour](place) - Shadows to enriching the depth of design elements.
- `#ffffff` ![Colour](place) - Background colour for the authentication area, patterned using a design from [MagicPattern](https://www.magicpattern.design/tools/css-backgrounds), specifically the radial gradient of black and white, enhancing the visual appeal while maintaining functional simplicity.



## Planning

## Technologies Used

### Languages Used

#### Python
- **Python 3**: The core backend programming language used for the application. Django, a high-level Python web framework, is employed to handle backend logic, database operations, and application routing.

#### HTML5
- **HTML5**: Used for structuring the web pages of the application. HTML5 is the latest standard, offering a wide range of features for web documents.

#### CSS3
- **CSS3**: Used to style the HTML content. CSS3 provides a variety of styling options through selectors, properties, and values to create responsive and visually appealing web pages.

#### JavaScript
- **JavaScript**: Employed for adding interactive behaviors to web pages. JavaScript is used sparingly to enhance user interfaces and improve user experience, for instance, in form validations and dynamic content updates.

### Frameworks, Libraries & Programs Used

#### Django
- A high-level Python web framework used for developing the web application.
- Provides a robust set of tools and features for building scalable and maintainable web applications.
- The code uses various Django components such as views, models, authentication, and URL routing.

#### Python Standard Library
- Several modules from the Python standard library are used, including:
 - `os`: Used for interacting with the operating system.
 - `json`: Used for working with JSON data.
 - `re`: Used for regular expression matching and validation.

#### dotenv
- A Python library used for loading environment variables from a `.env` file.
- Allows sensitive information, such as API keys, to be stored securely outside of the codebase.

#### OpenAI
- The OpenAI API is used to generate descriptions for expenses using the ChatCompletion model.
- Requires an OpenAI API key to be set in the environment variables.

#### Google OAuth
- Functionality for Google OAuth authentication is included.
- Uses the `google-auth` library to verify the OAuth token and retrieve user data.

#### JSON Web Tokens (JWT)
- The `jwt` library is used for working with JSON Web Tokens.
- Likely used for authentication and authorization purposes.

#### Django Messages Framework
- Used to display success and error messages to the user.
- Provides a convenient way to store and retrieve messages across requests.

#### Django Authentication System
- The built-in Django authentication system is utilized for user registration, login, and logout functionality.
- Uses the `User` model provided by Django to store user information.

#### Django Email
- Django's email functionality is used to send verification emails to users during the registration process.
- Utilizes the `EmailMessage` class from `django.core.mail` to compose and send emails.

### Software & Web Applications Used

#### Git
- Git is used for version control and collaboration among developers.
- It allows tracking changes in the codebase, creating branches for feature development, and merging changes back into the main branch.

#### GitHub
- GitHub is a web-based platform for hosting Git repositories.
- It provides a centralized location for storing and managing the project's source code.
- GitHub also offers features like issue tracking, pull requests, and project documentation.

#### Visual Studio Code
- Visual Studio Code is a lightweight and extensible code editor used for developing the application.
- It provides a rich set of features and extensions for Python development, including syntax highlighting, code completion, and debugging support.

#### Heroku
- Heroku is a cloud platform used for deploying and hosting the web application.
- It provides a seamless way to deploy Django applications and manages the infrastructure and scaling of the application.

#### PostgreSQL
- PostgreSQL is a powerful and open-source relational database management system.
- It is used as the primary database for storing application data, including user information, expenses, and categories.

#### Google Fonts
- Google Fonts is a library of free and open-source fonts used for typography in the application.
- It provides a wide range of font styles and weights to enhance the visual appeal of the application.

#### Balsamiq
- Balsamiq is a user interface (UI) wireframing tool used for creating mockups and prototypes of the application's user interface.
- It helps in visualizing and iterating on the design before implementing it in code.

#### Draw.io
- Draw.io is a diagramming and flowcharting tool used for creating visual representations of the application's architecture and user flows.
- It helps in documenting and communicating complex systems and processes.

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

1. **Sign Up or Log In to Heroku**:
    - If you do not already have a Heroku account, go to [Heroku's website](https://signup.heroku.com/) to sign up.
    - If you have an account, simply log in.

2. **Create a New Application**:
    - Navigate to your Heroku dashboard.
    - Click on the "New" button in the top right corner, then select "Create new app."
    - Enter a name for your application. It must be unique across all Heroku apps.
    - Select the region closest to your users to minimize latency.
    - Click on "Create app."

3. **Add a PostgreSQL Database**:
    - Once your app is created, go to the "Resources" tab in your Heroku dashboard.
    - In the "Add-ons" section, start typing "Heroku Postgres" in the search box, then select it when it appears.
    - Choose a plan. For development purposes, you can select the free "Hobby Dev" plan.
    - Click "Submit Order Form" to add the PostgreSQL add-on to your application.

4. **Configure Environment Variables**:
    - Go to the "Settings" tab in your Heroku dashboard.
    - Under the "Config Vars" section, click on "Reveal Config Vars."
    - Enter the necessary configuration variables such as `DJANGO_SECRET_KEY`, `DEBUG`, and any other variables your app requires. For example:
      - Key: `DJANGO_SECRET_KEY`, Value: `<your_secret_key>`
      - Key: `DEBUG`, Value: `False`

5. **Deploy Your Application**:
    - Connect your GitHub account under the "Deploy" tab by selecting "GitHub" as the deployment method.
    - Search for your repository and connect to it.
    - Enable Automatic Deploys for automatic deployment when you push to your repository, or use the "Manual Deploy" section to deploy a specific branch.

6. **Run Migrations**:
    - After deploying, you need to run your database migrations.
    - In the "More" dropdown menu at the top right corner of your application dashboard, select "Run console."
    - Type `python manage.py migrate` and click "Run" to execute the migrations.

7. **Open Your App**:
    - You can open your application by clicking on the "Open app" button in the top right corner of the dashboard.

By following these steps, you can set up and deploy your Django Expenses app on Heroku using the web interface.

### Executing automated tests

### Final Deployment steps

## Credits 

### Code 

### Content 

### Media 

### Acknowledgments

I would like to express my gratitude to the Slack Community for their invaluable assistance. Stephen Seagrave for helping me throughout my coding. My mentor Brian Macharia.
