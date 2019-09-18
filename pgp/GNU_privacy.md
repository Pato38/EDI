### GNU Privacy Guard
GnuPG es un programa de software de cifrado híbrido, que utiliza una combinación de criptografía de clave simétrica convencional para mayor velocidad y criptografía de clave pública para facilitar el intercambio seguro de claves, generalmente, mediante el uso de la clave pública del destinatario, para cifrar una clave de sesión que se usa solo una vez. Este modo de operación es parte del estándar OpenPGP y ha sido parte de PGP desde su primera versión.

**Cifrado asimétrico**

GnuPG cifra los mensajes utilizando pares de claves asimétricas generadas individualmente por los usuarios de GnuPG. Las claves públicas resultantes, pueden intercambiarse con otros usuarios de varias maneras, como los servidores de claves de Internet. Siempre deben hacerse cuidadosamente, para evitar la suplantación de identidad corrompiendo las correspondencias de identidad de "propietario" de clave pública. También es posible agregar una firma digital criptográfica a un mensaje, de modo que se pueda verificar la integridad del mensaje y el remitente.

**Anillos de claves (keyring)**

El keyring es el deposito donde se almacenan todas las claves GPG, tanto públicas como privadas. Cuando recibimos una clave pública de otra persona, ésta deberemos incluirla en nuestro keyring o anillo de claves, que es el lugar donde se almacenan todas las claves públicas de las que disponemos. Para incluir estas claves públicas de otras personas, lo haremos de la siguiente forma:
   ```sh
$ gpg --import clavepublica.asc 
 ```

donde clavepublica.asc es el nombre del archivo recibido con la clave pública. 
Una vez que hemos importado la clave, podemos verificar el contenido de nuestro keyring con la opción

 ```sh
-kv: $ gpg -kv
 ```

**Servidores de claves (keyservers)**

Un Servidor de claves es un servidor en el que se almacenan claves públicas. Se puede buscar la clave pública de una persona en el servidor mediante el nombre. Una vez obtenida la clave, se puede utilizar para enviar mensajes cifrados al dueño de la clave pública o bien para comprobar la firma digital de un mensaje enviado por el dueño de la misma. 

#### Instalación y configuración PGP
1. **Instalación**
    ```sh
    $ sudo apt install pgp
    ```

2. **Generación de clave e identificación personal**
   Para crear una clave PGP nueva:

    Seleccione Archivo ▸ Nuevo….

    Seleccione clave PGP en la lista y pulse Continuar.

    Introduzca su nombre completo en el campo Nombre completo.

    Opcionalmente, puede añadir su dirección de correo-e y un comentario para describir la clave.

    Pulse Crear.

    En el diálogo de contraseñas, introduzca una contraseña para la clave. Vuelva a escribir la contraseña para confirmarla.

    Pulse Aceptar para terminar.


```sh
    $ sudo gpg --gen-key
```

3. **Exportar nuestra Public Key**
  
  Para exportar su clave PGP pública

   Seleccione el depósito claves GnuPG en el panel lateral izquierdo.

   Seleccione de la lista la clave PGP personal PGP que exportar.

   Seleccione Archivo ▸ Exportar….

   Para guardar las claves en formato ASCII, seleccione Claves PGP blindadas en el menú de encima del botón Exportar.

   elija una ubicación para el archivo de claves y pulse Exportar para terminar.


```  sh
    $ gpg --armor --export you@exammple.com > mykey.asc
```

4. **Crear servidor basico para que un compañero pueda descargarla**

    Crea un servidor en la carpeta actual al que todos tendran acceso por su IP y puerto específico.
    ```sh
    $ python2 -m SimpleHTTPServer 80
    ```
    ```sh
    $ python3 -m http.server 80
    ```
    Luego para obtener su IP debe tipear en su terminal 
    ```sh
    $ ip a
    ```
    Finalmente si desea descargar el archivo mykey.asc, su colega debe tipear
    ```sh
    $  wget nuestra_ip:puerto/mykey.asc
    ```
    *Nota: El comando wget sin especificar la ruta del archivo, descargará todo el contenido de la carpeta que se utilizo para montar el servidor http.
    
    
5. **Verificar que el archivo contenga la key**

    Hacemos uso del comando cat para ver su contenido
    ```sh
    $  cat mykey.asc
    ```

6. **Importar una Public Key**

  	Importar una clave pública es tan fácil como exportarla. Cuando importa una clave pública, tiene que descifrar el mesaje recibido y controlar la firma digital de dicha clave.

     Una de las maneras más sencillas de importar una clave es descargar o grabarla de un sitio Web. 

     Después de descargarla, use el comando 

    ```sh
    $ gpg --import mykey.asc
    ```
    para añadirla

7. **Comprobar importación**

    Este comando nos permitirá ver la lista de keys disponibles en nuestro terminal.
    ```sh
    $ gpg --list-key
    ```

8. **Eliminar una Key del almacen de claves**

    Primero debemos eliminar la secret key de dicha clave mediante su dirección o primeros 8 digitos.
    ```sh
    $ sudo gpg --delete-secret-key 00AA11BB
    $ sudo gpg --delete-secret-key email@dominio.com
    ```
     Luego debemos eliminar su public key
    ```sh
    $ sudo gpg --delete-key 00AA11BB
    $ sudo gpg --delete-key email@dominio.com
    ```

9. **Enviar un archivo encryptado para que solo su receptor pueda descifararlo con su private key**

    Creamos nuestro archivo y redactamos le mensaje deseado (En caso de que el archivo exista, saltear este paso).
  ```sh
    $ nano holamundo.txt
  ```
 
  Luego encriptamos y enviamos con el siguiente comando (recordar example@dominio.com permitira buscar y tomar la key en nuestor terminal con dicho correo o bién podemos hacer uso de los primeros 8 digitos)
  
```sh 
    $ gpg --output holamundo.txt.gpg --encrypt
    --recipient example@dominio.com holamundo_encryptado.txt
```

```sh 
    $ gpg --output holamundo.txt.gpg --encrypt --recipient 00AA11BB holamundo_encryptado.txt
  ```
    
   
 *Nota: El segundo "holamundo.txt" se guardará en el lugar de trabajo del terminal con el documento original ya encriptado.
    
10. **Desencriptando documento encriptado**
    Nos pedirá la contraseña (la que introdujo en este caso el propietario de la public key cuando generó su par de claves). Una vez ingresada ya podremos leer el documento.
    ```sh 
    $ sudo --output holamundo.txt --decrypt holamundo.txt.gpg 

