
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/slice', methods=['POST'])
def slice_email():
    email = request.form['email']
    try:
        username, domain = email.split('@')
        return render_template('index.html', username=username, domain=domain, email=email)
    except ValueError:
        return render_template('index.html', error="Invalid email format. Please enter a valid email.")

if __name__ == '__main__':
    app.run(debug=True)
