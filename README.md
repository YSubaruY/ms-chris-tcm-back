# ms-chris-tcm-back Api Rest
BookshopApiRest is a REST API based on Django 5 and its Rest-framework library, designed to provide a wide range of functionalities for an online bookstore. From publishing books to making purchases and interacting through comments, the API encompasses all essential features of a modern bookshop. With the use of JWT access tokens for authentication across all operations, comprehensive security for data and transactions is ensured.


## Key Features
- **Secure Authentication and Authorization:** Utilizes a JWT (JSON Web Tokens) system to enable users to securely perform designated functions. It allows for secure login and registration, ensuring the protection of users' data.
- **Advanced Functionalities for Administrators:** Administrators have access to various management functions, including overall book management. They can create, delete, edit, and update books, as well as manage associated comments.
- **User Comments on Books:** Users can leave comments on books available for sale, sharing their experiences and reviews. This encourages interaction and allows other users to make informed decisions about which books to purchase.
- **User Management Ease:** Simplifies user management, enabling administrators to efficiently manage user accounts. This includes functions such as creating, editing, and deleting user accounts, as well as managing permissions and roles.


## Documentation

The API is documented using Swagger, facilitating its understanding and use. 
Detailed documentation is available for all operations, easing integration with the frontend and subsequent deployment in production.

## Technologies Used

- Django: High-level Python web framework.
- Django REST Framework (DRF): Powerful toolkit for building web APIs.
- JSON Web Tokens (JWT): Mechanism used for authentication and authorization.
- Swagger / drf-yasg: Tools for API documentation.

## Installation and Usage

To install and use this project, follow these steps:

1. Clone this repository to your local machine.
2. Install dependencies using the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

3. Perform database migrations:

    ```bash
    python manage.py migrate
    ```

4. Start the development server:

    ```bash
    python manage.py runserver
    ```

5. Access the API documentation via the URL provided by Swagger or drf-yasg.


## License

This project is licensed under the MIT License. For more details, please read the [LICENSE](LICENSE) file.

## Contact

If you have any questions or comments about the project, feel free to contact us via [email](solisaullajuan@gmail.com) or by opening an issue in this repository.
