document.addEventListener('DOMContentLoaded', () => {
    const panicBtn = document.getElementById('panicBtn');
    if (panicBtn) {
        panicBtn.addEventListener('click', () => {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(position => {
                    const { latitude, longitude } = position.coords;
                    sendPanicSignal(latitude, longitude);
                }, error => {
                    console.error('Error getting location:', error);
                    alert('Could not get your location. Sending alert without it.');
                    sendPanicSignal(null, null);
                });
            } else {
                console.error('Geolocation is not supported by this browser.');
                alert('Geolocation is not available. Sending alert without location.');
                sendPanicSignal(null, null);
            }
        });
    }
});

async function sendPanicSignal(latitude, longitude) {
    const userString = localStorage.getItem('user');
    if (!userString) {
        alert('You must be logged in to send a panic signal.');
        window.location.href = 'login.html';
        return;
    }

    const user = JSON.parse(userString);

    try {
        const response = await fetch('http://127.0.0.1:5000/emergency/panic', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                latitude,
                longitude,
                userId: user.id 
            })
        });

        const data = await response.json();

        if (response.ok) {
            alert('Emergency alert sent successfully!');
        } else {
            alert(`Error: ${data.message}`);
        }
    } catch (error) {
        console.error('Failed to send panic signal:', error);
        alert('Failed to send panic signal. Please check your connection and try again.');
    }
}