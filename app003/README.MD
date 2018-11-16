#app002

1. index para programar comportamiento

-para abrir es ctrl+j
-vamos a la carpeta que estamos trabajando 
    -cd "carpeta" 
    -python app.py  (se pone un espacio despues de la direcci{on de la carpeta})

-PARA detener el compilado es ctrl+c 

-para empezar codigo python en html se pone un ($) 

otro codigo para mandar registros 
en index 
class Index:
    def GET(self):
        datos = ['gerardo', 'kjasbfkjsabfa']
        return render.index(datos)

en html 
$def with(datos)
<h1>Index</h1>
$for i in range(50):
    $i - $i <br>

   Nombre $datos[0]
   Email $datos[1]

        