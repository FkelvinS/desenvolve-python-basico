def validador_senha(senha):
    # Verifica se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        return False

    # Flags para os critérios
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False

    # Conjunto de caracteres especiais
    especiais = "@#$%^&*()-_=+[]{}|;:,.<>?/!"

    # Percorre cada caractere da senha e verifica os critérios
    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_numero = True
        elif caractere in especiais:
            tem_especial = True

    # Retorna True se todos os critérios forem atendidos
    return tem_maiuscula and tem_minuscula and tem_numero and tem_especial

# Exemplo de uso:
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"

print(validador_senha(senha1))  # Saída esperada: True
print(validador_senha(senha2))  # Saída esperada: False
print(validador_senha(senha3))  # Saída esperada: False
