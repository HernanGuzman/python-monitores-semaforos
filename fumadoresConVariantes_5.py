import random
import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)
semaphoreAgente = threading.Semaphore(1)

cantidadMaximaPapel = 2
cantidadMaximaFosforos = 1
cantidadMaximaTabaco = 2
cantiadPuestasAgente1 = 12
cantiadPuestasAgente2 = 11
cantiadPuestasAgente3 = 10
papel = []
fosforos = []
tabaco = []
cigarrillosArmados = []


def agentePapelYFosforos():
    global papel, fosforos, cantiadPuestasAgente1, cantidadMaximaPapel, cantidadMaximaFosforos  
    while cantiadPuestasAgente1 > 0:
        if len(papel) < cantidadMaximaPapel and len(fosforos) < cantidadMaximaFosforos:
            semaphoreAgente.acquire()
            cantiadPuestasAgente1-=1
            papel.append(1)
            fosforos.append(1)
            semaphoreAgente.release()
            

def agentePapelYTabaco():
    global papel, tabaco, cantiadPuestasAgente2, cantidadMaximaPapel, cantidadMaximaTabaco
    while cantiadPuestasAgente2 > 0:
        if len(papel) < cantidadMaximaPapel and len(tabaco) < cantidadMaximaTabaco:
            semaphoreAgente.acquire()
            cantiadPuestasAgente2-=1
            papel.append(1)
            tabaco.append(1)
            semaphoreAgente.release()

def agenteFosforosYTabaco():
    global tabaco, fosforos, cantiadPuestasAgente3, cantidadMaximaTabaco, cantidadMaximaFosforos
    while cantiadPuestasAgente3 > 0:
        if len(fosforos) < cantidadMaximaFosforos and len(tabaco) < cantidadMaximaTabaco:
            semaphoreAgente.acquire()
            cantiadPuestasAgente3-=1
            fosforos.append(1)
            tabaco.append(1)
            semaphoreAgente.release()

        
        

def ArmadorConPapel():
    while True:
        global fosforos, tabaco, cigarrillosArmados
        
        if len(fosforos) > 0 and len(tabaco) > 0:     # si hay fósforos y tabaco en la mesa
            #TOMO LOS CIGARRILLOS
            fosforos.pop()
            tabaco.pop()             # tomarlos
            cigarrillosArmados.append(1)
            logging.info(f'Armador con Papel: Armando cigarrillo') # armar cigarrillo y fumar: se puede simular con un sleep
            time.sleep(2)
                     # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
            
            
        
            
            
            

def ArmadorConFosforos():
    while True:
        global papel,tabaco, cigarrillosArmados
        
        if len(papel) > 0 and len(tabaco) > 0:        # si hay papel y tabaco en la mesa
            #TOMO LOS CIGARRILLOS
            papel.pop()                 # tomarlos
            tabaco.pop()                # tomarlos
            cigarrillosArmados.append(1)
            logging.info(f'Armador con Fosforos: Armando cigarrillo') # armar cigarrillo y fumar: se puede simular con un sleep
            time.sleep(2)
             # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
            
        
            
            
            

def ArmadorConTabaco():
    while True:
        global papel, fosforos, cigarrillosArmados
        
        if len(papel) > 0 and len(fosforos) > 0:   # si hay fósforos y papel en la mesa
            #TOMO LOS CIGARRILLOS
            papel.pop()             # tomarlos
            fosforos.pop()          # tomarlos
            cigarrillosArmados.append(1)
            logging.info(f'Armador con Tabaco: Armando cigarrillo') # armar cigarrillo y fumar: se puede simular con un sleep
            time.sleep(2)
             # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar

def Fumador():
    while True:
        global cigarrillosArmados
        
        if len(cigarrillosArmados) > 0:   # si hay fósforos y papel en la mesa
            #TOMO LOS CIGARRILLOS
            cigarrillosArmados.pop()             # tomarlos
            logging.info(f'Fumador: Fumando cigarrillo') # armar cigarrillo y fumar: se puede simular con un sleep
            time.sleep(4)

agente1Hilo = threading.Thread(target=agentePapelYFosforos)
agente2Hilo = threading.Thread(target=agentePapelYTabaco)
agente3Hilo = threading.Thread(target=agenteFosforosYTabaco)
ArmadorConPapelHilo = threading.Thread(target=ArmadorConPapel)
ArmadorConFosforosHilo = threading.Thread(target=ArmadorConFosforos)
ArmadorConTabacoHilo = threading.Thread(target=ArmadorConTabaco)
FumadorHilo = threading.Thread(target=Fumador)

agente1Hilo.start()
agente2Hilo.start()
agente3Hilo.start()
ArmadorConPapelHilo.start()
ArmadorConFosforosHilo.start()
ArmadorConTabacoHilo.start()
FumadorHilo.start()