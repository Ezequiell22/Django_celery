# Django Celery Integration

Welcome to the **Django Celery Integration** project! This repository demonstrates how to use Celery with Django to handle asynchronous tasks effectively, improving performance and scalability for web applications.

## Features

- **Asynchronous Task Management**: Offload time-consuming tasks to the background, ensuring a faster and more responsive user experience.
- **Celery Integration**: Set up Celery with Django to manage task queues seamlessly.
- **Example Tasks**: Includes examples of task creation, scheduling, and execution.

## Requirements

- Python 3.8+
- Django 4.x
- Celery 5.x
- RabbitMQ or Redis (as the message broker)

## Getting Started

Follow these steps to set up and run the project locally.

### 1. Clone the Repository

git clone https://github.com/Ezequiell22/Django_celery.git
cd Django_celery

### 2. Install Dependencies

Create a virtual environment and install the required Python packages:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

### 3. Configure Message Broker
Ensure that RabbitMQ or Redis is installed and running on your system. Update the Celery configuration in settings.py to point to your broker.

CELERY_BROKER_URL = 'pyamqp://guest@localhost///'

### 4. Start Celery Worker
Run the Celery worker in a terminal:
celery -A core worker --loglevel=info

### 5. Run the Django Server
Start the Django development server:

python manage.py runserver