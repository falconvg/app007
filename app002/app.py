import web

urls = (
    "/", "Index", 
    '/acercade', 'Acercade',)

#para abrir la carpeta 
#renderizado para tomar el codigo y mostrarlo como respuesta (muestra la pagina que esta llamando )
render = web.template.render('templates/')

#estas son nuestras p{aginas que mandamos llamar, indica donde estan las p{aginas web 
class Index:
    def GET(self):
        nombre = "Gerardo"
        email = "falconvg@hotmail.com"
        return render.index(nombre,email)
            
class Acercade:
    def GET(self):
        return render.acercade()

if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()