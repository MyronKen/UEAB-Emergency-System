document.addEventListener('DOMContentLoaded', () => {
    const emergencyBadge = document.querySelector('.emergency-badge');
    if (emergencyBadge) {
        emergencyBadge.addEventListener('click', makeCall);
    }
});

let device;

async function makeCall() {
    try {
        const response = await fetch('http://127.0.0.1:5000/communication/token');
        const data = await response.json();
        const token = data.token;

        device = new Twilio.Device(token);
        
        device.on('ready', () => {
            const params = {
                // Optional parameters to pass to the TwiML app
            };
            device.connect({ params });
            alert('Connecting to emergency services...');
        });

        device.on('error', (error) => {
            console.error('Twilio Device Error:', error);
            alert('Could not place the call. Please try again.');
        });

        device.on('disconnect', () => {
            alert('Call disconnected.');
        });

    } catch (error) {
        console.error('Error making call:', error);
        alert('Failed to initiate call. Please check your connection.');
    }
}