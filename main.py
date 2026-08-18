# main.py
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'suhrob_premium_cinematic_portfolio_2026'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        print(f"\n=== NEW MESSAGE ===")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {message}")
        print("==================\n")
        
        flash('Thank you. Your message has been received.', 'success')
        return redirect(url_for('home'))
        
    return render_template('index.html')

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)