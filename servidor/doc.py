import datetime
import requests
from Qr import qr
from docx.shared import Mm
from docxtpl import DocxTemplate, InlineImage

link = 'URL de obtencion de datos a obtener'
response = requests.get(link).json()


def genDocument(nombre, apellido, cedula, carrera):
    qr.qr()
    tpl = DocxTemplate("C:/Users/bcarl/Downloads/solicitud.docx")
    context = {
        "fecha": datetime.date.today(),
        "nombre": nombre,
        "apellido": apellido,
        "cedula" : cedula,
        "nivel" : '3ro',
        "carrera" : carrera,
        "firma" : InlineImage(tpl, image_descriptor = "C:/Users/bcarl/PycharmProjects/pythonProject/Prueba_Firma/image.png"),
        "firmaa" : InlineImage(tpl, image_descriptor = "C:/Users/bcarl/PycharmProjects/pythonProject/Prueba_Firma/img_firma-3-300x196.jpg", width=Mm(26), height=Mm(17))
    }
    tpl.render(context)
    file_path = './document/'
    try:
        tpl.save(f'{file_path}generate_{response[0]["v_apellidos"]}_document.docx')
        return 'success'

    except Exception as e:
        return str(e)

def genDoc(nombre, apellido, jornada, cedula, carrera):
    tpl = DocxTemplate("C:/Users/bcarl/Downloads/inicio-fin.docx")
    context = {
        "fecha" : datetime.date.today(),
        "nombre" : nombre,
        "apellido" : apellido,
        "cedula" : cedula,
        "carrera" : carrera,
        "jornada" : jornada
    }
    tpl.render(context)
    file_path = './document/'
    try:
        tpl.save(f'{file_path}inicio-fin{response[0]["v_apellidos"]}.docx')
        return 'success'

    except Exception as e:
        return str(e)