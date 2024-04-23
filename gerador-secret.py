import string
import secrets

caracteres = string.ascii_letters + string.digits

senha = ''.join(secrets.choice(caracteres) for i in range(16))

print(senha)