# Abstracción representada: Cajero Automático / Cuenta Bancaria

class CuentaBancaria:
    def __init__(self, titular, numero_cuenta, saldo_inicial=0):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.__saldo = saldo_inicial  # atributo encapsulado
        self.movimientos = []

    # Método para depositar dinero
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            self.movimientos.append(f"Depósito: +${monto}")
            print(f"Depósito exitoso. Nuevo saldo: ${self.__saldo:.2f}")
        else:
            print("El monto debe ser positivo.")

    # Método para retirar dinero
    def retirar(self, monto):
        if monto <= 0:
            print("El monto debe ser mayor que 0.")
        elif monto > self.__saldo:
            print("Saldo insuficiente.")
        else:
            self.__saldo -= monto
            self.movimientos.append(f"Retiro: -${monto}")
            print(f"Retiro exitoso. Nuevo saldo: ${self.__saldo:.2f}")

    # Método para consultar el saldo
    def consultar_saldo(self):
        print(f"Saldo actual: ${self.__saldo:.2f}")

    # Método para ver historial de movimientos
    def mostrar_historial(self):
        print(f"\nHistorial de movimientos de {self.titular}:")
        if self.movimientos:
            for mov in self.movimientos:
                print(" -", mov)
        else:
            print("No hay movimientos registrados.")


class CajeroAutomatico:
    def __init__(self):
        self.cuentas = []

    # Método para crear una nueva cuenta
    def crear_cuenta(self):
        print("\n CREAR NUEVA CUENTA")
        titular = input("Ingrese el nombre del titular: ")
        numero = input("Ingrese número de cuenta: ")

        # Verificamos que no exista ya una cuenta con ese número
        for c in self.cuentas:
            if c.numero_cuenta == numero:
                print("Ya existe una cuenta con ese número.")
                return

        saldo_inicial = float(input("Ingrese saldo inicial (puede ser 0): "))
        if saldo_inicial < 0:
            saldo_inicial = 0

        cuenta = CuentaBancaria(titular, numero, saldo_inicial)
        self.cuentas.append(cuenta)
        print(f"Cuenta creada para {titular} con saldo inicial de ${saldo_inicial:.2f}")

    # Buscar una cuenta por número
    def buscar_cuenta(self, numero):
        for cuenta in self.cuentas:
            if cuenta.numero_cuenta == numero:
                return cuenta
        return None

    # Menú principal
    def menu(self):
        while True:
            print("\n MENU CAJERO AUTOMÁTICO")
            print("1. Crear nueva cuenta")
            print("2. Depositar dinero")
            print("3. Retirar dinero")
            print("4. Consultar saldo")
            print("5. Ver historial de movimientos")
            print("6. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.crear_cuenta()

            elif opcion in ["2", "3", "4", "5"]:
                numero = input("Ingrese el número de cuenta: ")
                cuenta = self.buscar_cuenta(numero)
                if not cuenta:
                    print("No se encontró la cuenta.")
                    continue

                if opcion == "2":
                    monto = float(input("Ingrese el monto a depositar: "))
                    cuenta.depositar(monto)
                elif opcion == "3":
                    monto = float(input("Ingrese el monto a retirar: "))
                    cuenta.retirar(monto)
                elif opcion == "4":
                    cuenta.consultar_saldo()
                elif opcion == "5":
                    cuenta.mostrar_historial()

            elif opcion == "6":
                print("Gracias por usar el cajero. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente nuevamente.")


# Programa principal
if __name__ == "__main__":
    cajero = CajeroAutomatico()
    cajero.menu()
