valor_compra = 17.00
pagamento = 100.00

troco = pagamento - valor_compra

aux = troco
c20 = aux // 20
aux = aux % 20 
c10 = aux // 10
aux = aux % 10
c5 = aux // 5
aux = aux % 5
c1 = aux 

print('\tPagamento = ', pagamento, '\t\nCompra = ', valor_compra, '\t\nTroco = ', troco)
print('\tCédula de 20 = ', c20)
print('\tCédula de 10 = ', c10)
print('\tCédula de 5 = ', c5)
print('\tCédula de 1 = ', c1)