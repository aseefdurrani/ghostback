import os
from flask import Flask, jsonify
from flask_cors import CORS
from routes.videoProcessing import video_bp
from routes.handleWaitlist import waitlist_bp
from database import create_app

app = create_app()
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# Register the video processing blueprint
app.register_blueprint(video_bp, url_prefix='/api')
app.register_blueprint(waitlist_bp, url_prefix='/api')

# GET request TEST
@app.route('/api/home', methods=['GET'])
def hello_world():
    return jsonify({'message': 'helloworld'})  # Return "helloworld" as JSON

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
