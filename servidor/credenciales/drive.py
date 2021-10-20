from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

directorio_credentials = 'C:/Users/bcarl/PycharmProjects/pythonProject/Prueba_Firma/servidor/credenciales/credentials_module.json'

# inicia sesion

def login():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(directorio_credentials)

    if gauth.access_token_expired:
        gauth.Refresh()
        gauth.SaveCredentialsFile(directorio_credentials)
    else:
        gauth.Authorize()

    return GoogleDrive(gauth)


def descarga():
    credenciales = login()
    archivo = credenciales.CreateFile({'id' : '1QbAsLMFEm0J-M_SkhGWFeQ_aAVAIeEnv'})
    nombre = archivo['title']
    archivo.GetContentFile('C:/Users/bcarl/Downloads/' + nombre)

def doc2():
    credenciales = login()
    archivo = credenciales.CreateFile({'id' : '1IIfhIPvY0tlzy2jt1TR83PNnYyb5rePY'})
    nombre = archivo['title']
    archivo.GetContentFile('C:/Users/bcarl/Downloads/' + nombre)
