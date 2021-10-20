import datetime
import time

import requests
from eliminacion import eliminacion
# --------------------------
# creacion y edicion del template
from docxtpl import DocxTemplate
from docx.shared import Mm
from docx2pdf import convert
# --------------------------
# --------------------------
# enviar doc por email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# --------------------------------------------------------------------------
#   -- EN API --> servidor/main

# url = 'http://75.119.155.19:22500/usuarios/?cedula=0957546047'
# response = requests.get(url).json()
# name_Student = response[0]["v_contacto"]
# print(name_Student)
#
# # --- template
# doc = DocxTemplate("C:/Users/bcarl/Downloads/solicitud.docx")
#
# # Definir imagen insertada
# # picture = InlineImage(doc,
# # 					  'C: /Users/Surface/Desktop/word/illustration.png',
# # 					  width=Mm(100),
# #                       height=Mm(60)
# # 					  )
#
# # Inserte el contenido de docx
#
# context = {
#     'fecha': datetime.date.today(),
#     'nombre': response[0]["v_nombres".replace(" ' ", "")],
#     'apellido': response[0]["v_apellidos".replace(" ' ", "")],
#     'cedula': response[0]["v_cedula".replace(" ' ", "")],
#     'carrera': response[0]["v_carrera".replace(" ' ", "")],
#     'nivel': '3ro'
# }
#
# doc.render(context)
# doc.save("C:/Users/bcarl/Desktop/jordy.docx")
# ---------------------------------------------------------------------------

c = "C:/Users/bcarl/Desktop/jordy.docx"
convert(c)
pdf = "C:/Users/bcarl/Desktop/jordy.pdf"
# time.sleep()
# --- email
# Iniciamos los parámetros del script
time.sleep(1)
remitente = 'bcarlosjordy.@gmail.com'
destinatarios = ['cjbuestan@est.itsgg.edu.ec']  # cjbuestan@est.itsgg.edu.ec
asunto = '[RPI] Correo de prueba'
cuerpo = 'Este es el contenido del mensaje'
ruta_adjunto = "C:/Users/bcarl/Desktop/jordy.docx"
nombre_adjunto = 'jordy.docx'

# Creamos el objeto mensaje
mensaje = MIMEMultipart()

# Establecemos los atributos del mensaje
mensaje['From'] = remitente
mensaje['To'] = ", ".join(destinatarios)
mensaje['Subject'] = asunto

# Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
mensaje.attach(MIMEText(cuerpo, 'plain'))

# Abrimos el archivo que vamos a adjuntar
archivo_adjunto = open(ruta_adjunto, 'rb')

# Creamos un objeto MIME base
adjunto_MIME = MIMEBase('application', 'octet-stream')
# Y le cargamos el archivo adjunto
adjunto_MIME.set_payload(archivo_adjunto.read())
# Codificamos el objeto en BASE64
encoders.encode_base64(adjunto_MIME)
# Agregamos una cabecera al objeto
adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
# Y finalmente lo agregamos al mensaje
mensaje.attach(adjunto_MIME)

# Creamos la conexión con el servidor
sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)

# Ciframos la conexión
sesion_smtp.starttls()

# Iniciamos sesión en el servidor
sesion_smtp.login('bcarlosjordy@gmail.com', '25062018')

# Convertimos el objeto mensaje a texto
texto = mensaje.as_string()

# Enviamos el mensaje
sesion_smtp.sendmail(remitente, destinatarios, texto)

# Cerramos la conexión
sesion_smtp.quit()

archivo_adjunto.close()
eliminacion()
