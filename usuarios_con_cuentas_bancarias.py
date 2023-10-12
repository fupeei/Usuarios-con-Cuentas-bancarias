
class CuentaBancaria:

    def __init__(self, tasa_interés, balance, nombre):
        self.tasa_interés = tasa_interés
        self.balance = balance
        self.nombre = nombre
"""
    def depósito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        if amount <= self.balance:
            self.balance -= amount

            
        elif amount > self.balance:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
        return self
    
    def generar_interés(self):
        if self.balance > 0:
            self.balance += self.balance * self.tasa_interés
        return self

    def mostrar_info_cuenta(self):
        print(self.balance)"""


class Usuario:
    def __init__(self, nombre, cuentas):
        self.nombre = nombre
        self.cuentas = cuentas
    
            

    def hacer_deposito(self, deposito):
        self.cuentas.balance += deposito

    def hacer_retiro(self, retiro):
        self.cuentas.balance -= retiro

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.nombre}")
        print(f"Balance: {self.cuentas.balance}")
        print(f"Cuenta: {self.cuentas.nombre}")

cuentarut = CuentaBancaria(0.02,100, "Cuenta rut")
cuentacorriente = CuentaBancaria(0.02, 500, "Cuenta Corriente")

usuario1 = Usuario("Chris", cuentacorriente)
usuario1.hacer_deposito(200)
usuario1.hacer_retiro(100)
usuario1.mostrar_balance_usuario()
print("--------------")
usuario1 = Usuario("Chris", cuentarut)
usuario1.hacer_deposito(200)
usuario1.hacer_retiro(100)
usuario1.mostrar_balance_usuario()