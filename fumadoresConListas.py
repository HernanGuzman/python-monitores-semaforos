import random
import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)
semaphoreAgente = threading.Semaphore(1)


papel = []
fosforos = []
tabaco = []


def agente():
    global papel, fosforos, tabaco
    while True:
        semaphoreAgente.acquire() # esperar a reponer las cosas una vez que alguien haya tomado las dos anteriores
        caso = random.choice([0,1,2]) #al azar pone dos cosas en la mesa
        if caso == 0:
            papel.append(1)
            tabaco.append(1)
        if caso == 1:
            papel.append(1)
            fosforos.append(1)
        if caso == 2:
            tabaco.append(1)
            fosforos.append(1)

        
        

def fumadorConPapel():
    while True:
        global fosforos
        global tabaco
        if len(fosforos) > 0 and len(tabaco) > 0:     # si hay fósforos y tabaco en la mesa
            #TOMO LOS CIGARRILLOS
            fosforos.pop()
            tabaco.pop()             # tomarlos
            
            logging.info(f'Fumador con Papel: Armando y fumando cigarrillo') # armar cigarrillo y fumar: se puede simular con un sleep
            time.sleep(1)
            semaphoreAgente.release()           # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
            
            
        
            
            
            

def fumadorConFosforos():
    while True:
        global papel
        global tabaco
        if len(papel) > 0 and len(tabaco) > 0:        # si hay papel y tabaco en la mesa
            #TOMO LOS CIGARRILLOS
            papel.pop()                 # tomarlos
            tabaco.pop()                # tomarlos
            logging.info(f'Fumador con Fosforos: Armando y fumando cigarrillo') # armar cigarrillo y fumar: se puede simular con un sleep
            time.sleep(1)
            semaphoreAgente.release() # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
            
        
            
            
            

def fumadorConTabaco():
    while True:
        global papel
        global fosforos
        if len(papel) > 0 and len(fosforos) > 0:   # si hay fósforos y papel en la mesa
            #TOMO LOS CIGARRILLOS
            papel.pop()             # tomarlos
            fosforos.pop()          # tomarlos
            logging.info(f'Fumador con Tabaco: Armando y fumando cigarrillo') # armar cigarrillo y fumar: se puede simular con un sleep
            time.sleep(1)
            semaphoreAgente.release() # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
           
        
           
            
            


agenteHilo = threading.Thread(target=agente)
fumadorConPapelHilo = threading.Thread(target=fumadorConPapel)
fumadorConFosforosHilo = threading.Thread(target=fumadorConFosforos)
fumadorConTabacoHilo = threading.Thread(target=fumadorConTabaco)

agenteHilo.start()
fumadorConPapelHilo.start()
fumadorConFosforosHilo.start()
fumadorConTabacoHilo.start()
