from flask import Flask
from application import app

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')

