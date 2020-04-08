from app import app


@app.route('/')
def index():
    return "My Site-First Page"

