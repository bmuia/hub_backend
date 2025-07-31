### **HUB API**

#### **Project Overview**

**HUB API** is an API that enables users to create, browse, and engage with user-generated jokes. Users can register, log in, submit their own jokes, and vote on others' contributions. The backend is built using Django and Django REST Framework, offering a secure and scalable architecture.

**Live Demo:** [https://hub-backend-qtb7.onrender.com](https://hub-backend-qtb7.onrender.com)

---

#### **Authors**

This project was collaboratively developed by:

* **Belam** – Implemented voting,like functionality for jokes and setup Jenkins.
* **Max** – Built the user authentication system, including registration and login.
* **Mark** – Developed the core joke creation features.

---

#### **API Endpoints**

The application follows RESTful design principles, offering the following API endpoints for user and joke management:

| Endpoint              | Method | Description                                              | Request (JSON)                                                                       | Response (JSON)                                                                      |
| :-------------------- | :----- | :------------------------------------------------------- | :----------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------- |
| `/auth/register`      | POST   | Register a new user.                                     | `{ "username": "testuser", "email": "test@example.com", "password": "password123" }` | `{ "user": { "id": 1, "username": "testuser" }, "refresh": "...", "access": "..." }` |
| `/auth/login`         | POST   | Log in and receive JWT tokens.                           | `{ "email": "test@example.com", "password": "password123" }`                         | `{ "refresh": "...", "access": "...", "user": { "id": 1, "username": "testuser" } }` |
| `/auth/token/refresh` | POST   | Refresh an access token using a refresh token.           | `{ "refresh": "..." }`                                                               | `{ "access": "..." }`                                                                |
| `/api/jokes/`         | GET    | Retrieve all jokes.                                      | —                                                                                    | `[ { "id": 1, "content": "Joke text", "category": "General" }, ... ]`                |
| `/api/jokes/create/`  | POST   | Create a new joke (**requires authentication**).         | `{ "content": "Why don't scientists trust atoms?", "category": "Science" }`          | `{ "id": 1, "content": "...", "category": "...", "created_at": "..." }`              |
| `/api/likes/create/`  | POST   | Like a joke (**requires authentication**).               | `{ "joke": 1 }`                                                                      | `{ "id": 1, "user": 1, "joke": 1, "is_liked": true, "created_at": "..." }`           |
| `/api/votes/create/`  | POST   | Upvote or downvote a joke (**requires authentication**). | `{ "joke": 1, "vote_type": "upvote" }`                                               | `{ "id": 1, "user": 1, "joke": 1, "vote_type": "upvote", "created_at": "..." }`      |
| `/api/jokes/random/`  | GET    | Fetch and store a random joke from an external API. (**requires authentication**)     | —                                                                                    | `{ "id": 1, "content": "...", "category": "...", "created_at": "..." }`              |

---

#### **Getting Started**

**Requirements:**

* Python 3.8+
* pip

**Setup Instructions:**

1. **Clone the repository:**

   ```bash
   git clone git@github.com:bmuia/hub_backend.git
   cd hub_backend
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

Once running, the API will be accessible at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
