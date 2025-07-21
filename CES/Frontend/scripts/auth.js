document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');

    if (loginForm) {
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            const response = await fetch('http://127.0.0.1:5000/auth/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ email, password })
            });

            const data = await response.json();

            if (response.ok) {
                localStorage.setItem('user', JSON.stringify(data.user));
                const userRole = data.user.role;
                switch (userRole) {
                    case 'admin':
                        window.location.href = 'dashboard_admin.html';
                        break;
                    case 'lecturer':
                        window.location.href = 'dashboard_lecturer.html';
                        break;
                    case 'responder':
                        window.location.href = 'dashboard_responder.html';
                        break;
                    case 'student':
                        window.location.href = 'dashboard_student.html';
                        break;
                    default:
                        // Fallback to dashboard if role is not recognized
                        window.location.href = 'index.html';
                }
            } else {
                alert(data.message);
            }
        });
    }

    if (registerForm) {
        registerForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const username = document.getElementById('username').value;
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            const role = document.getElementById('role').value;

            const response = await fetch('http://127.0.0.1:5000/auth/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username, email, password, role })
            });

            const data = await response.json();

            if (response.ok) {
                alert(data.message);
                window.location.href = 'login.html';
            } else {
                alert(data.message);
            }
        });
    }
});