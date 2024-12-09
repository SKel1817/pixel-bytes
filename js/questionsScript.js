document.addEventListener('DOMContentLoaded', function () {
    let currentQuestionIndex = 0;

    const questionElement = document.getElementById('question');
    const answerElements = [
        document.getElementById('answer1'),
        document.getElementById('answer2'),
        document.getElementById('answer3'),
        document.getElementById('answer4')
    ];

    function loadQuestion(index) {
        if (index >= questions.length) {
            alert('No more questions available!');
            window.location.href = '../index.php';
            return;
        }

        const currentQuestion = questions[index];
        questionElement.textContent = currentQuestion.Question;
        answerElements.forEach((element, i) => {
            element.textContent = currentQuestion[`Answer${i + 1}`];
            element.className = ''; // Reset classes
        });
    }

    function selectAnswer(index) {
        answerElements.forEach((el, i) => {
            el.classList.toggle('selected', i === index - 1);
        });
        document.querySelector('#submit').dataset.selectedAnswer = index;
    }

    async function submitAnswer() {
        const selectedIndex = parseInt(document.querySelector('#submit').dataset.selectedAnswer, 10);
        if (!selectedIndex) {
            alert('Please select an answer.');
            return;
        }

        const currentQuestion = questions[currentQuestionIndex];
        if (selectedIndex === currentQuestion.Answer) {
            alert('Correct!');
            await makeApiCall(); // Call API for correct answers
            window.location.href = '../index.php'; // Redirect to the homepage
        } else {
            alert('Incorrect. Try the next question!');
            currentQuestionIndex++;
            loadQuestion(currentQuestionIndex); // Load the next question
        }
    }

    async function makeApiCall() {
        try {
            await fetch('https://example.com/api/endpoint', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ userId: 123, score: 1 }) // Replace with your logic
            });
        } catch (error) {
            console.error('Error making API call:', error);
        }
    }

    loadQuestion(currentQuestionIndex);
});
