from flask import Flask

# Create the Flask application instance
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    return "Welcome to the Digital Content Marketplace!"

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
