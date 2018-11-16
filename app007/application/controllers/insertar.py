import web

#para abrir la carpeta 
#renderizado para tomar el codigo y mostrarlo como respuesta (muestra la pagina que esta llamando )
render = web.template.render('application/views/', base='master')

#estas son nuestras p{aginas que mandamos llamar, indica donde estan las p{aginas web 
class Insertar:
    def GET(self):
        return render.insertar()
    