import re

def validar_senha(senha: str) -> bool:
    """
    Valida uma senha de acordo com as seguintes regras:
    1. Entre 8 e 20 caracteres
    2. Pelo menos uma letra maiúscula
    3. Pelo menos uma letra minúscula
    4. Pelo menos um número
    5. Pelo menos um caractere especial (!@#$%&*)
    6. Não pode conter espaços em branco
    """
    if len(senha) < 8 or len(senha) > 20:
        return False
    if " " in senha:
        return False
    if not re.search(r"[A-Z]", senha):
        return False
    if not re.search(r"[a-z]", senha):
        return False
    if not re.search(r"[0-9]", senha):
        return False
    if not re.search(r"[!@#$%&*]", senha):
        return False
    return True


if __name__ == "__main__":
    senha = input("Digite uma senha para validar: ")
    if validar_senha(senha):
        print("✅ Senha válida!")
    else:
        print("❌ Senha inválida!")
