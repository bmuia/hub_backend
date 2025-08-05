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
---

### `/auth/register`

**Method:** POST
**Description:** Register a new user.

**Request Body:**

```json
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "password123"
}
```

**Response Body:**

```json
{
  "user": {
    "id": 1,
    "username": "testuser"
  },
  "refresh": "...",
  "access": "..."
}
```

---

### `/auth/login`

**Method:** POST
**Description:** Log in and receive JWT tokens.

**Request Body:**

```json
{
  "email": "test@example.com",
  "password": "password123"
}
```

**Response Body:**

```json
{
  "refresh": "...",
  "access": "...",
}
```

---

### `/auth/token/refresh`

**Method:** POST
**Description:** Refresh an access token using a refresh token.

**Request Body:**

```json
{
  "refresh": "..."
}
```

**Response Body:**

```json
{
  "access": "..."
}
```

---

### `/api/jokes/`

**Method:** GET
**Description:** Retrieve all jokes.

**Request Body:**
*None*

**Response Body:**

```json
[
  {
    "id": 1,
    "content": "Joke text",
    "category": "General"
  },
  ...
]
```

---

### `/api/jokes/create/`

**Method:** POST
**Description:** Create a new joke (**requires authentication**).

**Request Body:**

```json
{
  "content": "Why don't scientists trust atoms?",
  "category": "Science"
}
```

**Response Body:**

```json
{
  "id": 1,
  "content": "Why don't scientists trust atoms?",
  "category": "Science",
  "created_at": "..."
}
```

---

### `/api/likes/create/`

**Method:** POST
**Description:** Like a joke (**requires authentication**).

**Request Body:**

```json
{
  "joke": 1
}
```

**Response Body:**

```json
{
  "id": 1,
  "user": 1,
  "joke": 1,
  "is_liked": true,
  "created_at": "..."
}
```

---

### `/api/votes/create/`

**Method:** POST
**Description:** Upvote or downvote a joke (**requires authentication**).

**Request Body:**

```json
{
  "joke": 1,
  "vote_type": "upvote"
}
```

**Response Body:**

```json
{
  "id": 1,
  "user": 1,
  "joke": 1,
  "vote_type": "upvote",
  "created_at": "..."
}
```

---

### `/api/jokes/random/`

**Method:** GET
**Description:** Fetch and store a random joke from an external API (**requires authentication**).

**Request Body:**
*None*

**Response Body:**

```json
{
  "id": 1,
  "content": "...",
  "category": "...",
  "created_at": "..."
}
```
---
### `api/jokes/favurite`
**Method:** GET
**Description** Fetch jokes liked by the user / favourite
**Request Body**
*None*

**Response Body:**
```json
  {
    "id": 12,
    "content": "Why did the programmer quit his job? Because he didn't get arrays.",
    "category": "Programming",
    "created_at": "2025-08-05T08:30:00Z"
  },
  {
    "id": 15,
    "content": "I told my computer I needed a break, and it said 'No problem, I’ll go to sleep.'",
    "category": "Tech",
    "created_at": "2025-08-04T10:45:00Z"
  }
```
---

#### **Getting Started**

**Requirements:**

* Python 3.7+
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
