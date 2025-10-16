#!/usr/bin/python3

# Constante que almacena ruta y nombre de archivo de documentación
DOC_FILENAME = "documentacion.md"

def is_title(line: str) -> bool:
    """Método que identifica si una línea es un título"""
    return line.startswith('#')

def title_level(line: str) -> int:
    """Método que devuelve el nivel de un título"""
    return len(line) - len(line.lstrip('#'))
    
def format_menu_option(index: int, title: str) -> str:
	return "\033[1m" + "[" + str(index) + "] " + title + "\033[0m"
	
def format_title(title: str, level: int) -> str:
	return "\033[30;47m" + f"     {title.strip('#').strip()}     " + "\033[0m" + "\n"

if __name__ == '__main__':
	# Lista que almacenará cada sección como un diccionario
	# con las claves 'title', 'level' y 'content'
    structured_content = []
    
    # Bandera para omitir el volcado del contenido de la sección
    # si es el primer título del documento
    first_title = True
    
    # Nivel de título que será considerado en la generación del menú
    target_level = 2
    
    try:
        # Abre el archivo de documentación en modo lectura
        with open(DOC_FILENAME, "r") as doc:
            # Inicializa variables para la sección actual
            section_title = ""
            section_level = 0
            section_content = ""
            
            for line in doc:
                # Verifica si la línea es un título y si su nivel coincide con el nivel objetivo
                if(is_title(line) and title_level(line) == target_level):
                    if(not first_title):
                        structured_content.append({
                            'title': section_title, 
                            'level': section_level,
                            'content': section_content.strip()
                        })
                        
                    # Procesa el nuevo título como inicio de la nueva sección
                    else:
                        first_title = False # La primera sección ya ha sido procesada
                    
                    # Inicializa las variables para la nueva sección
                    section_title = line.strip()
                    section_level = title_level(line)
                    section_content = '\n' # Inicializa el contenido con un salto de línea
                    
                # Si no es un título objetivo y no estamos en la primera línea (primer_title es False)
                # significa que es contenido de la sección actual.
                elif(not first_title):
                    section_content += line
            
        # Una vez terminado el bucle, se almacena la última sección procesada
        structured_content.append({
            'title': section_title, 
            'level': section_level,
            'content': section_content.strip()
        })
            
    except FileNotFoundError as not_found:
        # Manejo de error si el archivo de documentación no existe
        print("Fichero de documentación no encontrado: '"+DOC_FILENAME+"'")
        
    # Variable para almacenar la opción seleccionada por el usuario
    option = -1
    
    # Bucle principal del menú
    while True:
		# Imprime el menú de opciones recorriendo el contenido estructurado
        for index, section in enumerate(structured_content):
			# Muestra el título de la sección como opción numerada (empezando en 1)
            print(format_menu_option(str(index+1), section['title']))
        
        # Opción para salir del programa
        print(format_menu_option(0," - Terminar programa"))
        
        try:
			# Solicita la entrada del usuario
            option = int(input("Seleccione una opción: "))
            
            if(option == 0):
				# Sale del bucle While
                break
            
            # Verifica si la opción está dentro del rango válido (1 hasta el número de secciones)            
            if(option <= len(structured_content)):
				# Imprime el título y el contenido de la sección seleccionada
                print(format_title(structured_content[option-1]['title'],
                    structured_content[option-1]['level']))
                print(structured_content[option-1]['content'] + "\n")
            else:
				# La opción es un número fuera del rango
                print("Opción inválida\n")
                
        except ValueError:
			# Manejo de error si el usuario introduce algo que no es un entero
            print("Opción inválida\n")
            continue

