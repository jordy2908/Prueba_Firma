# from flaskwebgui import FlaskUI # import FlaskUI
import uvicorn

from credenciales.drive import *
from pathlib import Path

from validador import codigo
import requests
from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from starlette.background import BackgroundTasks
from starlette.requests import Request
from starlette.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from doc import genDocument, genDoc
import os


link = ' '  # URL PARA OBTENCIO LA INFORMACION PERSONAL
response = requests.get(link).json()  # CONVERCION DE LA INFORMACION A FORMATO JSON

# print(response[0]["v_cedula"])

codig = codigo()  # GENERACION DE CODIGO VALIDADOR

HOST_NAME = os.getenv("HOST_NAME")

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "templates"),
    name="static",
)

template = Jinja2Templates(directory="templates")  # DIRECTORIO DE LOS TEMPLATES

conf = ConnectionConfig(  # CONFIGURACION SEL SERVIDOR SMTP PARA EL ENVÍO DEL CODIGO Y ARCHIVO POR EMAIL
    MAIL_USERNAME='email',
    MAIL_PASSWORD="contraseña",
    MAIL_FROM='email',
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_TLS=True,
    MAIL_SSL=False
)


# ===============================================================================================
# ----- PAGINA PRINCIPAL
@app.get("/")
def main():
    return RedirectResponse(url="/alumno/")  # REDIRECCIONAMIENTO A LA PAGINA DE LOGIN


@app.get('/alumno/', response_class=HTMLResponse)
def home(request: Request):
    return template.TemplateResponse("/html/login.html", {"request": request})  # PAGINA DE LOGIN


# ===============================================================================================
# ===============================================================================================
# ----- YA SE ESTA VALIDADO POR JAVASCRIPT

# @app.post('/alumnos/', response_class = HTMLResponse)
# async def home(request : Request ):
#     formdata = await request.form()
#     datos = formdata["contra"]
#     ced = response[0]["v_cedula"]
#     print(datos)
# if ced != datos:
#     return template.TemplateResponse("/html/login.html", {"request" : request}) # REDIRECCIONAMIENTO DE LA PAGINA SI LA CEDULA INSERTADA ES DIFERENTE AL DE LA INFORMACION OBTENIDA DE LA URL
#     return template.TemplateResponse("/html/docs.html", {"request" : request})
# else:
#     return template.TemplateResponse("/html/login.html", {"request" : request})

# ===============================================================================================
# ===============================================================================================

# ---- Validación de codigo Email

@app.post("/valid_code")
async def valid_code(request: Request):
    form = await request.form()
    datos = form["codigo"]
    print(codig)
    if codig == datos:  # VALIDACION DEL CODIGO INGRESADO Y EL CODIGO ENVIADO POR EMAIL
        return template.TemplateResponse("/html/docs.html", {"request": request})
    else:
        return template.TemplateResponse("/html/login.html", {
            "request": request})  # REDIRECCIONAMIENTO DE LA PAGINA SI EL CODIGO ENVIADO POR EMAIL ES DIFERENTE AL CODIGO INSERTADO DE LA PAGINA


# ===============================================================================================
# ===============================================================================================

# ---- GENERACIÓN DEL DOCUMENTO

@app.post('/doc')  # GENERACION, ENVIO POR EMAIL Y ELIMINACION DEL ARCHIVO EN ALMACENAMIENTO
def generate_document(request: Request, background_tasks: BackgroundTasks):
    descarga()
    url = f'{HOST_NAME}/static/generate_{response[0]["v_apellidos"]}_document2.docx'
    rs = genDocument(response[0]["v_nombres"], # Obtencion de datos de la URL para introducirlos en el doc template
                     response[0]["v_apellidos"],
                     response[0]["v_cedula"],
                     response[0]["v_carrera"],
                     )

    ret = {
        "status": 'ok',
        "download": url
    }

    file_name = f'generate_{response[0]["v_apellidos"]}_document.docx'
    # file_path = f'D:/Users/buest/Downloads/{file_name}'
    file_path = f'./document/{file_name}'

    email = response[0]["v_correo_personal"]

    message = MessageSchema(
        subject="Fastapi mail module",
        recipients=[email],
        body="Simple background task ",
        attachments=[file_path]
    )

    fm = FastMail(conf)

    background_tasks.add_task(fm.send_message, message)

    os.startfile(f'C:/Users/bcarl/PycharmProjects/pythonProject/Prueba_Firma/document/{file_name}', "print") # Impresion del doc -- copiar directorio completo donde se descarga el archivo, excepto el nombre

    # os.remove(f'{file_path}generate_{response[0]["v_apellidos"]}_document.docx')
    return template.TemplateResponse('/html/docs.html', {'request': request})

    # file_name = f'generate_{response[0]["v_nombres"]}_document.docx'
    # file_path = f'./document/{file_name}'
    # time.sleep(5)
    # if os.path.exists(file_name):
    #     try:
    #         os.remove(os.getcwd() + "/" + file_name)
    #         return JSONResponse(content={
    #             "eliminado": True
    #         }, status_code=200)
    #     except FileNotFoundError:
    #         return JSONResponse(content={
    #             "eliminado": False,
    #             "error_message": "Archivo no encontrado"
    #         }, status_code=404)        # return RedirectResponse('docs.html')
    # else:
    #     return 'file does no exist'


