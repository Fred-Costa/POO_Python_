class Complexo:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario

    def __add__(self, other):
        # Adição de números complexos
        novo_real = self.real + other.real
        novo_imaginario = self.imaginario + other.imaginario
        return Complexo(novo_real, novo_imaginario)

    def __sub__(self, other):
        # Subtração de números complexos
        novo_real = self.real - other.real
        novo_imaginario = self.imaginario - other.imaginario
        return Complexo(novo_real, novo_imaginario)

    def __mul__(self, other):
        # Multiplicação de números complexos
        novo_real = (self.real * other.real) - (self.imaginario * other.imaginario)
        novo_imaginario = (self.real * other.imaginario) + (self.imaginario * other.real)
        return Complexo(novo_real, novo_imaginario)

    def __str__(self):
        # Representação legível de números complexos
        if self.imaginario >= 0:
            return f"{self.real} + {self.imaginario}i"
        else:
            return f"{self.real} - {-self.imaginario}i"

# Exemplos de uso
num1 = Complexo(3, 4)
num2 = Complexo(1, -2)

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

print(f"Num1: {num1}")
print(f"Num2: {num2}")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")