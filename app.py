from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from rq_config import q
from tasks import process_url

app = Flask(__name__)
CORS(app)  

@app.route('/upload', methods=['POST'])
def upload():
    data = request.json
    if 'dataUrl' not in data:
        return jsonify({'error': 'No URL provided'}), 400

    result = q.enqueue(process_url, data)
    return jsonify({'message': 'Task enqueued successfully', 'job_id': result.id}), 200

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


