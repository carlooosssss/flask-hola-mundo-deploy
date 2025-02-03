from flask import Flask 
from dotenv import load_dotenv
import os

# load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    username = os.getenv('USER')
    password = os.getenv('PASSWORD')
    email = os.getenv('EMAIL')
    print(username, password, email)
    return 'MI PRIMERA APP DEPLOYEADA EN RENDER<br> {} {} {}'.format(username, password, email)


def status_404(error):
    return 'PAGE NOT FOUND ERROR 404'

if __name__ == '__main__':
    app.register_error_handler(404, status_404)
    app.run()