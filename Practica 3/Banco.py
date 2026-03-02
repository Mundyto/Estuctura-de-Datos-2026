def encue(queue, elemento):
    queue.append(elemento)
    
def deque(queue):
    if len(queue) > 0: 
        queue.pop(0)

def peek(queue):
    return queue[0]

def is_empty(queue):
    if queue == []:
        return True
    else:         
        return False
    
def size(queue):
    return len(queue)

def retiros(lista, lista2):
    if not is_empty(lista) and not is_empty(lista2):
        r = lista[0] - lista2[0]
        deque(lista)
        deque(lista2)
        encue(lista, r)

def deposito(lista, lista2):
    if not is_empty(lista) and not is_empty(lista2):
        d = lista[0] + lista2[0]
        deque(lista)
        deque(lista2)
        encue(lista, d)

cola_saldos = []
cola_retiros = []
cola_depositos = []

encue(cola_saldos, 1000)
encue(cola_saldos, 1000)
encue(cola_saldos, 1000)
encue(cola_saldos, 1000)
encue(cola_saldos, 1000)

encue(cola_retiros, 500)
encue(cola_retiros, 500)
encue(cola_retiros, 500)
encue(cola_retiros, 500)
encue(cola_retiros, 500)

encue(cola_depositos, 300)
encue(cola_depositos, 300)
encue(cola_depositos, 300)
encue(cola_depositos, 300)
encue(cola_depositos, 300)

retiros(cola_saldos, cola_retiros)
retiros(cola_saldos, cola_retiros)
retiros(cola_saldos, cola_retiros)
retiros(cola_saldos, cola_retiros)
retiros(cola_saldos, cola_retiros)

print(cola_saldos)

deposito(cola_saldos, cola_depositos)
deposito(cola_saldos, cola_depositos) 
deposito(cola_saldos, cola_depositos)
deposito(cola_saldos, cola_depositos)   
deposito(cola_saldos, cola_depositos)

print(cola_saldos)

