import random
import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)
semaphoreAgente = threading.Semaphore(1)

papelEnMesa = False
fosforosEnMesa = False
tabacoEnMesa = False

def agente():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        semaphoreAgente.acquire() # esperar a reponer las cosas una vez que alguien haya tomado las dos anteriores
        caso = random.choice([0,1,2]) #al azar pone dos cosas en la mesa
        if caso == 0:
            papelEnMesa = True
            tabacoEnMesa = True
        if caso == 1:
            papelEnMesa = True
            fosforosEnMesa = True
        if caso == 2:
            fosforosEnMesa = True
            tabacoEnMesa = True
        
        

def fumadorConPapel():
    while True:
        global fosforosEnMesa
        global tabacoEnMesa
        if fosforosEnMesa and tabacoEnMesa:     # si hay fósforos y tabaco en la mesa
            #TOMO LOS CIGARRILLOS
            fosforosEnMesa = False              # tomarlos
            tabacoEnMesa = False
            logging.info(f'Fumador con Papel: Armando y fumando cigarrillo') # armar cigarrillo y fumar: se puede simular con un sleep
            time.sleep(1)
            semaphoreAgente.release()           # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
            
            
        
            
            
            

def fumadorConFosforos():
    while True:
        global papelEnMesa
        global tabacoEnMesa
        if papelEnMesa and tabacoEnMesa:        # si hay papel y tabaco en la mesa
            #TOMO LOS CIGARRILLOS
            papelEnMesa = False                 # tomarlos
            tabacoEnMesa = False                # tomarlos
            logging.info(f'Fumador con Fosforos: Armando y fumando cigarrillo') # armar cigarrillo y fumar: se puede simular con un sleep
            time.sleep(1)
            semaphoreAgente.release() # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
            
        
            
            
            

def fumadorConTabaco():
    while True:
        global papelEnMesa
        global fosforosEnMesa
        if fosforosEnMesa and papelEnMesa:  # si hay fósforos y papel en la mesa
            #TOMO LOS CIGARRILLOS
            papelEnMesa = False             # tomarlos
            fosforosEnMesa = False          # tomarlos
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

