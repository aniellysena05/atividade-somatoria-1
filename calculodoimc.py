print(30*'-')
print('| CALCULADORA DE IMC         |')
print(30*'-')
nome =input("| Digite seu nome :")
peso= float(input('| Digite seu peso :'))
altura=float( input('| Digite sua altura :'))

imc=peso/altura**2
print(f'| O IMC é: {imc:.2f}')   
if imc <=18.5:
    print('| Você está baixo do peso')
    print('| coma mais pizza,Não viva só de miojo e vento :)')
elif imc < 24.9:
    print('| Você está com o peso normal')
    print('| muito bem continue assim,mais nada de comer só salada,hein ninguem é de ferro coma sobremesa também ')
elif imc < 29.9:
    print('| Você está com sobrepeso')
    print ('| Opa talvez seja bom maneirar nos lanches de madrugada...mas só talvez ')
elif imc <34.9:
    print('| Obesidade grau 1')
    print('| Cuidado!seu corpo esta pedindo socorro,tipo (Me salvaaaa)')
elif imc <39.9:
    print('| Obesidade grau 2')
    print('| Opa acho que você utrapassou um pouco dos limites da pizza ')
else:
    print('| Obesidade grau 3 (mórbida)')
    print('| Talvez seja hora de trocar essas pizzas por caminhadadas no parque ')

print(85*'-')
print ('| Esses cálculos é só uma estimativa.sempre bom consutar um profissional de saúde   |')
print(85*'-')