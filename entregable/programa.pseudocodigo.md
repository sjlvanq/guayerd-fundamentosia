```
CONSTANTE DOC_FILENAME ← "documentacion.md"

FUNCIÓN esTitulo(linea)
    DEVOLVER (linea comienza con '#')

FUNCIÓN nivelTitulo(linea)
    CONTAR cuántos caracteres '#' hay al inicio de la línea
    DEVOLVER ese número

FUNCIÓN formatearOpcionMenu(indice, titulo)
    DEVOLVER texto en negrita con el número y el título

FUNCIÓN formatearTitulo(titulo, nivel)
    DEVOLVER texto con fondo gris y letras negras del título

INICIO PROGRAMA PRINCIPAL

    listaSecciones ← lista vacía
    esPrimerTitulo ← VERDADERO
    nivelObjetivo ← 2

    INTENTAR
        ABRIR DOC_FILENAME en modo lectura COMO archivo
            tituloActual ← ""
            nivelActual ← 0
            contenidoActual ← ""

            PARA cada linea EN archivo HACER
                SI esTitulo(linea) Y nivelTitulo(linea) = nivelObjetivo ENTONCES
                    SI NO esPrimerTitulo ENTONCES
                        AGREGAR a listaSecciones un nuevo diccionario con:
                            'titulo' = tituloActual
                            'nivel' = nivelActual
                            'contenido' = contenidoActual sin espacios finales
                    SINO
                        esPrimerTitulo ← FALSO
                    FIN SI

                    tituloActual ← linea sin espacios
                    nivelActual ← nivelTitulo(linea)
                    contenidoActual ← salto de línea
                SINO SI NO esPrimerTitulo ENTONCES
                    contenidoActual ← contenidoActual + linea
                FIN SI
            FIN PARA

            AGREGAR última sección procesada a listaSecciones
        FIN ABRIR
    CAPTURAR error de archivo no encontrado
        MOSTRAR "Fichero de documentación no encontrado"
    FIN INTENTAR

    opcion ← -1

    MIENTRAS VERDADERO HACER
        PARA cada índice y sección en listaSecciones HACER
            MOSTRAR formatearOpcionMenu(índice + 1, sección.titulo)
        FIN PARA

        MOSTRAR opción [0] para salir

        INTENTAR
            LEER opcion desde entrada del usuario (como número)
            SI opcion = 0 ENTONCES
                SALIR DEL BUCLE
            FIN SI

            SI opcion está entre 1 y cantidad de secciones ENTONCES
                MOSTRAR formatearTitulo(sección seleccionada)
                MOSTRAR contenido de la sección
            SINO
                MOSTRAR "Opción inválida"
            FIN SI
        CAPTURAR error de conversión a número
            MOSTRAR "Opción inválida"
        FIN INTENTAR
    FIN MIENTRAS

FIN PROGRAMA
```
