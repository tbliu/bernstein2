from flask import Flask, request
from candidate import Candidate

app = Flask(__name__)

candidate = None
html = None
with open('search.html', 'r') as f:
    html = f.read()


@app.route('/search_candidate', methods=['POST'])
def user_input():
    candidate = Candidate(request.form['candidate_name'].upper())
    return str(candidate)


@app.route('/')
def main():
    return html

if __name__ == "__main__":
    app.run()
