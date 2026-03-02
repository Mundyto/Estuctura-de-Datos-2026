def encue(queue, elemento):
    queue.append(elemento)
    
def deque(queue):
    queue.pop(0)

def retiros(lista,lista2):
    r = lista[0]-lista2[0]
    deque(lista)
    deque(lista2)
    encue(lista,r)


def peek(queue):
    return queue[0]

def is_empty(queue):
    if queue == []:
        return True
    else:        
        return False
    
def size(queue):
    return len(queue)

listas = []
print(is_empty(listas))
encue(listas, 1)
print(listas)
encue(listas, 2)
deque(listas)
print(is_empty(listas))
encue(listas, 0)
encue(listas, 9)
print(peek(listas))
print(size(listas))

