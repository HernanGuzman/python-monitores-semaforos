# Cigarrillos y fumadores

Un cigarrillo necesita de papel, tabaco y fósforos para ser preparado y fumado. Hay tres fumadores, y cada uno tiene un único ingrediente al que puede acceder todo el tiempo: papel, tabaco o fósforos. Un agente coloca sobre la mesa al azar dos ingredientes, y el correspondiente fumador debe darse cuenta, tomarlos, armar el cigarrillo y fumarlo. Luego el agente vuelve a colocar al azar sobre la mesa dos ingredientes, y así se sigue.

1. Usar `fumadores.py` como base para sincronizar el agente y los fumadores.
1. ¿Hay alguna sección crítica?
No, no hay seccion crítica. Lo que se debe realizar es sicronizar a los fumadores.
1. En vez de con flags que den cuenta si hay o no tal cosa en la mesa, realice una versión con listas. Por ejemplo `listaPapel` si no está vacía es porque hay papel (la puede llenar con cualquier cosa, con 1s por ejemplo).
Resuelto en el archivo fumadoresConListas.py

## Bonus: variantes 

Como base para empezar, siempre se puede tomar la solución original. Luego de eso, si se anima, puede mezclar dos o más ítems entre sí (según tenga sentido hacerlo).

* Que haya tres agentes, y no una solo, uno por cada par de ingredientes. Compiten entre sí para entrar a la mesa y poner sus dos respectivos ingredientes.
Resuelto en el archivo fumadoresConVariantes_1
* Que la cantidad de veces que el agente pone ingredientes en la mesa sea acotada.
Resuelto en el archivo fumadoresConVariantes_2
* Que puedan haber en la mesa hasta un máximo de dos por cada ingrediente.
Resuelto en el archivo fumadoresConVariantes_3
* Que puedan haber en la mesa hasta un máximo de dos por cada ingrediente, salvo para fósforos que sea un máximo de uno.
Resuelto en el archivo fumadoresConVariantes_4
* Que los tres fumadores solamente ahora sean armadores de cigarillos, y que haya cuarto y único fumador. Como fumar es más lento que armar (poner los `sleep` para que se simule esto), entonces que haya una cantidad acotada de cigarrillos armados sin fumar.
Resuelto en el archivo fumadoresConVariantes_5

## Bonus extra

* Que haya un agente por cada ingrediente, compitiendo todo el tiempo para poner su correspondiente ingrediente sobre la mesa, y que en la mesa haya a lo sumo dos ingredientes. Cuando en la mesa hay dos ingredientes pasa igual que en la situación original: el correspondiente fumador toma los dos ingredientes, arma el cigarrillo y fuma. Luego de nuevo los tres agentes compiten para poner dos ingredientes, etc.
Resuelto en el archivo fumadoresConVariantes_Bonus