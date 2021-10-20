from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

directorio_credentials = 'directorio donde se ubica credentials_module.json'

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
    archivo = credenciales.CreateFile({'id' : 'id del archivo'})
    nombre = archivo['title']
    archivo.GetContentFile('C:/Users/bcarl/Downloads/' + nombre) # Ubicacion de descarga

def doc2():
    credenciales = login()
    archivo = credenciales.CreateFile({'id' : 'id del archivo'})
    nombre = archivo['title']
    archivo.GetContentFile('C:/Users/bcarl/Downloads/' + nombre) # Ubicacion de descarga
