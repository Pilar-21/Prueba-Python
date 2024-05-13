#Prueba Python IBM
# Para verificar el tipo de cualquier objeto en Python, usamos la función type() :
print(">>>>>>>>>>>><<<<<<<<<<<")
print("<<<Prueba Python IBM>>>")

s_textoLargo = """Declaro clase de objeto "Tareas",con la ayuda de ChatGPT, depurandolo con la teoría del curso en un texto largo para el profe, empezamos..."""

# Creo una clase llamada ListaTareas, y para la estructura del programa, utilzo un constructor, con metodo especial.
class ListaTareas:
    def __init__(self):
        self.tareas = []

# Agrego la función para insertar un elemento a la lista vacía con su descripción y estado / Para crear un conjunto vacío hay que usar set(), y con {} creamos un diccionario vacio / 
    def agregar_tarea(self, tarea):
        self.tareas.append({"descripcion": tarea, "completada": False})

# En estas funciones podemos realizar el marcado de completada o pendiente de cada tarea, manteniendo su enumercación / En la estructura de las opciones de "Marcar o Eliminar tarea" se reutilizan códigos para las excepciones.

    def marcar_completada(self, posicion):
        try:
            self.tareas[posicion]["completada"] = True
            print("Tarea marcada como completada.")
        except IndexError:
            print("La posición ingresada no es válida.")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas pendientes.")
        else:
            for i, tarea in enumerate(self.tareas):
                estado = "Completada" if tarea["completada"] else "Pendiente"
                print(f"{i+1}. {tarea['descripcion']} - Estado: {estado}")
                
 # Con esta definición podemos eliminar la tarea y su posición dentro de la lista.
                
    def eliminar_tarea(self, posicion):
        try:
            del self.tareas[posicion]
            print("Tarea eliminada correctamente.")
        except IndexError:
            print("La posición ingresada no es válida.")
  
# Nos enumera cada tarea en la lista, creando una cadena para cada tarea con su descripcion y estado (completada o pendiente), y el join nos une todas estas cadenas separandola por saltos de línea.
    
    def __str__(self):
        return "\n".join([f"{i+1}. {tarea['descripcion']} - Estado: {'Completada' if tarea['completada'] else 'Pendiente'}" for i, tarea in enumerate(self.tareas)])
  

# Defini la instancia de lista_tareas fuera de la función main.

lista_tareas = ListaTareas()

# Cuerpo del programa que veremos reflajado en la consola / Use el main solo para el script de la interfaz para proporcionar modularidad y porque no logre hacerlo de otra forma profe.

def main():
    while True:
        print("\n1. Agregar nueva Tarea")
        print("2. Marcar Tarea como completada")
        print("3. Mostrar todas las Tareas")
        print("4. Eliminar una Tarea")
        print("5. Salir")
        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            tarea = input("Ingrese la nueva Tarea: ")
            lista_tareas.agregar_tarea(tarea)
     
        elif opcion == "2":
            posicion = int(input("Indique la posición de la Tarea que desea marcar como terminada: ")) - 1
            lista_tareas.marcar_completada(posicion)
       
        elif opcion == "3":
            print(lista_tareas)
      
        elif opcion == "4":
            posicion = int(input("Indique la posición de la Tarea que desea eliminar: ")) - 1
            lista_tareas.eliminar_tarea(posicion)
           
        elif opcion == "5":
            print("Saliendo del programa... ")
            break
        
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
