
from flask import Flask, render_template, request
from models import Question, QuizResult

app = Flask(__name__)

questions = [
    Question("Capital of Nigeria?", ["Abuja", "Lagos", "Kano"], "Abuja"),
    Question("2 + 2 = ?", ["3", "4", "5"], "4")
]

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        score = 0

        for i, q in enumerate(questions):
            answer = request.form.get(f"q{i}")
            if q.check_answer(answer):
                score += 1

        result = QuizResult(score)
        return render_template("result.html", result=result.get_result())

    return render_template("quiz.html", questions=questions)


if __name__ == "__main__":
    app.run(debug=True)