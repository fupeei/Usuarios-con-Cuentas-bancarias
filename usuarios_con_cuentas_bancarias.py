
class CuentaBancaria:

    def __init__(self, tasa_interés, balance):
        self.tasa_interés = tasa_interés
        self.balance = balance

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
        print(self.balance)


class Usuario:
    def __init__(self, nombre, savings):
        self.nombre = nombre
        self.savings = CuentaBancaria(0.02, 0)

    def hacer_deposito(self, deposito):
        self.savings.balance += deposito

    def hacer_retiro(self, retiro):
        self.savings.balance -= retiro

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.nombre}")
        print(f"Usuario: {self.savings.balance}")



usuario1 = Usuario("Chris", ())
usuario1.hacer_deposito(100)
usuario1.hacer_deposito(100)
usuario1.hacer_deposito(100)
usuario1.hacer_retiro(100)
usuario1.mostrar_balance_usuario()