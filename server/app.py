from flask import Flask
from models import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Create tables (run once)
with app.app_context():
    db.create_all()

@app.route('/')
def health_check():
    return "Well-being Tracking API is running!"

if __name__ == '__main__':
    app.run(debug=True)