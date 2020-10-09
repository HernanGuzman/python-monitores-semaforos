import random
import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)
semaphoreAgente = threading.Semaphore(1)


papel = []
fosforos = []
tabaco = []


def agentePapelYFosforos():
    global papel, fosforos
    while True:
        semaphoreAgente.acquire()
        papel.append(1)
        fosforos.append(1)
        

def agentePapelYTabaco():
    global papel, tabaco
    while True:
        semaphoreAgente.acquire()
        papel.append(1)
        tabaco.append(1)
        

def agenteFosforosYTabaco():
    global tabaco, fosforos
    while True:
        semaphoreAgente.acquire()
        fosforos.append(1)
        tabaco.append(1)
        

        
        

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
           
        
           
            
            


agente1Hilo = threading.Thread(target=agentePapelYFosforos)
agente2Hilo = threading.Thread(target=agentePapelYTabaco)
agente3Hilo = threading.Thread(target=agenteFosforosYTabaco)
fumadorConPapelHilo = threading.Thread(target=fumadorConPapel)
fumadorConFosforosHilo = threading.Thread(target=fumadorConFosforos)
fumadorConTabacoHilo = threading.Thread(target=fumadorConTabaco)

agente1Hilo.start()
agente2Hilo.start()
agente3Hilo.start()
fumadorConPapelHilo.start()
fumadorConFosforosHilo.start()
fumadorConTabacoHilo.start()
