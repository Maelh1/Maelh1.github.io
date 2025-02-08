function openLetter() {
    const envelope = document.querySelector('.envelope');
    envelope.classList.add('open');
}

function handleResponse(response) {
    const fireworks = document.getElementById('fireworks');
    const errorMessage = document.getElementById('errorMessage');

    if (response === 'yes') {
        fireworks.classList.remove('hidden');
        errorMessage.classList.add('hidden');
    } else if (response === 'no') {
        errorMessage.classList.remove('hidden');
        fireworks.classList.add('hidden');
    }
}