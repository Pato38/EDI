**¿Cómo funciona Branching?**
Como ya hemos explicado, un Branch es una rama.
Es decir, dentro de nuestro sistema de control de versiones podemos ver el histórico de cambios como si de un árbol se tratase. De esta forma podemos ir abriendo ramas que parten bien de la rama principal (master) o de otra rama (branch).
La principal utilidad que tienen los branch es la de organizar nuestro trabajo, por ejemplo:

1-para desarrollar una nueva funcionalidad sin afectar al master mientras lo hacemos.
2-para hacer un hotfix (parcha rápido-Generalmente se crean estas revisiones para solucionar un problema específico de los usuarios del programa),en una versión que ya ha salido a producción.
3-para hacer un branch de producción, otro de pre, otro de testing, … y así ir promoviendo los cambios de uno a otro.

**Principales comandos**

Para crear una nueva rama de trabajo 

```
$  git branch (nombre de la rama)
```


Con esto creamos una nueva rama, pero si estamos posicionados (*) en el master, para movernos hacia la rama:
```
$ git checkout (nombre de la rama)
```
Sirve para moverse entre ramas por ejemplo si queremos movernos 3 commits hacia arriba:
```
git checkout HEAD ^3
```


Para crear un branch y movernos a él:
```
$ git checkout -b
```
Dentro de la nueva rama podemos hacer commits: 
```
$ git commit
```
Los commits, son los cambios que hacemos en el proyecto.
Si queremos incorporar los cambios realizados en el branch a nuestro master podemos realizar una fusión con :
```
$ git merge (nombre de la rama)
```
Así fusionamos los códigos del master y los de la rama.
Ahora en el branch master tenemos todos los cambios que hicimos sobre nuestro branch, por lo que podemos hacer un push para subirlos al repositorio central (como por ejemplo GitHub).

git rebase es el proceso de mover o combinar una secuencia de confirmaciones a una nueva confirmación base.
Git rebase básicamente lo que hace es recopilar uno a uno los cambios confirmados en una rama, y reaplicarlos sobre otra. Sobreescribe el commit:
```
$ git rebase
```
Otro de los comandos es git-cherry-pick - Aplica los cambios introducidos por algunos commits existentes 
```
$ git-cherry-pick
```
git cherry-pick, puede ser útil para deshacer cambios. Por ejemplo, digamos que un commit se hace accidentalmente en la rama incorrecta. Puede cambiar a la rama correcta y seleccionar el commit nuevamente.

El git revert, en cambio, se utiliza para deshacer los cambios en el historial de confirmación de un repositorio. Es importante entender que git revert deshace un solo commit.
En caso de que queramos borrar un commit que ya hemos subido al servidor remoto, la mejor opcion es realizar un nuevo commit que borre el commit que queremos eliminar utilizando el comando revert.
```
$ git revert HEAD
```

El git reset es una herramienta compleja y versátil para deshacer cambios. Si queremos borrar el último commit (siempre que no se haya subido al repositorio remoto) 
```
$ git reset --hard HEAD~1
```
Con esta opción estamos indicando que retrocedemos al comit HEAD~1 y perdemos todas las confirmaciones posteriores. 
Si no queremos perder los cambios posteriores
```
git reset --soft HEAD~1
```
Con esta opción estamos indicando que retrocedemos al commit HEAD~1 y no perdemos los cambios de los commits posteriores. Todos los cambios aparecerán como pendientes para realizar un commit.

git status nos muestra cómo está el repertorio
```
$ git status
```
Para enviar nuestro código y crear un repositorio remoto debemos hacerlo con 

```
$ git push
```
Para empezar el seguimiento de un nuevo archivo se usa el comando 
```
$ git add
```
