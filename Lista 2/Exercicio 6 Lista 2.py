salh = float(input('Quanto tu ganha por hora?'))
hmes = int(input('Quantas horas tu trabalha por mês?'))
salb = salh * hmes
print('Salário bruto:',salb)
sall = salb - salb * 0.11
print('Salário apos imposto de renda:',sall)
sall = sall - salb * 0.08
print('Salário apos inss:',sall)
sall = sall - salb * 0.05
print('Salário Liquido após sindicato:',sall)
