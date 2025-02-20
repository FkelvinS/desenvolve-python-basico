def calcular_digito(cpf, multiplicadores):
    soma = sum(int(cpf[i]) * multiplicadores[i] for i in range(len(multiplicadores)))
    resto = soma % 11
    return "0" if resto < 2 else str(11 - resto)

def validar_cpf(cpf):
    # Remover pontos e traço manualmente
    cpf = cpf.replace(".", "").replace("-", "")

    # Verificar se tem 11 dígitos
    if len(cpf) != 11 or not cpf.isdigit():
        return "Inválido"

    # Calcular os dígitos verificadores
    primeiro_digito = calcular_digito(cpf[:9], range(10, 1, -1))
    segundo_digito = calcular_digito(cpf[:9] + primeiro_digito, range(11, 1, -1))

    # Comparar com os dígitos informados
    return "Válido" if cpf[-2:] == primeiro_digito + segundo_digito else "Inválido"

# Solicita o CPF ao usuário
cpf_usuario = input("Digite um CPF (XXX.XXX.XXX-XX): ")

# Exibe o resultado da validação
print(validar_cpf(cpf_usuario))
