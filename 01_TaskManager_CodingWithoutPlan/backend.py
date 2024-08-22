from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Simulamos una base de datos en memoria
tasks = []

@app.route('/')
def index():
    return render_template('frontend.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        return jsonify({'error': 'Title is required'}), 400
    
    new_task = {
        'id': len(tasks) + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ''),
        'completed': False
    }
    tasks.append(new_task)
    print(f'Task added: {new_task}')  # Mensaje de depuración
    return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    task['title'] = request.json.get('title', task['title'])
    task['description'] = request.json.get('description', task['description'])
    task['completed'] = request.json.get('completed', task['completed'])
    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    tasks.remove(task)
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)