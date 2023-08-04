# ClubApp

ClubApp is a web application that enables club members to create and manage tasks and subtasks associated with their clubs. It provides a platform for users to collaborate, set deadlines, and specify social media platforms for each task.
## Demo


https://github.com/tarun-hegde/Social-Media-Task-Organizer/assets/101446457/9590ea42-8a86-4eac-a57b-2b099ce0f58c




## Requirements

- Python 3.x
- Django (see requirements.txt for specific versions of dependencies)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/tarun-hegde/Social-Media-Task-Organizer.git
   ```

2. Create and activate a virtual environment:

   ```bash
   virtualenv venv
   source venv/bin/activate
   ```

3. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Access the application locally at `http://localhost:8000`.

## Usage

- Visit the home page to register a new account or login if you already have one.
- After logging in, you will be directed to the dashboard where you can view and manage tasks associated with your club.
- To create a new task, click on the "Create Task" button and provide the necessary details such as the task title, description, deadline, and social media platform.
- Once a task is created, it will be listed in the dashboard with its details displayed, including the assigned deadline and social media platform.
- To delete a task, click on the "Delete" button next to the task you want to remove. Confirm the deletion when prompted.
- For each task, you can also add subtasks by clicking on the "Add Subtask" button. Specify the subtask details such as title, description, and any additional information.
- Subtasks will be displayed under their respective parent tasks in the dashboard.

## Features

- User registration and login with authentication.
- Dashboard displaying club-specific tasks and subtasks.
- Create, view, and delete tasks with associated details such as title, description, deadline, and social media platform.
- Add subtasks to tasks, providing additional details and descriptions.
- Deadline tracking for tasks and subtasks.
- Responsive design for seamless usage across different devices.

## Contributing

Contributions are welcome! If you'd like to contribute to ClubApp, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make the necessary changes and commit them.
4. Push your branch to your forked repository.
5. Submit a pull request with a description of your changes.






