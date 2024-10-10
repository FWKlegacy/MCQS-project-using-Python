from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define the quiz questions
questions = [
    {
        "question": "What is the powerhouse of the cell?",
        "options": ["Ribosome", "Nucleus", "Mitochondria", "Chloroplast"],
        "answer": "Mitochondria"
    },
    {
        "question": "What is the basic unit of life?",
        "options": ["Cell", "Tissue", "Organ", "Organism"],
        "answer": "Cell"
    },
    {
        "question": "Which organelle is responsible for photosynthesis?",
        "options": ["Mitochondria", "Chloroplast", "Ribosome", "Nucleus"],
        "answer": "Chloroplast"
    },
    {
        "question": "What is the process by which plants make their food?",
        "options": ["Respiration", "Digestion", "Photosynthesis", "Glycolysis"],
        "answer": "Photosynthesis"
    },
    {
        "question": "Which is the largest organ in the human body?",
        "options": ["Heart", "Brain", "Liver", "Skin"],
        "answer": "Skin"
    }
]

def get_comment(score_percentage):
    """
    Returns a comment based on the score percentage.
    """
    if score_percentage < 40:
        return "Poor"
    elif 40 <= score_percentage < 60:
        return "Average"
    elif 60 <= score_percentage < 75:
        return "Above Average"
    elif 75 <= score_percentage < 90:
        return "Good"
    else:
        return "Excellent"

@app.route('/', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # Collect answers from the form
        user_answers = request.form.to_dict()
        correct_answers = 0

        # Calculate score
        for i, question in enumerate(questions):
            user_answer = user_answers.get(f'question_{i}')
            if user_answer == question['answer']:
                correct_answers += 1

        score_percentage = (correct_answers / len(questions)) * 100
        comment = get_comment(score_percentage)

        # Pass the result to the result template
        return render_template('result.html', score=correct_answers, total=len(questions), percentage=score_percentage, comment=comment)
    
    # If GET request, show the quiz form
    return render_template('quiz.html', questions=questions)

if __name__ == '__main__':
    app.run(debug=True)


