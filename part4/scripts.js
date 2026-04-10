// ─── UTILS ────────────────────────────────────────────────────────────────────

function getCookie(name) {
    return document.cookie
        .split('; ')
        .find(row => row.startsWith(name + '='))
        ?.split('=')[1];
}

function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('id');
}

// ─── LOGIN ────────────────────────────────────────────────────────────────────

document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');

    if (loginForm && document.title.includes('Login')) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            const errorMsg = document.getElementById('error-msg');
            if (errorMsg) errorMsg.style.display = 'none';

            await loginUser(email, password);
        });
    }
});

async function loginUser(email, password) {
    const errorMsg = document.getElementById('error-msg');

    try {
        const response = await fetch('http://127.0.0.1:5000/api/v1/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });

        if (response.ok) {
            const data = await response.json();
            document.cookie = `token=${data.access_token}; path=/`;
            window.location.href = 'index.html';
        } else {
            if (errorMsg) errorMsg.style.display = 'block';
        }
    } catch (err) {
        if (errorMsg) errorMsg.style.display = 'block';
        console.error(err);
    }
}

// ─── INDEX ────────────────────────────────────────────────────────────────────

document.addEventListener('DOMContentLoaded', () => {
    if (!document.getElementById('places-list')) return;

    checkAuthentication();

    document.getElementById('price-filter').addEventListener('change', (event) => {
        const selected = event.target.value;
        const cards = document.querySelectorAll('.place-card');

        cards.forEach(card => {
            const price = parseFloat(card.dataset.price);
            if (selected === 'all' || price <= parseFloat(selected)) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    });
});

function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');

    if (!token) {
        if (loginLink) loginLink.style.display = 'block';
    } else {
        if (loginLink) loginLink.style.display = 'none';
        fetchPlaces(token);
    }
}

async function fetchPlaces(token) {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/v1/places', {
            headers: { 'Authorization': `Bearer ${token}` }
        });

        if (!response.ok) throw new Error('Failed to fetch places');

        const places = await response.json();
        displayPlaces(places);
    } catch (err) {
        console.error(err);
        document.getElementById('places-list').innerHTML = '<p>Error loading places.</p>';
    }
}

function displayPlaces(places) {
    const container = document.getElementById('places-list');
    container.innerHTML = '';

    if (places.length === 0) {
        container.innerHTML = '<p>No places available.</p>';
        return;
    }

    places.forEach(place => {
        const div = document.createElement('div');
        div.className = 'place-card';
        div.dataset.price = place.price;

        div.innerHTML = `
            <h3>${place.title}</h3>
            <p class="price">${place.price}€ / night</p>
            <a href="place.html?id=${place.id}">
                <button class="details-button">View Details</button>
            </a>
        `;

        container.appendChild(div);
    });
}

// ─── PLACE DETAILS ────────────────────────────────────────────────────────────

document.addEventListener('DOMContentLoaded', () => {
    const placeDetails = document.getElementById('place-details');
    if (!placeDetails) return;

    const token = getCookie('token');
    const placeId = getPlaceIdFromURL();
    const addReviewSection = document.getElementById('add-review');

    // Afficher section review si connecté
    if (!token) {
        if (addReviewSection) addReviewSection.style.display = 'none';
        const loginLink = document.getElementById('login-link');
        if (loginLink) loginLink.style.display = 'block';
    } else {
        if (addReviewSection) addReviewSection.style.display = 'block';
        const loginLink = document.getElementById('login-link');
        if (loginLink) loginLink.style.display = 'none';
    }

    if (!placeId) {
        placeDetails.innerHTML = '<p>Place not found.</p>';
        return;
    }

    fetchPlaceDetails(token, placeId);

    // Formulaire inline sur place.html
    const reviewForm = document.getElementById('review-form');
    if (reviewForm) {
        reviewForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const text = document.getElementById('review-text').value;
            const rating = parseInt(document.getElementById('rating').value);
            await submitReview(token, placeId, text, rating);
        });
    }
});

async function fetchPlaceDetails(token, placeId) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}`, {
            headers: { 'Authorization': `Bearer ${token}` }
        });

        if (!response.ok) throw new Error('Failed to fetch place details');

        const place = await response.json();
        displayPlaceDetails(place);
    } catch (err) {
        console.error(err);
        document.getElementById('place-details').innerHTML = '<p>Error loading place.</p>';
    }
}

function displayPlaceDetails(place) {
    const container = document.getElementById('place-details');
    container.innerHTML = `
        <div class="place-info">
            <h1>${place.title}</h1>
            <p><strong>Price:</strong> ${place.price}€ / night</p>
            <p><strong>Location:</strong> ${place.latitude ?? '—'}, ${place.longitude ?? '—'}</p>
            <p class="place-description">${place.description || 'No description available.'}</p>
        </div>
        <h2>Reviews</h2>
        <div id="reviews-list"></div>
    `;

    // Charger les reviews
    const token = getCookie('token');
    fetch('http://127.0.0.1:5000/api/v1/reviews', {
        headers: { 'Authorization': `Bearer ${token}` }
    })
    .then(res => res.json())
    .then(reviews => {
        const reviewsList = document.getElementById('reviews-list');
        const placeReviews = reviews.filter(r => r.place_id === place.id);

        if (placeReviews.length === 0) {
            reviewsList.innerHTML = '<p>No reviews yet.</p>';
            return;
        }

        placeReviews.forEach(review => {
            const div = document.createElement('div');
            div.className = 'review-card';
            div.innerHTML = `
                <p>${review.text}</p>
                <p><strong>Rating:</strong> ${'★'.repeat(review.rating)}${'☆'.repeat(5 - review.rating)} (${review.rating}/5)</p>
            `;
            reviewsList.appendChild(div);
        });
    })
    .catch(err => console.error(err));
}

// ─── ADD REVIEW ───────────────────────────────────────────────────────────────

document.addEventListener('DOMContentLoaded', () => {
    const reviewForm = document.getElementById('review-form');
    if (!reviewForm || !document.title.includes('Add Review')) return;

    const token = checkAuthenticationReview();
    const placeId = getPlaceIdFromURL();

    reviewForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const text = document.getElementById('review-text').value;
        const rating = parseInt(document.getElementById('rating').value);
        await submitReview(token, placeId, text, rating);
    });
});

function checkAuthenticationReview() {
    const token = getCookie('token');
    if (!token) {
        window.location.href = 'index.html';
        return null;
    }
    return token;
}

async function submitReview(token, placeId, text, rating) {
    const successMsg = document.getElementById('success-msg');
    const errorMsg = document.getElementById('error-msg');

    if (successMsg) successMsg.style.display = 'none';
    if (errorMsg) errorMsg.style.display = 'none';

    try {
        const response = await fetch('http://127.0.0.1:5000/api/v1/reviews', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ text, rating, place_id: placeId })
        });

        handleResponse(response, placeId);
    } catch (err) {
        if (errorMsg) errorMsg.style.display = 'block';
        console.error(err);
    }
}

function handleResponse(response, placeId) {
    const successMsg = document.getElementById('success-msg');
    const errorMsg = document.getElementById('error-msg');

    if (response.ok) {
        if (successMsg) successMsg.style.display = 'block';
        document.getElementById('review-text').value = '';
        setTimeout(() => {
            if (placeId) window.location.href = `place.html?id=${placeId}`;
        }, 1500);
    } else {
        if (errorMsg) errorMsg.style.display = 'block';
    }
}
