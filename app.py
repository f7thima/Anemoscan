from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        age = request.form['age']
        return redirect(url_for('dashboard'))
    return render_template('profile.html')

@app.route('/camera')
def camera():
    return render_template('camera.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' in request.files:
        image = request.files['image']
        if image.filename != '':
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
            # You can add ML prediction here later
            result = "Possible symptoms detected"
            return render_template('result.html', result=result)
    return redirect(url_for('camera'))

@app.route('/result')
def result():
    return render_template('result.html', result="Upload an image first")

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)



