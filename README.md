
---

# Django Rest Framework Blog API

This project implements a simple Blog API using Django Rest Framework. It provides endpoints to manage blog posts, including functionalities for listing, creating, updating, and deleting posts. Additionally, the API supports pagination, filtering based on categories or tags, and requires authentication for access.

## Features

- **Blog Post Management**: Create, read, update, and delete blog posts via API endpoints.
- **Pagination**: Supports paginated responses for listing blog posts.
- **Filtering**: Allows filtering of blog posts based on categories or tags.
- **Authentication**: Requires token-based authentication for accessing the API endpoints.

## Setup Instructions

### Prerequisites

- Python (3.6 or higher)
- Django
- Django Rest Framework

### Installation

1. Clone the repository:

    ```bash
    git clone <https://github.com/shrey1010/codesis-Assignment->
    cd Django-Rest-Framework-Blog-API
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Create a superuser for authentication:

    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

### Usage

- **API Endpoints**:
    - `/api/posts/`: Endpoint for managing blog posts (requires authentication).
        - `GET`: List all blog posts.
        - `POST`: Create a new blog post.
    - `/api/posts/<post_id>/`: Endpoint to retrieve, update, or delete a specific blog post.
        - `GET`: Retrieve a single blog post.
        - `PUT`/`PATCH`: Update a blog post.
        - `DELETE`: Delete a blog post.
    - **Filtering**:
        - To filter by category: `/api/posts/?category=<category_name>`
        - To filter by tag: `/api/posts/?tag=<tag_name>`
    - **Authentication**:
        - Token-based authentication is required for accessing the API endpoints.
        - Obtain a token by logging in as a user and use it in the request headers: `Authorization: Token <token_value>`

### Running Tests

To run tests:

```bash
python manage.py test blog
```

The tests include cases for CRUD operations on blog posts, authentication, pagination, and filtering based on categories or tags.

## Contributors

- [Shrey Shukla](https://github.com/shrey1010)

---

Feel free to customize this README according to your specific project details, add deployment instructions, or include additional sections as needed.