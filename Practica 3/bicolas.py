def enque_head(lista, elemento):
    lista.insert(0, elemento)

def deque_head(lista):
    return lista.pop(0)

def enque_tail(lista, elemento):
    lista.append(elemento)

def deque_tail(lista):
    return lista.pop()

def retiros(saldo_list, retiro_queue):
    monto_retiro = deque_head(retiro_queue)
    saldo_actual = deque_head(saldo_list)

    nuevo_saldo = saldo_actual - monto_retiro
    enque_tail(saldo_list, nuevo_saldo)

def depositos(saldo_list, deposito_list):
    monto_deposito = deque_tail(deposito_list)
    saldo_actual = deque_head(saldo_list)

    nuevo_saldo = saldo_actual + monto_deposito
    enque_tail(saldo_list, nuevo_saldo)

saldo = [1000,1000,1000,1000,1000]
retiro = [500,500,500,500,500]
deposito = [300,300,300,300,300]

print(f"Los saldos son: {saldo}")

for _ in range(5):
    retiros(saldo, retiro)
print(f"Saldo despues del retiro: {saldo}")

for _ in range(5):
    depositos(saldo, deposito)
print(f"Saldo despues del deposito: {saldo}")