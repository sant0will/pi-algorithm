import time
start = time.time()
from threading import Thread
import math
import random
total_pontos = 10000000
num_threads = 400
pontos_quad = total_pontos/num_threads
pi = 0.0

def calcula_pontos(result, index):  
  pontos_circ = 0
  cont = 1

  while cont <= pontos_quad:
    # Px = random.random()
    # Py = random.random()

    deltaX = math.pow((random.random()-0.5), 2)
    deltaY = math.pow((random.random()-0.5), 2)
    distancia = math.sqrt(deltaX+deltaY)
    if distancia < 0.5:
      pontos_circ += 1

    cont += 1

  result[index] = pontos_circ

threads = [None] * num_threads
results = [None] * num_threads

for i in range(len(threads)):
  threads[i] = Thread(target=calcula_pontos, args=(results, i))
  threads[i].start()

for i in range(len(threads)):  
  threads[i].join()
        
print(4*(float(sum(results)))/(float(total_pontos)))
end = time.time()
print(end - start)
