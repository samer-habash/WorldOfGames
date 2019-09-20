from flask import Flask, render_template
from Utils import SCORES_FILE_NAME
import os
import time

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def score_server():
    with open(SCORES_FILE_NAME, 'r') as f:
        if os.path.exists(SCORES_FILE_NAME) and os.path.getsize(SCORES_FILE_NAME) > 0:
            SCORE = int(f.read())
            return render_template('Score.html', SCORE=SCORE, reload=time.time())
        else:
            SCORE = 0
            return render_template('Score.html', SCORE=SCORE, reload=time.time())

os.environ["FLASK_APP"] = "MainScores.py"

if __name__ == "__main__":
    app.run(debug=True)

