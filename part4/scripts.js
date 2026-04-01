document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');

    if (loginForm) {
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            try {
                const response = await fetch('http://127.0.0.1:5000/api/v1/login', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email, password })
                });

                if (response.ok) {
                    const data = await response.json();

                    // stocker token
                    document.cookie = `token=${data.access_token}; path=/`;

                    // redirection
                    window.location.href = 'index.html';
                } else {
                    alert('Login failed');
                }
            } catch (err) {
                console.error(err);
            }
        });
    }
});
function getCookie(name) {
    return document.cookie
        .split('; ')
        .find(row => row.startsWith(name))
        ?.split('=')[1];
}

async function fetchPlaces() {
    const token = getCookie('token');

    const response = await fetch('http://127.0.0.1:5000/api/v1/places', {
        headers: {
            'Authorization': `Bearer ${token}`
        }
    });

    const data = await response.json();
    displayPlaces(data);
}

function displayPlaces(places) {
    const container = document.getElementById('places-list');
    container.innerHTML = '';

    places.forEach(place => {
        const div = document.createElement('div');
        div.className = 'place-card';

        div.innerHTML = `
            <h3>${place.title}</h3>
            <p>Price: ${place.price}</p>
            <a href="place.html?id=${place.id}">
                <button class="details-button">View</button>
            </a>
        `;

        container.appendChild(div);
    });
}

document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('places-list')) {
        f
