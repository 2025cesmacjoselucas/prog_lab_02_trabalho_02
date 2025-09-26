# Questão 3: Sistema de autenticação simples
# Usuários e senhas pré-definidos. Criar uma função para autenticar.

def authenticate(user: str, password: str) -> bool:
    usuarios = {
        "admin": "1234",
        "joao": "senha123",
        "maria": "abc@2024"
    }
    return usuarios.get(user) == password


usuario = input("Usuário: ")
senha = input("Senha: ")

if authenticate(usuario, senha):
    print("Autenticação bem-sucedida!")
else:
    print("Usuário ou senha incorretos.")
