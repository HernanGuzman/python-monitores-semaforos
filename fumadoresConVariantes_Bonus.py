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
papel = False
fosforos = False
tabaco = False
cigarrillosArmados = []
cantidadEnMesa = []


def agentePapel():
    global papel, cantiadPuestasAgente1,  cantidadEnMesa
    while cantiadPuestasAgente1 > 0:
        if papel == False  and len(cantidadEnMesa) < 2: #Consulto si no hay papel en la mesa y sino hay dos tipos en la mesa
            semaphoreAgente.acquire()
            cantiadPuestasAgente1-=1
            papel = True
            cantidadEnMesa.append(1)
            semaphoreAgente.release()
            

def agenteTabaco():
    global  tabaco, cantiadPuestasAgente2, cantidadEnMesa
    while cantiadPuestasAgente2 > 0:
        if tabaco == False and  len(cantidadEnMesa) < 2:
            semaphoreAgente.acquire()
            cantiadPuestasAgente2-=1
            tabaco = True
            cantidadEnMesa.append(1)
            semaphoreAgente.release()

def agenteFosforos():
    global  fosforos, cantiadPuestasAgente3, cantidadEnMesa
    while cantiadPuestasAgente3 > 0:
        if fosforos == False and len(cantidadEnMesa) < 2:
            semaphoreAgente.acquire()
            cantiadPuestasAgente3-=1
            fosforos = True
            cantidadEnMesa.append(1)
            semaphoreAgente.release()

        
        

def ArmadorConPapel():
    while True:
        global fosforos, tabaco, cigarrillosArmados, cantidadEnMesa
        
        if fosforos == True and tabaco == True:     # si hay fósforos y tabaco en la mesa
            #TOMO LOS CIGARRILLOS
            fosforos = False
            tabaco = False             # tomarlos
            cigarrillosArmados.append(1)
            logging.info(f'Armador con Papel: Armando cigarrillo') # armar cigarrillo y fumar: se puede simular con un sleep
            time.sleep(2)
            cantidadEnMesa.pop()#saco de la mesa los dos productos
            cantidadEnMesa.pop()#saco de la mesa los dos productos
                     # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
            
            
        
            
            
            

def ArmadorConFosforos():
    while True:
        global papel,tabaco, cigarrillosArmados
        
        if papel == True and tabaco == True:        # si hay papel y tabaco en la mesa
            #TOMO LOS CIGARRILLOS
            papel = False                 # tomarlos
            tabaco = False               # tomarlos
            cigarrillosArmados.append(1)
            logging.info(f'Armador con Fosforos: Armando cigarrillo') # armar cigarrillo y fumar: se puede simular con un sleep
            time.sleep(2)
            cantidadEnMesa.pop()#saco de la mesa los dos productos
            cantidadEnMesa.pop()#saco de la mesa los dos productos
             # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
            
        
            
            
            

def ArmadorConTabaco():
    while True:
        global papel, fosforos, cigarrillosArmados
        
        if papel == True and fosforos == True:   # si hay fósforos y papel en la mesa
            #TOMO LOS CIGARRILLOS
            papel = False             # tomarlos
            fosforos = False          # tomarlos
            cigarrillosArmados.append(1)
            logging.info(f'Armador con Tabaco: Armando cigarrillo') # armar cigarrillo y fumar: se puede simular con un sleep
            time.sleep(2)
            cantidadEnMesa.pop()#saco de la mesa los dos productos
            cantidadEnMesa.pop()#saco de la mesa los dos productos
             # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar

def Fumador():
    while True:
        global cigarrillosArmados
        
        if len(cigarrillosArmados) > 0:   # si hay fósforos y papel en la mesa
            #TOMO LOS CIGARRILLOS
            cigarrillosArmados.pop()             # tomarlos
            logging.info(f'Fumador: Fumando cigarrillo') # armar cigarrillo y fumar: se puede simular con un sleep
            time.sleep(4)

agente1Hilo = threading.Thread(target=agentePapel)
agente2Hilo = threading.Thread(target=agenteTabaco)
agente3Hilo = threading.Thread(target=agenteFosforos)
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