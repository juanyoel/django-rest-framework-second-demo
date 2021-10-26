# django-rest-framework-second-demo

## CURSO AVANZADO

## INSTALACION

* Creamos la app con el comando *django-admin start project [nombreProyeto]*
* Nota --> Cuando tenemos varias aplicaciones es conveniente tener una app core que vincule todas, en ella es como tener las migraciones y otros archivos comunes.
* Creamos entonces la app core con el comando *python manage.py startapp core*
* Como la app core solo la usaremos para guardar BD, y relaciones entre las demás apps, no necesitamos ni los archivos *test.py* y *views.py* podemos eliminarlos.
* Creamos la carpeta tests, dónde guardaremos todos los test de nuestro proyecto.
* Dentro de la carpeta anterior creamos el archivo __init.py__ que es dónde finalmente tendremos los tests.


## MODELO USUARIO
* Ya con todas las especificaciones anteriores listas pasamos a crear nuestro modelo de usuario, que será personalizado.
* Cuando se trabaja con desarrollo basados en test, primero se implementa el test y luego el modelo.
* Ponemos nuestra app core en las aplicaciones instaladas.

![image](https://user-images.githubusercontent.com/84333525/138892775-93fbe2bf-efa1-4c66-b896-941e03b3e863.png)

* Creamos un nuevo archivo en nuestra app *test_models.py* lo que vamos a usar para testear que la función helper de nuestro modelo pueda crear un nuevo usuario.

![image](https://user-images.githubusercontent.com/84333525/138894933-cb5ad3cd-0047-42f0-b0cb-5b66de3c8225.png)

* Corremos el test aunque sabemos que al no tener un modelo configurado igual mostrará error, lo hacemos con el comando *python manage.py test*
* Seguidamente vamos a crear nuestro modelo de usuario en el archivo *models.py*

![image](https://user-images.githubusercontent.com/84333525/138896073-285ce782-7e46-4813-9389-40daa3d0b6f6.png)

  -Hacemos las importanciones necesarias que nos permitirán crear un modelo de usuario personalizado:
    * Creación de usuario: AbstractBaseUser
    * Creación de administración: BaseUserManager
    * Creación de permisos: PermissionsMixin

* Primero creamos nuestro user manager, que es el encargado de proveer las funciones helpers para la creación de usuarios.

![image](https://user-images.githubusercontent.com/84333525/138897621-3128ed1a-d408-4637-99da-dce40a5b3674.png)

  - En este caso le pasamos como argumento el email, el password en este caso igual None debido a que no requerimos de que para crear un usuario tenga que tener una contraseña, a diferencia del usuario manager que si debe tener, y por último **extra_fields** es para guardar campos que se vayan incorporando y no tenemos que estar adicionandolos manualmente.
  - Para la contraseña usamos la propiedad *user.set_password(password)* porque no podemos guardar la contraseña en texto plano y con esto la convertimos a un hash.
 
 * Creamos un modelo de usuario personalizado, porque es una buena práctica que el login se haga con el email no con el usuario.
 
 ![image](https://user-images.githubusercontent.com/84333525/138901278-136bf960-93cf-4e5f-8ffb-a95745380cff.png)

 - Con esta linea *USERNAME_FIELD = 'email'* le decimos a Django que queremos hacer login con email.

* Lugo debemos configurar el archivo *settings.py* para decirle a Django que usemos ese modelo para cualquier acción que necesite autenticación
  Para ello adicionamos el siguiente comando: --> 
  
  ![image](https://user-images.githubusercontent.com/84333525/138901983-b77ee5a3-c5fe-4f86-80be-ea5d9bee2e46.png)

### Cuando ya terminamos de trabajar con los modelos siempre se deben crear y correr las migraciones
  * python manage.py makemigrations
  * python manage.py migrate
  
## NORMALIZAR LOS CORREOS ELECTRONICOS
* Como estamos trabajando con una metodologí en base de pruebas, primero creamos la prueba correspondiente a la normalización del correo y verificamos que funcione, para ellos agregamos esta función en el archivo *test_models.py*

![image](https://user-images.githubusercontent.com/84333525/138905756-f4be2332-ccdb-42cf-b47d-d878da818cfb.png)

* Al correr el test como es lógico nos damos cuenta de que obtenemos error debido a que aún en el modelo no hemos normalizado el correo, para solucionar este problema sencillamente adicionamos la siguiente línea:

![image](https://user-images.githubusercontent.com/84333525/138907730-bb524c95-3e99-47a9-a15f-8556a2936ee4.png)

* Actualizamos nuestro test para evaluar si un email es inválido:

![image](https://user-images.githubusercontent.com/84333525/138908346-310e693e-4370-43cf-a895-0d39869b8d51.png)

* Para dar solución a esto simplemente adicionamos la verficación en la creación del modelo usuario

![image](https://user-images.githubusercontent.com/84333525/138908796-b60dafe3-d269-42f2-ac8b-de529f3e9f29.png)

## CREAR SUPER USUARIO
* Adicionamos primero el test

![image](https://user-images.githubusercontent.com/84333525/138909993-f64f7f29-71bb-413c-9fcb-275536517855.png)

* Adicionamos luego la funcionalidad para crear el super usuario:

![image](https://user-images.githubusercontent.com/84333525/138910810-2af0d96e-8b66-4808-bf46-0445a34a78fb.png)

## ADICIONAR NUESTROS MODELOS AL AREA DE ADMIN
* Adicionar nuestros modelos a nuestra área de admin, nos permite trabajar comodamente con los mismos al poder crear, actualizar y eliminar instancias de los mismos.
* Como estamos programando basado en pruebas debemos crear un nuevo archivo para las funcionalidades que vamos a crear en el área de administración, por lo que creamos un nuevo archivo *test_admin.py* en la carpeta *tests*.
* Lo primero que tenemos que hacer es crear la función setUp() debido a que es la que crea los elementos necesarios para definir las otras funciones de test. Es obligatorio crear esta función, porque es dónde creamos a los usuarios con los que se estarán realizando las pruebas.

![image](https://user-images.githubusercontent.com/84333525/138914581-1ec93d8c-b9a5-48a3-b0ac-444913fd54db.png)

* En el test *test_user_listed* usamos la función *reverse*, funciona pasandole entre comillas el app que queremos: el url que queremos lo cual genera el url para la lista de usuarios que tenemos, usamos esta función en vez de escribir el url manualmente, por si en algún momento queremos cambiar el url la función reverse se encarga del resto.

![image](https://user-images.githubusercontent.com/84333525/138915935-d531c27d-6355-4a14-bba5-e36476564192.png)

* Luego ya podemos modificar el archivo *admin.py* para poder trabajar con el usuario modificado.
  - Importamos *from django.contrib.auth.admin import UserAdmin as BaseUserAdmin*
  
  ![image](https://user-images.githubusercontent.com/84333525/138917051-d90ee044-2246-40dc-be5b-31c2b6189d0d.png)


* Actualizamos nuestro admin de djando para poder soportar cuando actualizamos nuestro modelo de usuario. (Porque la página de usuario no va a funcionar aún).
* Para ello creamos otro test --> 

![image](https://user-images.githubusercontent.com/84333525/138918147-250e1184-335d-455d-8621-30843fd2a6cc.png)

* Al correr test obtenemos error debido a que aún debemos customizar un poco más el archivo *admin.py*
  
  ![image](https://user-images.githubusercontent.com/84333525/138919417-f1b90dc0-2bee-4cf7-9752-e31ec4633ad1.png)

 - El símbolo '_' es para hacer el texto entendible humano, para ello importamos *from django.utils.translation import gettext as _*

* Por último necesitaomos crear un test más el de *LA PAGINA PARA AGREGAR USUARIOS*
  
  ![image](https://user-images.githubusercontent.com/84333525/138920726-e70ba443-ba6d-4a27-b90b-99440bf7ba4d.png)

* Al correr los test obtenemos un error en este punto debido a que debemos agregar la función para agregar usuarios *admin.py*
  - Para ello podemos usar add_fields que es un preset que tiene Django en su documentación se encuentra.
  
  ![image](https://user-images.githubusercontent.com/84333525/138939392-699d40eb-053d-438e-b042-fac0f1f48c0f.png)

## CREACION DE ENDPOINTS PARA MANEJAR USUARIOS
* Esto nos va a permitir CRUD de usuarios y todo lo que queramos hacer con ellos ....
* Hasta el momento lo que hemos logrado es la administración en si de los usuarios, para su gestión crearemos una app user, con la cual van interactuar las demás apps que tengamos en el proyecto.
* De la nueva app user que creamos, podemos eliminar varios archivos que queremos mantener en core, como son los models.py, migrations.py, test.py en caso de este creamos una carpeta tests y dentro es que crearemos los test, ...etc
* Luego adicionamos nuestra app a los settings.py de nuestra app:

![image](https://user-images.githubusercontent.com/84333525/138943594-83a88d30-085a-44c3-8c64-60039f2d9cc3.png)

### API PARA CREAR USUARIOS
* Como estamos programando basado en pruebas primero creamos el test para crear usuario. Esto lo hacemos en el archivo *test_user_api.py*
* Después de hacer las importanciones necesarias que veremos en las próximas imágenes
* Creamos una función helper para nuestro url
* Importante --> Dividiremos los test para más organización en los públicos y privados. Por ejemplo uno público podría ser la creación de un usuario y uno privado puede ser un update del usuario.

1. Creamos el serializador para el usuario *serializer.py*
   
   ![image](https://user-images.githubusercontent.com/84333525/138951871-d1c0c25e-24b5-4bd1-9051-447b1505f63b.png)

2. Creamos la view en *views.py*

  ![image](https://user-images.githubusercontent.com/84333525/138952372-048b948f-398a-476b-8c6d-4c5d32e0a9c7.png)

3. Creamos la url con la que vamos acceder a la view en el archivo *urls.py* (tenemos que crearlo)
    - Siempre que definismos urls tenemos que decir para que app, por eso la variable app_name

   ![image](https://user-images.githubusercontent.com/84333525/138952979-92fa423b-742d-439b-ac5b-1ecdfd3f82c9.png)

4. Creamos la url en el archivo *urls.py* del proyecto.

  ![image](https://user-images.githubusercontent.com/84333525/138954895-b58c6659-862d-4989-8a2f-a0f16859fe72.png)

### AUTENTICACION POR TOKEN
* La autenticación que utilizaremos es por token, así verificamos cuando el usuario haga request que es el usuario ...
1. Adicionamos la url

![image](https://user-images.githubusercontent.com/84333525/138955871-ea5594e7-fb2c-422a-811d-b646ae78d953.png)


