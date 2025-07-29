from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Create upload folder if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# 1️⃣ Load Page (Default homepage)
@app.route('/')
def load_page():
    return render_template('load.html')

# 2️⃣ Login Page (index.html)
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Dummy credentials
        if email == 'test@example.com' and password == 'pass':
            session['email'] = email
            return redirect(url_for('start'))
        else:
            error = 'Invalid credentials. Try again.'
    return render_template('index.html', error=error)

# 3️⃣ Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

# 4️⃣ Start Page
@app.route('/start')
def start():
    if 'email' not in session:
        return redirect(url_for('login'))
    return render_template('start.html')

# 5️⃣ Dashboard
@app.route('/dashboard')
def dashboard():
    if 'email' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

# 6️⃣ Result
@app.route('/result')
def result():
    if 'email' not in session:
        return redirect(url_for('login'))
    return render_template('result.html')

# 7️⃣ Profile
@app.route('/profile')
def profile():
    if 'email' not in session:
        return redirect(url_for('login'))
    return render_template('profile.html')

# 8️⃣ Camera
@app.route('/camera')
def camera():
    if 'email' not in session:
        return redirect(url_for('login'))
    return render_template('camera.html')

# 9️⃣ Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
