# API Documentation

## Base URL
All API endpoints are prefixed with `/api`.

---

## Authentication

### 1. Register a New User
*   **Endpoint:** `POST /auth/register`
*   **Description:** Creates a new user account.
*   **Request Body:**
    ```json
    {
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123",
        "role": "student"
    }
    ```
*   **Success Response (201):**
    ```json
    {
        "message": "User registered successfully"
    }
    ```

### 2. Log In
*   **Endpoint:** `POST /auth/login`
*   **Description:** Authenticates a user and returns their data.
*   **Request Body:**
    ```json
    {
        "email": "test@example.com",
        "password": "password123"
    }
    ```
*   **Success Response (200):**
    ```json
    {
        "message": "Login successful",
        "user": {
            "username": "testuser",
            "email": "test@example.com",
            "role": "student"
        }
    }
    ```
*   **Error Response (401):**
    ```json
    {
        "message": "Invalid credentials"
    }
    ```

### 3. Log Out
*   **Endpoint:** `POST /auth/logout`
*   **Description:** Logs the current user out.
*   **Success Response (200):**
    ```json
    {
        "message": "Logout successful"
    }
    ```

### 4. Forgot Password
*   **Endpoint:** `POST /auth/forgot_password`
*   **Description:** Initiates the password reset process.
*   **Request Body:**
    ```json
    {
        "email": "test@example.com"
    }
    ```
*   **Success Response (200):**
    ```json
    {
        "message": "If an account with that email exists, a password reset link has been sent."
    }
    ```

---

## User

### 1. Get User Dashboard
*   **Endpoint:** `GET /user/dashboard`
*   **Description:** Retrieves dashboard information for the currently logged-in user.
*   **Authentication:** Requires the user to be logged in.
*   **Success Response (200):**
    ```json
    {
        "id": 1,
        "username": "testuser",
        "email": "test@example.com",
        "role": "student",
        "responder_type": null,
        "last_heartbeat": "2023-10-27T10:00:00Z",
        "phone_number": "1234567890"
    }