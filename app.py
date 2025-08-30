from flask import Flask, request, jsonify
from flask_cors import CORS
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy

# --- Configuração Inicial ---
app = Flask(__name__)
CORS(app)

# --- Configuração do SQLAlchemy ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarefas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# --- Inicialização das Extensões ---
db = SQLAlchemy(app)
swagger = Swagger(app)

# --- Modelo do Banco de Dados (Tabela Tarefas) ---
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

# --- Rotas da API ---
@app.route('/tarefas', methods=['POST'])
def add_task():
    """
    Adiciona uma nova tarefa.
    Esta rota cria uma nova tarefa no banco de dados com um título e descrição.
    ---
    tags:
      - Tarefas
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            titulo:
              type: string
              description: O título da tarefa.
              example: "Finalizar o MVP"
            descricao:
              type: string
              description: A descrição detalhada da tarefa.
              example: "Completar a integração do SQLAlchemy e Swagger."
    responses:
      201:
        description: Tarefa criada com sucesso.
    """
    dados = request.get_json()
    nova_tarefa = Tarefa(
        titulo=dados.get('titulo'), 
        descricao=dados.get('descricao')
    )
    db.session.add(nova_tarefa)
    db.session.commit()
    return jsonify({'mensagem': 'Tarefa criada com sucesso'}), 201

@app.route('/tarefas', methods=['GET'])
def get_tasks():
    """
    Retorna a lista de todas as tarefas.
    Esta rota consulta o banco de dados e retorna todas as tarefas cadastradas.
    ---
    tags:
      - Tarefas
    responses:
      200:
        description: Uma lista de tarefas.
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              titulo:
                type: string
              descricao:
                type: string
              status:
                type: string
    """
    tarefas_objetos = Tarefa.query.all()
    tarefas_dicionarios = [tarefa.to_dict() for tarefa in tarefas_objetos]
    return jsonify(tarefas_dicionarios)

@app.route('/tarefas/<int:id>', methods=['PUT'])
def update_task_status(id):
    """
    Atualiza o status de uma tarefa existente.
    Esta rota permite alterar o status de uma tarefa para 'A Fazer', 'Em Andamento' ou 'Concluído'.
    ---
    tags:
      - Tarefas
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: O ID da tarefa a ser atualizada.
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            status:
              type: string
              description: O novo status da tarefa.
              example: "Em Andamento"
    responses:
      200:
        description: Status da tarefa atualizado com sucesso.
      404:
        description: Tarefa não encontrada.
    """
    tarefa = Tarefa.query.get_or_404(id)
    novo_status = request.get_json().get('status')
    tarefa.status = novo_status
    db.session.commit()
    return jsonify({'mensagem': 'Status da tarefa atualizado com sucesso'})

@app.route('/tarefas/<int:id>', methods=['DELETE'])
def delete_task(id):
    """
    Deleta uma tarefa.
    Esta rota remove permanentemente uma tarefa do banco de dados.
    ---
    tags:
      - Tarefas
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: O ID da tarefa a ser deletada.
    responses:
      200:
        description: Tarefa deletada com sucesso.
      404:
        description: Tarefa não encontrada.
    """
    tarefa = Tarefa.query.get_or_404(id)
    db.session.delete(tarefa)
    db.session.commit()
    return jsonify({'mensagem': 'Tarefa deletada com sucesso'})

# --- Execução da Aplicação ---
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)