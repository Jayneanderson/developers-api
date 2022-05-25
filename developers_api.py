from flask import Flask, jsonify, request
import json

request.d
app = Flask(__name__)

developers = [
    {"id": 1, "name": "Jay Show", "habilidades": ['Python', 'Java']},
    {"id": 2, "name": 'Felipe', 'habilidades': ['Python']}
]

@app.route('/devs')
def get_developers():
    return jsonify(developers)
    
@app.route('/devs/<int:id>', methods=['GET'])
def get_developer(id):
    # developer = developers[id]
    developer = find_developer(id)
    print(developer)
    return jsonify(developer)

@app.route('/devs/<int:id>', methods=['PUT'])
def update_developer(id):
    developer = json.loads(request.data)
    developers[id] = developer
    return jsonify(developer)
    
@app.route('/devs/<int:id>', methods=['DELETE'])
def delete_developer(id):
    developers.pop(id)
    return jsonify({"mensagem": "Usuário excluído com sucesso"})

@app.route('/devs', methods=['POST'])
def create_developer():
    data = json.loads(request.data)

    developers.append(data)
    return jsonify(developers)

def find_developer(id):
    for d in developers:
        if d['id'] == id:
            return d
    return 'Developer not found'
    
if __name__ == '__main__':
    app.run()

