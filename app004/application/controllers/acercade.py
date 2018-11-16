import web

#para abrir la carpeta 
#renderizado para tomar el codigo y mostrarlo como respuesta (muestra la pagina que esta llamando )
render = web.template.render('application/views/', base='master')

#estas son nuestras p{aginas que mandamos llamar, indica donde estan las p{aginas web 
class Acercade:
    def __init__(self):
        pass
    
    def GET(self):
        nombre = "gerardo"
        email = "falconvg@hotmail.com"
        telefono = "7711259083"
        return render.acercade(nombre,email,telefono)