from flask import Flask, request, jsonify
from flask_cors import CORS
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarefas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
swagger = Swagger(app)

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(20), nullable=False, default='A Fazer')

    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'status': self.status
        }

# --- Rotas da API (PEP8) ---
@app.route('/adicionar_tarefa', methods=['POST'])
def adicionar_tarefa():
    dados = request.get_json()
    nova_tarefa = Tarefa(
        titulo=dados.get('titulo'),
        descricao=dados.get('descricao')
    )
    db.session.add(nova_tarefa)
    db.session.commit()
    return jsonify({'mensagem': 'Tarefa criada com sucesso'}), 201

@app.route('/buscar_tarefas', methods=['GET'])
def buscar_tarefas():
    tarefas_objetos = Tarefa.query.all()
    tarefas_dicionarios = [tarefa.to_dict() for tarefa in tarefas_objetos]
    return jsonify(tarefas_dicionarios)

@app.route('/atualizar_tarefa/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    tarefa = Tarefa.query.get_or_404(id)
    novo_status = request.get_json().get('status')
    tarefa.status = novo_status
    db.session.commit()
    return jsonify({'mensagem': 'Status da tarefa atualizado com sucesso'})

@app.route('/deletar_tarefa/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    tarefa = Tarefa.query.get_or_404(id)
    db.session.delete(tarefa)
    db.session.commit()
    return jsonify({'mensagem': 'Tarefa deletada com sucesso'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
