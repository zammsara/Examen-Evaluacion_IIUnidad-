# main.py
from metodos import verificar_balanceo, balancear
import os 

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    input("Presione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')
    

limpiar_pantalla()
def main():
    while True:
        
        print("\n--- Menú ---")
        print("1. Verificar balanceo")
        print("2. Balancear cadena")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                cadena = input("Ingrese la cadena a verificar: ")
                if verificar_balanceo(cadena):
                    print("✅ La cadena está balanceada.")
                else:
                    print("❌ La cadena NO está balanceada.")
                

            case "2":
                cadena = input("Ingrese la cadena a balancear: ")
                balanceada = balancear(cadena)
                print(f"Cadena balanceada: {balanceada}")

            case "3":
                print("Gracias por usar el programa.")
                input("Presione Enter para salir...")
                limpiar_pantalla()
                break
            case _:
                print("Opción inválida, intente nuevamente.")
                limpiar_pantalla()

            
            

if __name__ == "__main__":
    main()
