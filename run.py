from flask import Flask
from flask_cors import CORS

from blueprints import img_manipulation_bp

app = Flask('cGANo')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.register_blueprint(img_manipulation_bp, url_prefix='/api/v1.0/img')

if __name__ == "__main__":
    app.run(debug=True)