from conta import Conta

c = Conta()
#print("Saldo: ", c.getSaldo())
#c.setSaldo(100)
#print("Saldo: ", c.getSaldo())

print("Saldo: ", c.saldo)
c.saldo = 100
print("Saldo: ", c.saldo)

c.sacar(100)
c.sacar(98)
c.depositar(1.5)
c.depositar(2)

print("Saldo: ", round(c.saldo, 2))