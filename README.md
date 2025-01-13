# Simulador de Caixa Eletrônico com Flask

Este é um projeto de API desenvolvida com Flask que simula o funcionamento de um caixa eletrônico. A API recebe um valor de saque e retorna a quantidade mínima de cédulas necessárias para compor o valor solicitado, utilizando as denominações disponíveis: 100, 50, 20, 10, 5 e 2.

## Documentação

### **Endpoints**

#### 1. `/api/saque` (POST)
- **Descrição**: Calcula a quantidade mínima de cédulas para um valor de saque.
- **Requisição**:
  - **Corpo (JSON)**:
    ```json
    {
      "valor": 380
    }
    ```
- **Respostas**:
  - **200 OK**:
    ```json
    {
      "10": 1,
      "100": 3,
      "2": 0,
      "20": 1,
      "5": 0,
      "50": 1
    }
    ```
  - **400 Bad Request**:
    ```json
    {
      "erro": "O valor deve ser um inteiro positivo"
    }
    ```
    ou
    ```json
    {
      "erro": "O valor nao pode ser representado pelas notas disponiveis."
    }
    ```
  - **500 Internal Server Error**:
    - Para exceções inesperadas.

### **Estrutura do Projeto**
    O projeto está organizado da seguinte forma:

        CAIXA_API/
        ├── app/
        │   ├── __init__.py        # Configuração principal e registro dos Blueprints
        │   ├── routes.py          # Blueprint principal para as rotas de saque
        │   ├── logic.py           # Lógica para cálculo das cédulas
        │   ├── config.py          # Configurações globais (e.g., DEBUG)
        ├── run.py                 # Arquivo de execução principal
        ├── README.md              # Documentação do projeto

## Como executar o projeto

1. **Pré-requisitos**:
   - Python 3.7 ou superior.
   - `pip` instalado.

2. **Clone o repositório**:
    ```bash
    git clone https://github.com/seu-repositorio/caixa_api.git
    cd caixa_api

3. **Instale as dependências**:
    ```bash
    pip install flask

4. **Inicie o servidor**:
    ```bash
    python run.py

5. **Teste a API**:
    ```bash
    curl -X POST -H "Content-Type: application/json" -d "{\"valor\": 380}" http://127.0.0.1:5000/api/saque


## **Principais desafios**

1. **Aprender Flask**:
    O projeto exigiu familiarização com o framework Flask, incluindo conceitos como Blueprints e organização de rotas.

2. **Organização do projeto**:
    Planejar uma estrutura modular e escalável para facilitar a manutenção e o crescimento do projeto.

3. **Sintaxe nova**:
    Entender e aplicar sintaxes específicas do Flask, como jsonify, manipulação de requisições e uso de Blueprints.

4. **Casos de Testes**:
    Como era minha primeira experiência com Flask e com a criação de casos de teste, enfrentei dificuldades em implementar testes automatizados para validar as funcionalidades do projeto.
