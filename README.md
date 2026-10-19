Library Management System API
A RESTful API for a Library Management System built with Django and Django REST Framework (DRF). The project implements role-based access control, JWT authentication, full CRUD operations, and customized admin panel features.
Project Implementation Summary
1. Completed Tasks (Fully Implemented)
 Task 1: Database Models & Relationships
 Implemented Author, Category, and Book models with proper one-to-many ForeignKey relationships.  
 Added constraints: unique isbn validation, non-negative available_copies, and proper str() representations.  
 Successfully created and applied database migrations.  
 Task 2: Django Admin Panel
 Registered all models (Book, Author, Category).  
 Customized the Book admin interface using list_display, search_fields (title, ISBN), and list_filter (author, category, published date).  
 Created a superuser and verified admin CRUD actions.  
 Task 3: Serializers & Validation
 Built BookSerializer, AuthorSerializer, CategorySerializer, and RegisterSerializer using ModelSerializer.  
 Configured nested serializers to represent full author and category details on read operations while accepting primary keys on creation.  
 Enforced secure password hashing using create_user during user registration.  
 Task 4: Views & RESTful Endpoints
 Implemented full CRUD operations for Books, Authors, and Categories using DRF ViewSets / Generic Views.  
 Added search functionality (by title, ISBN) and filtering (by author, category) using django-filter and filters.SearchFilter.  
 Configured proper HTTP response codes (200 OK, 201 Created, 204 No Content, 400 Bad Request, 404 Not Found).  
 Task 5: Authentication & Authorization (JWT)
 Integrated djangorestframework-simplejwt for authentication.  
 Implemented endpoints for user registration, JWT login (access and refresh token generation), and token refresh.  
 Configured role-based access control:
 Guests / Regular Users: Read-only permissions (GET requests).  
 Administrators: Full write access (POST, PUT, PATCH, DELETE).  
2. Testing & Verification
 Browsable API & JWT Testing: Verified user authentication, login token retrieval (HTTP 200 OK), and token lifecycle.
 Admin Verification: Tested book, author, and category management through Django Admin.  
 Documentation: Attached screenshots verifying token generation and endpoint execution in the repository.
3. Bonus Tasks Status (Optional)
 Optional Features (e.g., Borrowing history, Swagger docs): Not included in this milestone to ensure complete and robust compliance with all mandatory core requirements.
Installation & Setup Instructions
1. Clone the Repository:
git clone https://github.com/ritaj-althobaiti/LibraryProject.git
cd LibraryProject
2. Create and Activate Virtual Environment:
python -m venv .venv
.venv\Scripts\activate
3. Install Dependencies:
pip install -r requirements.txt
4. Database Migrations:
python manage.py makemigrations
python manage.py migrate
5. Create Superuser (Admin):
python manage.py createsuperuser
6. Run the Development Server:
python manage.py runserver
The API will be available at: http://127.0.0.1:8000/
API Endpoints
Authentication (/api/auth/)
 POST /api/auth/register/ : Register a new user (Public)
 POST /api/auth/login/ : Obtain JWT token pair (Access/Refresh) (Public)
 POST /api/auth/token/refresh/ : Refresh expired access token (Public)
 GET /api/auth/profile/ : Retrieve authenticated user profile (Authenticated User)
Books (/api/books/)
 GET /api/books/ : List all books (Public)
 GET /api/books/{id}/ : Retrieve a single book (Public)
 POST /api/books/ : Create a new book (Admin Only)
 PUT/PATCH /api/books/{id}/ : Update a book (Admin Only)
 DELETE /api/books/{id}/ : Delete a book (Admin Only)
Authors & Categories
 Authors: /api/authors/ (GET: Public, POST/PUT/DELETE: Admin)
 Categories: /api/categories/ (GET: Public, POST/PUT/DELETE: Admin)