@app.post('/doc2')
def generate_document(request: Request, background_tasks: BackgroundTasks):
    doc2()
    url = f'{HOST_NAME}/static/inicio-fin{response[0]["v_apellidos"]}.docx'

    rs = genDoc(response[0]["v_apellidos"], # Obtencion de datos de la URL para introducirlos en el doc template
                response[0]["v_nombres"],
                response2[0]["v_jornada"],
                response[0]["v_cedula"],
                response2[0]["v_carrera"],
                )

    ret = {
        "status": 'ok',
        "download": url
    }

    file_name = f'inicio-fin{response[0]["v_apellidos"]}.docx'
    # file_path = f'D:/Users/buest/Downloads/{file_name}'
    file_path = f'./document/{file_name}'

    email = response[0]["v_correo_personal"]

    message = MessageSchema(
        subject="Fastapi mail module",
        recipients=[email],
        body="Simple background task ",
        attachments=[file_path]
    )

    fm = FastMail(conf)

    background_tasks.add_task(fm.send_message, message)

    os.startfile(f'C:/Users/bcarl/PycharmProjects/pythonProject/Prueba_Firma/document/{file_name}', "print") # Impresion del doc -- copiar directorio completo donde se descarga el archivo, excepto el nombre

    # os.remove(f'{file_path}generate_{response[0]["v_apellidos"]}_document.docx')
    return template.TemplateResponse('/html/docs.html', {'request': request})


# ===============================================================================================
# ===============================================================================================

# -------------- ELIMINACION DEL DOCUMENTO --- > INCLUIDO EN /DOC

@app.post('/deletefile/')
def delete_file(request: Request):
    file_name1 = f'inicio-fin{response[0]["v_apellidos"]}.docx'
    file_name = f'generate_{response[0]["v_apellidos"]}_document.docx'
    # file_path = f'./document/{file_name}'
    try:
        os.remove('./document' + '/' + file_name)
        os.remove('./document' + '/' + file_name1)
        os.remove('C:/Users/bcarl/PycharmProjects/pythonProject/Prueba_Firma/image.png')
        os.remove('C:/Users/bcarl/Downloads/solicitud.docx')
        os.remove('C:/Users/bcarl/Downloads/inicio-fin.docx') # Eliminacion de los documentos
    except:
        pass
    return template.TemplateResponse('/html/login.html', {'request': request})


# ===============================================================================================
# ===============================================================================================

# -------------- ENVÍO DE CÓDIGO DE AUTENTICACIÓN

@app.post("/send_code")  # ENVIO DEL CODIGO POR EMAIL
async def code(request: Request, background_tasks: BackgroundTasks):
    msg = f'<h1> {codig} </h1>'
    email = response[0]["v_correo_personal"] # Obtencion del Email mediante JSON de la URL
    message = MessageSchema(
        subject="Fastapi mail module",
        recipients=[email],
        body=msg,
    )

    fm = FastMail(conf)

    background_tasks.add_task(fm.send_message, message)

    return template.TemplateResponse('/html/validador.html', {'request': request})

    # return JSONResponse(status_code=200, content={"message": "email has been sent"})


# ===============================================================================================
# ===============================================================================================

# ------------------- ENVÍO DEL DOCUMENTO POR CORREO ----> INCLUIDO EN /DOC

# @app.post("/send_mail")
# async def send_file( background_tasks: BackgroundTasks ):
#     file_name = f'generate_{response[0]["v_apellidos"]}_document.docx'
#     # file_path = f'D:/Users/buest/Downloads/{file_name}'
#     file_path = f'./document/{file_name}'
#
#     email = response[0]["v_correo_personal"]
#
#     message = MessageSchema(
#         subject="Fastapi mail module",
#         recipients=[email],
#         body="Simple background task ",
#         attachments=[file_path]
#     )
#
#     fm = FastMail(conf)
#
#     background_tasks.add_task(fm.send_message, message)
#
#     # return JSONResponse(status_code=200, content={"message": "email has been sent"})
# ================================================================================