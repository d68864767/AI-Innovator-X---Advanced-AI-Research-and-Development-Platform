# server.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import database
import model
import data_analysis
import collaboration
import simulation
import resources
import cloud_services
import ethics

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/model', methods=['POST'])
def create_model():
    data = request.get_json()
    result = model.create_model(data)
    return jsonify(result)

@app.route('/api/data_analysis', methods=['POST'])
def analyze_data():
    data = request.get_json()
    result = data_analysis.analyze(data)
    return jsonify(result)

@app.route('/api/collaboration', methods=['POST'])
def collaborate():
    data = request.get_json()
    result = collaboration.collaborate(data)
    return jsonify(result)

@app.route('/api/simulation', methods=['POST'])
def simulate():
    data = request.get_json()
    result = simulation.simulate(data)
    return jsonify(result)

@app.route('/api/resources', methods=['GET'])
def get_resources():
    result = resources.get_resources()
    return jsonify(result)

@app.route('/api/cloud_services', methods=['POST'])
def use_cloud_services():
    data = request.get_json()
    result = cloud_services.use(data)
    return jsonify(result)

@app.route('/api/ethics', methods=['POST'])
def check_ethics():
    data = request.get_json()
    result = ethics.check(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
