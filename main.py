"""Main module."""

from application import app

if __name__ == "__main__":
    app.run(debug=False)  # True only on dev env
