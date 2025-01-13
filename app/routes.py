from flask import Blueprint, request, jsonify
from app.logic import calcular_cedulas

# Criação de um Blueprint para organizar as rotas da API
bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/saque', methods=['POST'])
def saque():
    """
    Endpoint para calcular a quantidade mínima de cédulas necessárias para um valor de saque.
    
    Requisição:
        Método: POST
        Corpo (JSON): {"valor": <int>} - Um valor inteiro positivo representando o valor do saque.
    
    Resposta:
        - 200: Retorna a quantidade de cédulas necessárias em JSON.
        - 400: Retorna um erro se o valor for inválido ou não puder ser representado pelas notas.
        - 500: Retorna um erro genérico para exceções inesperadas.
    """
    try:
        # Obtém o JSON enviado na requisição
        dados = request.get_json()
        valor = dados.get("valor")  # Extrai o valor do saque do corpo da requisição

        # Validação: verifica se o valor é um inteiro positivo
        if not isinstance(valor, int) or valor <= 0:
            return jsonify({"erro": "O valor deve ser um inteiro positivo"}), 400

        # Chama a lógica de cálculo e retorna o resultado em formato JSON
        resultado = calcular_cedulas(valor)
        return jsonify(resultado)

    except ValueError as ve:
        # Trata casos onde o valor não pode ser representado pelas notas disponíveis
        return jsonify({"erro": str(ve)}), 400

    except Exception as e:
        # Captura exceções genéricas para evitar que erros não tratados quebrem a aplicação
        return jsonify({"erro": f"Erro no processamento: {str(e)}"}), 500