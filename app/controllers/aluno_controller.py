from flask import Blueprint, jsonify, request

aluno_bp = Blueprint("aluno_bp", __name__)

alunos = [
    {"id": 1, "nome": "Amanda Silva", "idade": 19, "email": "amanda@gmail.com"},
    {"id": 2, "nome": "Bruno Oliveira", "idade": 22, "email": "bruno@gmail.com"}
]

@aluno_bp.route("/alunos", methods=["GET"])
def get_alunos():
    return jsonify(alunos)

@aluno_bp.route("/alunos/<int:idAluno>", methods=["GET"])
def get_aluno(idAluno):
    aluno = next((a for a in alunos if a["id"] == idAluno), None)
    if aluno:
        return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404

@aluno_bp.route("/alunos", methods=["GET"])
def create_aluno():
    novo_aluno = request.json
    alunos.append(novo_aluno)
    return jsonify(novo_aluno), 201