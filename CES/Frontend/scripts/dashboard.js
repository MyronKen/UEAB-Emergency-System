document.addEventListener('DOMContentLoaded', function() {
    // Retrieve the user object from localStorage
    const userString = localStorage.getItem('user');

    if (userString) {
        const user = JSON.parse(userString);
        const userNameElement = document.getElementById('userName');
        const userAvatarElement = document.getElementById('userAvatar');

        if (userNameElement) {
            userNameElement.textContent = user.username;
        }

        if (userAvatarElement) {
            // Create initials for the avatar
            const initials = user.username.split(' ').map(n => n[0]).join('').toUpperCase();
            userAvatarElement.textContent = initials;
        }
    } else {
        // If no user data is found, redirect to the login page for security
        alert('You are not logged in. Redirecting to login page.');
        window.location.href = 'login.html';
    }

    // Logout functionality
    const logoutBtn = document.getElementById('logoutBtn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', function(e) {
            e.preventDefault();
            if (confirm('Are you sure you want to log out?')) {
                // Clear user data from localStorage
                localStorage.removeItem('user');
                // Redirect to login page
                window.location.href = 'login.html';
            }
        });
    }
});