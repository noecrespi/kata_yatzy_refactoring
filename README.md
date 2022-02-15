# Yatzy Refactoring Kata

El objetivo de este kata es refactorizar el código del juego del yatzy.

**Kata readme by [Emily Bache](https://github.com/emilybache)** 

[Emily Bache kata repo](https://github.com/emilybache/Yatzy-Refactoring-Kata)

*Diseñado por Jon Jagger. Está disponible en su Cyber-Dojo. [ Publicación de blog](http://jonjagger.blogspot.co.uk/2012/05/yahtzee-cyber-dojo-refactoring-in-java.html)*

**Texto sacado de [dfleta](https://github.com/dfleta/yatzy-refactoring-kata)**



##  Kata: Reglas de Yatzy
---

El juego de Yatzy es un simple juego de dados. Cada jugador
lanza cinco dados de seis caras. Pueden volver a tirar algunos o todos
de los dados hasta tres veces (incluida la tirada original).

Por ejemplo, supongamos que un jugador tira:

    3,4,5,5,2
    
Mantienen (-,-,5,5,-) y vuelven a tirar (3,4,-,-,2):

    5,1,5,5,3

Mantienen (5,-,5,5,-) y vuelven a tirar (-,1,-,-,3):

    5,6,5,5,2

Luego, el jugador coloca la tirada en una categoría, como unos,
dos, cinco, par, dos pares, etc. (ver más abajo). Si el rollo es
compatible con la categoría, el jugador obtiene una puntuación para el
rodar de acuerdo con las reglas. Si el rollo no es compatible
con la categoría, el jugador anota cero para la tirada.

Por ejemplo, supongamos que un jugador anota 5,6,5,5,2 en los cincos
categoría ellos anotarían 15 (tres cincos). la puntuación para
ese ir se agrega a su total y la categoría no puede
utilizarse de nuevo en los restantes va para ese juego.
Un juego completo consta de una oportunidad para cada categoría. Así, por
su última oportunidad en un juego, un jugador debe elegir su única
categoría restante.

Su tarea es anotar una tirada DADA en una categoría DADA.
NO tienes que programar el lanzamiento aleatorio de dados.
El juego NO se juega dejando que la computadora elija el
categoría de puntuación más alta para una tirada determinada.
  

##  Kata: categorías Yatzy y reglas de puntuación
---

###  Probabilidad:
El jugador anota la suma de todos los dados, sin importar lo que lea.
Por ejemplo:
  
-    1,1,3,3,6 colocado en "casualidad" puntúa 14 (1+1+3+3+6)
-    4,5,5,6,1 colocado en "casualidad" puntúa 21 (4+5+5+6+1)  

###  Yatzy:
Si todos los dados tienen el mismo número,
el jugador anota 50 puntos.
Por ejemplo:
  
-    1,1,1,1,1 colocado en "yatzy" puntúa 50
-    1,1,1,2,1 colocado en "yatzy" puntúa 0

###  Unos, dos, tres, cuatro, cinco, seis:
El jugador anota la suma de los dados que lee uno,
dos, tres, cuatro, cinco o seis, respectivamente.
Por ejemplo:

-    1,1,2,4,4 colocados en "cuatro" puntúa 8 (4+4)
-    2,3,2,5,1 colocado en "dos" puntúa 4 (2+2)
-    3,3,3,4,5 colocados en "unos" puntuaciones 0

###  Pareja:
El jugador anota la suma de los dos dados iguales más altos.
Por ejemplo, cuando se coloca en "par":
  
-    3,3,3,4,4 puntuaciones 8 (4+4)
-    1,1,6,2,6 puntuaciones 12 (6+6)
-    3,3,3,4,1 puntuaciones 6 (3+3)
-    3,3,3,3,1 puntuaciones 6 (3+3)

###  Dos pares:
Si hay dos pares de dados con el mismo número, el
jugador anota la suma de estos dados.
Por ejemplo, cuando se coloca en "dos pares":
  
-    1,1,2,3,3 puntuaciones 8 (1+1+3+3)
-    1,1,2,3,4 puntuaciones 0
-    1,1,2,2,2 puntuaciones 6 (1+1+2+2)

###  Trío:
Si hay tres dados con el mismo número, el jugador
anota la suma de estos dados.
Por ejemplo, cuando se coloca en "tres de una clase":
    
-     3,3,3,4,5 puntuaciones 9 (3+3+3)
-     3,3,4,5,6 puntuaciones 0
-     3,3,3,3,1 puntúa 9 (3+3+3)

###  Cuatro iguales:
Si hay cuatro dados con el mismo número, el jugador
anota la suma de estos dados.
Por ejemplo, cuando se coloca en "four of a kind":
  
-     2,2,2,2,5 puntúa 8 (2+2+2+2)
-     2,2,2,5,5 puntuaciones 0
-     2,2,2,2,2 puntúa 8 (2+2+2+2)

###  Pequeña recta:
Cuando se coloca en "pequeña escalera", si los dados dicen

   1,2,3,4,5,
   
el jugador anota 15 (la suma de todos los dados).

###  Gran recta:
Cuando se coloca en "escalera grande", si los dados dicen

   2,3,4,5,6,
   
el jugador anota 20 (la suma de todos los dados).

###  Casa llena:
Si los dados son dos de una clase y tres de una clase, el
jugador anota la suma de todos los dados.
Por ejemplo, cuando se coloca en "casa llena":
   
-     1,1,2,2,2 puntúa 8 (1+1+2+2+2)
-     2,2,3,3,4 puntuaciones 0
-     4,4,4,4,4 puntuaciones 0