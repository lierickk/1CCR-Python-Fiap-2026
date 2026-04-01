#Leitura

nome = input("digite seu nome:")
hora = float(input("digite sua hora trabalhada:"))
horaTrabalhadaNoMes = float(input("digite sua hora trabalhada no Mes :"))
BonusFixo = float(input("digite sua Bonus Fixo:"))
descontoTotal = float(input("digite sua desconto total:"))



salarioBruto = (hora * horaTrabalhadaNoMes) + BonusFixo
salarioLiquido = salarioBruto - descontoTotal


print(nome)
print(f" salario Bruto e salario liquido :{salarioBruto,salarioLiquido}")


nome = input("Digite o nome do produto: ")
preco = float(input("Digite o valor do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))
percentual = float(input("Digite o percentual desconto do produto: "))

# Cálculo
bruto = preco * quantidade
desconto = (percentual / 100 * bruto)
final = bruto - desconto

# Saída
print(f"Nome do produto: {nome}")
print(f"Valor bruto do produto: {bruto:.2f} reais")
print(f"Quantidade de produto: {quantidade}")
print(f"Desconto do produto: {desconto:.2f} reais")
print(f"Valor final do produto: {final:.2f} reais")


n1 = int(input("digite o primeiro numero:"))
n2 = int(input("digite o segundo numero:"))
print(n1 * 2 + n2/2)





nome = input("digite seu nome:")
hora = float(input("digite sua hora trabalhada:"))
horaTrabalhadaNoMes = float(input("digite sua hora trabalhada no Mes :"))
BonusFixo = float(input("digite sua Bonus Fixo:"))
descontoTotal = float(input("digite sua desconto total:"))



salarioBruto = (hora * horaTrabalhadaNoMes) + BonusFixo
salarioLiquido = salarioBruto - descontoTotal


print(nome)
print(f" salario Bruto e salario liquido :{salarioBruto,salarioLiquido}")

