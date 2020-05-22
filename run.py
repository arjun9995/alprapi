from app import app
from db import fun

db.init_app(app)

@app.before_first_request
def create_tables():
    fun()
