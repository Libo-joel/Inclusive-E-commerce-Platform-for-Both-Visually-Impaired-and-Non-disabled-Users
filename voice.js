window.onload = function () {
    const emailInput = document.getElementById('email');
    if (emailInput) {
        emailInput.focus();
        speak("Please enter your email ID.");
    }

    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'en-IN';
    recognition.interimResults = false;

    // Optional voice button
    const voiceBtn = document.getElementById('voice-btn');
    if (voiceBtn) {
        voiceBtn.addEventListener('click', () => {
            recognition.start();
        });
    }

    recognition.onresult = function (event) {
        const result = event.results[0][0].transcript;
        if (emailInput) {
            emailInput.value = result;
            speak("Email received: " + result);
        }
    };

    recognition.onerror = function () {
        speak("Sorry, I didn't get that.");
    };
};

function speak(message) {
    const utterance = new SpeechSynthesisUtterance(message);
    utterance.lang = 'en-IN';
    window.speechSynthesis.speak(utterance);
}
