# Django Chatbot

Django Chatbot is a simple chatbot application built using Django, powered by the scikit-learn library. It allows you to set up questions and answers using the Django admin panel, making it easy to customize responses for your chatbot.

## Features

- **Admin Panel Interface**: Set up chatbot responses and manage questions and answers via the Django admin panel.

- **Scikit-Learn Integration**: Utilizes scikit-learn's machine learning capabilities to understand and respond to user queries.

## Installation

To get started with this Django chatbot project, follow these installation steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/django-chatbot.git
   cd django-chatbot
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Apply database migrations:

bash
Copy code
python manage.py migrate
Create a superuser to access the Django admin panel:

bash
Copy code
python manage.py createsuperuser
Start the development server:

bash
Copy code
python manage.py runserver
The application should now be accessible at http://localhost:8000/ and the admin panel at http://localhost:8000/admin/.

Usage
Access the Django admin panel by logging in with the superuser credentials created earlier.

Navigate to the "Chatbot" section and start adding questions and their corresponding answers.
