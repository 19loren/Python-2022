##Divisao entre os ganhadores de um valor - APPC

quantia = float(input("Digite a quantia a ser dividida "))

##
q1 = quantia * 0.46
q2 = quantia * 0.32
q3 = quantia * 0.22

##
print(f"\n\tValor total = R${quantia:.2f}")
print(f"\n\tO Primeiro jogador recebeu = R${q1:.2f}")
print(f"\n\tO Segundo jogador recebeu = R${q2:.2f}")
print(f"\n\tO Terceiro jogador recebeu = R${q3:.2f}")