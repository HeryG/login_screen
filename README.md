# login_screen
This is a simple login and registration application built using Python and the Tkinter library for the graphical user interface (GUI).

<h2>Features</h2>

User Registration

1. Users can register for a new account by providing a unique username and a password.
The application ensures that the password provided meets a minimum length requirement (currently set to 3 characters).
Upon successful registration, users receive a confirmation message.
User Login:

2. Registered users can login using their username and password.
If the provided credentials are correct, users receive a login success message.
If the provided credentials are incorrect, users receive a notification indicating either a wrong password or that the user does not exist.
Feedback Messages

3. The application provides feedback messages in case of errors such as wrong password, user not found, existing username, or weak password.
These messages are displayed in separate pop-up windows.

<h2>Prerequisites</h2>

Python 3.11 installed on your system.
Required Python packages:
psycopg2: PostgreSQL adapter for Python.
customtkinter: A custom Tkinter library for creating GUI elements.

<h2>Installation</h2>

1. Install Python if not already installed. You can download it from the official Python website: https://www.python.org/downloads/

2. Install the required Python packages using pip:
   
      `pip install psycopg2 customtkinter`

3. Set up a PostgreSQL database:

4. Ensure that you have PostgreSQL installed on your system.
Create a new database.
Modify the database connection parameters in the code (hostname, database, user_db, pwd, port_id) to match your PostgreSQL setup.

   `hostname = "localhost"`
   `database = ""`
   `user_db = ""`
   `pwd = ""`
   `port_id = 5432`
<h2>Usage</h2>
1. Run the application by executing the script login_screen.py:

   `python login_screen.py`

2. The main screen will appear, providing options to either login or register for a new account.

3. Click on the "Register" button to create a new account. Enter a unique username and password, then click "Register".

4. Once registered, you can use the "Login" button to access your account. Enter your username and password, then click "Login".

5. Depending on the input, you will receive appropriate feedback messages in pop-up windows.

6. Close the application window when done.
