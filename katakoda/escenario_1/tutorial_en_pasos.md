# KATAKODA ESCENARIO 1
**PASO 1**
Para almacenar un directorio bajo el control de versiones necesita crear un repositorio. Con Git inicializa un repositorio en el directorio de nivel superior para un proyecto.

**TAREA**
Como este es un nuevo proyecto, se necesita crear un nuevo repositorio. Utilice el comando git init para crear un repositorio.

```sh
$ git init
```

**PROTIP**
Después de inicializar un repositorio, se crea un nuevo subdirectorio oculto llamado .git. Este subdirectorio contiene los metadatos que Git utiliza para almacenar su información. Si está interesado en los detalles, use la línea de comandos para explorar los contenidos.

**PASO 2 - ESTADO  GIT**
Cuando un directorio forma parte de un repositorio, se denomina Directorio de trabajo. Un directorio de trabajo contiene la última versión descargada del repositorio junto con cualquier cambio que aún no se haya confirmado. Mientras trabaja en un proyecto, todos los cambios se realizan en este directorio de trabajo.

Puede ver qué archivos han cambiado entre su directorio de trabajo y lo que se ha confirmado previamente en el repositorio con el comando git status.

La salida de este comando se denomina "estado del árbol de trabajo".

```sh
$ git status
```

**Protip**
Todos los archivos están "sin seguimiento" por Git hasta que se indique lo contrario. Los detalles de cómo se trata en el siguiente paso.

