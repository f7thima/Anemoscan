from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'secretkey'
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

users = {}  # Temporary in-memory storage
user_profile = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    if email in users and users[email] == password:
        return redirect(url_for('profile'))
    else:
        flash("You don't have an account or wrong password. Please create one.")
        return redirect(url_for('index'))

@app.route('/create_account')
def create_account():
    return render_template('create_account.html')

@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']
    users[email] = password
    return redirect(url_for('profile'))

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        user_profile['name'] = request.form['name']
        user_profile['gender'] = request.form['gender']
        user_profile['dob'] = request.form['dob']
        return redirect(url_for('camera'))
    return render_template('profile.html')

@app.route('/camera', methods=['GET', 'POST'])
def camera():
    if request.method == 'POST':
        file = request.files.get('image')
        if not file or file.filename == '':
            flash('No file chosen. Please select or take a photo.')
            return redirect(url_for('camera'))
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return redirect(url_for('result'))
    return render_template('camera.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)




