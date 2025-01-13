from app import create_app

# Cria a instância do aplicativo Flask usando a função de fábrica definida em app/__init__.py
app = create_app()

if __name__ == '__main__':
    # Inicia o servidor Flask no ambiente local
    app.run()
