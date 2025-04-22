from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, I'm [Your Name]!</h1><p>My first Python web app in AWS!</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

