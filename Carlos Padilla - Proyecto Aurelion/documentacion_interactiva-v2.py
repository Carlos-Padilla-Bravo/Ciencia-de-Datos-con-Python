import os
import time
import re

class DocumentacionInteractiva:
    def __init__(self, ruta_documento):
        self.ruta_documento = ruta_documento
        self.secciones = self.parsear_documento()

    def parsear_documento(self):
        """Parsea el archivo Markdown para extraer secciones y subsecciones."""
        try:
            with open(self.ruta_documento, 'r', encoding='utf-8') as f:
                contenido = f.read()
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {self.ruta_documento}")
            return {}

        secciones = {}
        # Usamos una expresión regular para encontrar todos los encabezados (## y #)
        matches = list(re.finditer(r'^#(#?)\s*(.*)', contenido, re.MULTILINE))
        
        for i, match in enumerate(matches):
            nivel = len(match.group(1)) + 1
            titulo = match.group(2).strip()
            inicio = match.end()
            fin = matches[i + 1].start() if i + 1 < len(matches) else len(contenido)
            texto = contenido[inicio:fin].strip()
            
            if nivel == 1:
                secciones[len(secciones) + 1] = {"titulo": titulo, "texto": texto, "subsecciones": {}}
            elif nivel == 2 and secciones:
                # Asocia la subsección con la última sección de nivel 1 encontrada
                ultima_seccion = list(secciones.values())[-1]
                sub_idx = len(ultima_seccion["subsecciones"]) + 1
                titulo = re.sub(r'^\d+\.\s*', '', titulo)
                ultima_seccion["subsecciones"][sub_idx] = {"titulo": titulo, "texto": texto}

        return secciones

    def limpiar_pantalla(self):
        """Limpia la pantalla de la terminal."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_texto_paginado(self, texto: str):
        """Muestra texto largo con paginación y navegación mejorada."""
        lineas = texto.split('\n')
        alto_terminal = os.get_terminal_size().lines - 4
        total_paginas = (len(lineas) + alto_terminal - 1) // alto_terminal
        pagina_actual = 0

        while pagina_actual < total_paginas:
            self.limpiar_pantalla()
            inicio = pagina_actual * alto_terminal
            fin = min((pagina_actual + 1) * alto_terminal, len(lineas))
            
            print('\n'.join(lineas[inicio:fin]))
            
            if total_paginas > 1:
                print("\n" + "=" * 50)
                print(f"Página {pagina_actual + 1} de {total_paginas}")
                opciones = []
                if pagina_actual < total_paginas - 1:
                    opciones.append("ENTER para siguiente")
                if pagina_actual > 0:
                    opciones.append("'b' para anterior")
                opciones.append("'q' para volver")
                print(" | ".join(opciones))
                
                respuesta = input("\nOpción: ").lower()
                if respuesta == 'q':
                    break
                elif respuesta == 'b' and pagina_actual > 0:
                    pagina_actual -= 1
                elif respuesta == '' and pagina_actual < total_paginas - 1:
                    pagina_actual += 1
                elif respuesta == '' and pagina_actual == total_paginas - 1:
                    break
            else:
                input("\nPresione Enter para volver al menú...")
                break

    def mostrar_menu_principal(self):
        """Muestra y gestiona el menú principal."""
        while True:
            self.limpiar_pantalla()
            print("\n=== DOCUMENTACIÓN PROYECTO AURELION ===")
            print("\nSecciones disponibles:")
            for num, seccion in self.secciones.items():
                print(f"{num}. {seccion['titulo']}")
            print("0. Salir")
            
            try:
                opcion = int(input(f"\nSeleccione una sección (0-{len(self.secciones)}): "))
                if opcion == 0:
                    print("\n¡Gracias por usar la documentación interactiva!")
                    time.sleep(2)
                    self.limpiar_pantalla()
                    break
                elif opcion in self.secciones:
                    if self.secciones[opcion]["subsecciones"]:
                        self.mostrar_submenu(opcion)
                    else:
                        self.mostrar_texto_paginado(self.secciones[opcion]["texto"])
                else:
                    print("\nOpción no válida. Intente nuevamente.")
                    time.sleep(1)
            except ValueError:
                print("\nPor favor, ingrese un número válido.")
                time.sleep(1)

    def mostrar_submenu(self, numero_seccion: int):
        """Muestra y gestiona los submenús de las secciones."""
        seccion = self.secciones[numero_seccion]
        while True:
            self.limpiar_pantalla()
            print(f"\n=== {seccion['titulo']} - Subsecciones ===\n")
            
            for num, subseccion in seccion["subsecciones"].items():
                print(f"{num}. {subseccion['titulo']}")
            print("0. Volver al menú principal")
            
            try:
                opcion = int(input(f"\nSeleccione una subsección (0-{len(seccion['subsecciones'])}): "))
                if opcion == 0:
                    break
                elif opcion in seccion["subsecciones"]:
                    self.mostrar_texto_paginado(seccion["subsecciones"][opcion]["texto"])
                else:
                    print("\nOpción no válida. Intente nuevamente.")
                    time.sleep(1)
            except ValueError:
                print("\nPor favor, ingrese solo números.")
                time.sleep(1)

if __name__ == "__main__":
    # La ruta al documento MD se pasa al inicializar la clase.
    doc = DocumentacionInteractiva(ruta_documento="Documentación-v2.md")
    if doc.secciones:
        doc.mostrar_menu_principal()
