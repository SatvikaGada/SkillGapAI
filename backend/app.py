from flask import Flask
from database.models import db  # Import the db object from models.py

app = Flask(__name__)

# Configure your database URI (using SQLite here)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the app with the db
db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()

@app.route('/')
def hello():
    return 'Hello from SkillGapAI!'

if __name__ == '__main__':
    app.run(debug=True)
