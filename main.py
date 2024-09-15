class Empregado:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def salario(self):
        ...

class Gerente(Empregado):
    def salario(self):
        bonus_fixo = float(input(f"Digite quantos de bonus recebeu {self.nome}: "))
        total_salario1 = self.salario_base + bonus_fixo
        return f"{self.nome} tem salario de {self.salario_base} + bônus fixo {bonus_fixo}, recebendo no total {total_salario1}"
    
class Vendedor(Empregado):
    def salario(self):
        comissao = float(input(f"Digite quantos de comissão recebeu {self.nome}: "))
        total_salario1 = self.salario_base + comissao
        return f"{self.nome} tem salario de {self.salario_base} + comissão sobre vendas de {comissao}, recebendo no total {total_salario1}"
    
Roger = Gerente("Roger", 3500)
Rodolfo = Vendedor("Rodolfo", 1400)

print(Rodolfo.salario())
print(Roger.salario())