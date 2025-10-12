#!/usr/bin/python3

DOC_FILENAME = "documentacion.md"

def is_title(line):
    return line.startswith('#')

def title_level(line):
    #return line.rindex('#') + 1
    return len(line) - len(line.lstrip('#'))

if __name__ == '__main__':
    structured_content = []
    first_title = True
    target_level = 1
    try:
        with open(DOC_FILENAME, "r") as doc:
            for line in doc:
                if(is_title(line)):
                    if(first_title):
                        first_title = False
                    else:
                        structured_content.append({
                            'title': section_title, 
                            'level': section_level,
                            'content': section_content
                        })
                    section_title = line.strip() #line[:-1]
                    section_level = title_level(line)
                    section_content = ''
                else:
                    section_content += line
            
        structured_content.append({
            'title': section_title, 
            'level': section_level,
            'content': section_content
        })
            
    except FileNotFoundError as not_found:
        print("Documentación no encontrada en '"+DOC_FILENAME+"'")
        
    option = -1
    #while(option != 0):
    while True:
        print("\033[1m")
        for index, section in enumerate(structured_content):
            #if(section['level'] == target_level):
            #    print("[" + str(index+1) + "] " + section['title'])
            print("[" + str(index+1) + "] " + section['title'])
        print("[0] - Terminar programa")
        print("\033[0m")
        try:
            option = int(input())
            if(option == 0):
                break
            if(option <= len(structured_content)):
                print("\033[30;47m" + structured_content[option-1]['title'] + "\033[0m")
                print(structured_content[option-1]['content'])
            else:
                print("Opción inválida\n")
        except ValueError:
            print("Opción inválida\n")
            continue


