import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check_coverage', methods=['POST'])
def check_coverage():
    data = request.json
    target = data['target']
    regions = data['regions']
    covered = is_covered(target, regions)
    return jsonify({'covered': covered})

def is_covered(target, regions):
    tx1, ty1, tx2, ty2 = min(target['x1'], target['x2']), min(target['y1'], target['y2']), max(target['x1'], target['x2']), max(target['y1'], target['y2'])
    target_corners = [(tx1, ty1), (tx2, ty1), (tx1, ty2), (tx2, ty2)]
    for corner in target_corners:
        if not any(point_in_rectangle(corner, rect) for rect in regions):
            return False
    return True

def point_in_rectangle(point, rect):
    px, py = point
    rx1, ry1, rx2, ry2 = min(rect['x1'], rect['x2']), min(rect['y1'], rect['y2']), max(rect['x1'], rect['x2']), max(rect['y1'], rect['y2'])
    return rx1 <= px <= rx2 and ry1 <= py <= ry2

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
