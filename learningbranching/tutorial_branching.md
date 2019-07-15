**Espacio de definición institucional - ISFDyT210**
**Ejercicio Complementario sobre LearningBranching**

**Branching -Definición**
 Para entender realmente cómo ramifica Git, previamente hemos de examinar la forma en que almacena sus datos. Git no los almacena de forma incremental (guardando solo diferencias), sino que los almacena como una serie de instantáneas (copias puntuales de los archivos completos, tal y como se encuentran en ese momento). En cada confirmación de cambios (commit),  Git almacena un punto de control que conserva: 
 un apuntador a la copia puntual de los contenidos preparados (staged), 
 unos metadatos con el autor y el mensaje explicativo,
 y uno o varios apuntadores a las confirmaciones (commit) que sean padres directos de esta (un padre en los casos de confirmación normal, y múltiples padres en los casos de estar confirmando una fusión (merge) de dos o más ramas).

**Tarea**
Crear una rama nueva de nombre "Branching" y moverse a ella.

```sh
$ git checkout -b branching
```
Luego, crear una carpeta de nombre "LearningBranching", para finalmente, crear dentro este material introductorio y agregar todo al área de seguimiento.

```sh
$ mkdir learningbranching
$ nano tutorial_branching
$ git add .
```
Al completar estos pasos, volver a la rama master y realizar un merge.
```sh
$ git checkout master
$ git merge branching
```
