def calcular_cedulas(valor):
    """
    Calcula a quantidade mínima de cédulas necessárias para um dado valor.

    Parâmetros:
        valor (int): O valor do saque solicitado. Deve ser um número inteiro positivo.

    Retorno:
        dict: Um dicionário contendo a quantidade de cada cédula necessária, com as chaves
        representando os valores das cédulas (como strings) e os valores sendo as quantidades.

    Exceções:
        ValueError: Lançada quando o valor não pode ser representado pelas notas disponíveis.
    """
    cedulas = [100, 50, 20, 10, 5, 2]

    # Inicializa o dicionário de resultados, com as cédulas como chaves e valores zerados
    resultado = {str(cedula): 0 for cedula in cedulas}

    for cedula in cedulas:
        # Verifica se a cédula pode ser usada para o valor restante
        if valor >= cedula:
            quantidade = valor // cedula  # Calcula quantas cédulas deste valor são necessárias
            resultado[str(cedula)] = quantidade  # Armazena a quantidade no resultado
            valor -= quantidade * cedula

    # Se sobrar um valor que não pode ser representado pelas cédulas disponíveis
    if valor > 0:
        raise ValueError("O valor nao pode ser representado pelas notas disponiveis.")

    return resultado