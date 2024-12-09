document.addEventListener('DOMContentLoaded', function() {
    fetch('../questions.json')
        .then(response => response.json())
        .then(data => {
            let currentQuestionIndex = 0;
            const questionElement = document.getElementById('question');
            const answerElements = [
                document.getElementById('answer1'),
                document.getElementById('answer2'),
                document.getElementById('answer3'),
                document.getElementById('answer4')
            ];
            const submitButton = document.getElementById('submit');

            function loadQuestion(questionIndex) {
                const questionData = data[questionIndex];
                questionElement.textContent = questionData.question;
                answerElements.forEach((element, index) => {
                    element.textContent = questionData.answers[index];
                    element.classList.remove('selected', 'correct', 'incorrect');
                    element.onclick = () => selectAnswer(index);
                });
            }

            function selectAnswer(selectedIndex) {
                answerElements.forEach(element => element.classList.remove('selected'));
                answerElements[selectedIndex].classList.add('selected');
            }

            submitButton.onclick = () => {
                const selectedAnswer = answerElements.findIndex(element => element.classList.contains('selected'));
                if (selectedAnswer === -1) {
                    alert('Please select an answer.');
                    return;
                }
                const correctAnswer = data[currentQuestionIndex].correct;
                if (selectedAnswer === correctAnswer) {
                    answerElements[selectedAnswer].classList.add('correct');
                    alert('Correct!');
                } else {
                    answerElements[selectedAnswer].classList.add('incorrect');
                    alert('Incorrect. The correct answer is ' + data[currentQuestionIndex].answers[correctAnswer] + '.');
                }
                currentQuestionIndex = (currentQuestionIndex + 1) % data.length;
                loadQuestion(currentQuestionIndex);
            };

            loadQuestion(currentQuestionIndex);
        })
        .catch(error => console.error('Error loading questions:', error));
});