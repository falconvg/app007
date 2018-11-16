import web

urls = (
     '/', 'application.controllers.index.Index',
     '/insertar', 'application.controllers.insertar.Insertar',     
     '/borrar', 'application.controllers.borrar.Borrar',
     '/actualizar', 'application.controllers.actualizar.Actualizar'
)

if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run() 