from flask import Flask
from app.routes import bp as api_bp

# Função de fábrica para criar a aplicação Flask
def create_app():
    app = Flask(__name__)

    # Carrega configurações do arquivo de configuração definido em app/config.py
    app.config.from_object('app.config')

    # Registra o Blueprint da API
    app.register_blueprint(api_bp)

    return app


