# Django Filters

A Django-based web application to manage a list of people with functionality to filter, search, and paginate through records.

Django Filters is a reusable Django application that allows developers to create user-friendly interfaces for filtering Django querysets. This application provides a powerful and flexible way to create custom filters that can be used to narrow down the results displayed on a webpage based on specific criteria defined by the user.

![Django Filters Snapshot](https://github.com/AflaxCade/Django-Filters/blob/main/Screenshot.PNG)

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Running the Project](#running-the-project)
- [Populating the Database with Fake Data](#populating-the-database-with-fake-data)
- [Technologies Used](#technologies-used)
- [License](#license)

## Features

- Filter and search by name, age, gender, and date created.
- Paginate results to manage large datasets.
- Bootstrap integration for responsive design.

## Installation

Follow these steps to get a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.x
- pip (Python package manager)
- virtualenv (Recommended for Python environments)

### Setup

1. **Clone the repository**

    ```bash
    git clone https://github.com/yourusername/django-person-management.git
    cd django-person-management
    ```

2. **Create and activate a virtual environment**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages**

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a superuser (optional, for admin access)**

    ```bash
    python manage.py createsuperuser
    ```

## Usage

1. **Run the development server**

    ```bash
    python manage.py runserver
    ```

2. **Access the application**

    Open your web browser and go to `http://127.0.0.1:8000/`.

3. **Admin Dashboard**

    Access the admin dashboard at `http://127.0.0.1:8000/admin/` using your superuser credentials.

## Running the Project

### Basic Usage

- The home page displays a list of people with filtering options.
- Use the form at the top to filter by ID, name, age, gender, and creation date.
- Pagination is available for navigating through large datasets.

## Populating the Database with Fake Data

To quickly populate the database with 100 fake `Person` records, use the custom Django management command:

1. **Run the populate command**

    ```bash
    python manage.py populate_people
    ```

This command uses the Faker library to create 100 random entries in the database.

## Technologies Used

- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Django Filters**: Used for creating filters for querysets in Django.
- **Faker**: A Python package that generates fake data for testing purposes.
- **Bootstrap**: A front-end framework for faster and easier web development.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
