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

### CREAR API
1. Debemos serializar el token de autenticación, lo usamos para autenticar nuestros request.
2. Importamos authenticate:

![image](https://user-images.githubusercontent.com/84333525/138975215-8e7acfa8-dbf7-4c0f-8051-69a0035d2005.png)

A esto le pasamos un usuario y una contraseña y nos ayuda con el proceso de autenticación

![image](https://user-images.githubusercontent.com/84333525/138975347-bc0a7f02-74a7-4828-b43e-e9198cd80fc8.png)

(Internacionalización)

3. Luego creamos la clase y código necesario:

![image](https://user-images.githubusercontent.com/84333525/138975849-8c9a80ae-ffea-4d53-8ac9-7761d30230cb.png)

### CREAMOS EL VIEW PARA LA AUTENTICACION

![image](https://user-images.githubusercontent.com/84333525/138976273-3ef1fde1-c46f-4e0d-bbdf-410d20981e45.png)

### CREAMOS LA URL

![image](https://user-images.githubusercontent.com/84333525/138977516-cf0128c4-b665-4195-824f-c2f5f2a13dc0.png)

### AGREGAMOS EL MANAGE USER ENDPOINT
* Este endpoint va a permitir al usuario que ya ha sido autenticado el poder actualizar su perfil, cambiar su nombre, email y contraseña.

1. Creamos los test en el archivo *test_user_api.py*, la clase dónde estarán los métodos para testear los endpoints privados.

  - ![image](https://user-images.githubusercontent.com/84333525/138977954-db9e0df8-477e-4e79-a7ed-a7850c59fe0f.png)
  
  - ![image](https://user-images.githubusercontent.com/84333525/138978461-c378f721-ec7e-4683-b2e7-2ba8f93a12ec.png)

2. Creamos todos los tests

  ![image](https://user-images.githubusercontent.com/84333525/138979558-b0e432d2-0584-4ece-8ced-c356d9dbcb57.png)

### PASAMOS A CREAR NUESTRO MANAGE USER ENDPOINT
* En la vista hacemos nuevas importaciones

![image](https://user-images.githubusercontent.com/84333525/138979778-3e51b089-cd34-4ddb-90c9-460925ac7c7a.png)

* Creamos el APIView correspondiente para manejar la actualización de usuarios
  
![image](https://user-images.githubusercontent.com/84333525/138980334-8a02f8cc-bc97-4e26-a9d3-9cf9ea01542e.png)

* Actualizamos nuestr user serializer y le adicionamos el método update

![image](https://user-images.githubusercontent.com/84333525/138980842-cdcfe2aa-2aee-45ce-94cc-e22ee8f7bf72.png)

* Agregamos la url para tener accesos a la view

![image](https://user-images.githubusercontent.com/84333525/138980950-b16d9f11-6ebb-4567-a1d1-e51a7482ea1c.png)

********************************************************************************************************************************************************************************

# CREAMOS APP PARA LAS RECETAS
* *py.exe .\manage.py startapp recipe*
* Eliminamos los archivos que no vamos a necesitar (admin, migrations, models)
* Adicionamos la nueva app a las installed_apps en settings

## CREACION DEL TEST
* Luego definimos las pruebas test para las nuevas funcionalidades
  - Antes creamos una función con el propósito de crear un usuario de pruebas para las nuevas funcionalidades.

  ![image](https://user-images.githubusercontent.com/84333525/138988424-01cff513-915b-473b-afbb-06fd65de32ec.png)

  - Primer test
  ![image](https://user-images.githubusercontent.com/84333525/138989697-cfb606fa-7750-4ebf-a256-98e82cfbe65a.png)

* Luego que corremos el test verificamos que nos dice que no tenemos un Tag creado por lo que pasamos a crear el modelo.

## CREACION DEL MODELO
* Importamos los settings

![image](https://user-images.githubusercontent.com/84333525/138990051-d8c50dc5-013e-4d12-897e-a84105630b80.png)

* Creamos la clase (modelo) Tag
  - Vamos a crear una relación one to one porque queremos vincular un tag con un único usuario

![image](https://user-images.githubusercontent.com/84333525/138990437-97dded6c-1fe3-4c6a-9d84-6a84a01fbc32.png)

* Registramos el modelo en el panel de admin:

![image](https://user-images.githubusercontent.com/84333525/138990589-5f0ac0e4-dea5-4654-a181-130b79f5cd9e.png)

* Creamos y corremos migración como cada vez que hacemos cambios en los modelos.

## CREACION DEL API QUE LISTA LOS TAGS
* Recordar que como estamos desarrollando basado en pruebas, primero tenemos que crear las pruebas antes de crear las funcionalidades
* Creamos el archivo *test_tags_api.py* dónde escribiremos los tests.
* Realizamos todas las importaciones con las que estaremos trabajando

![image](https://user-images.githubusercontent.com/84333525/138993375-755786a1-35cb-4f81-a2fa-9c1f917ac0dc.png)

* Estaremos usando un viewset para trabajar la lista
* Creamos las pruebas necesarias:

![image](https://user-images.githubusercontent.com/84333525/139000338-816fa417-c0b1-4f4e-b1af-047dcac59098.png)

NOTA IMPORTANTE: PROFUNDIZAR EN LOS TEST

* Al correr las pruebas definidas salta un error, debido a que no hemos definido el serializer para los tags.

## CREACION DEL SERIALIZER
* Creamos el archivo *serializers.py* en la app.
* Realizamos las importaciones pertinentes

![image](https://user-images.githubusercontent.com/84333525/139000614-190c9085-b374-4261-a8a7-7ece032323e1.png)

* Realizamos el serializador

![image](https://user-images.githubusercontent.com/84333525/139000855-0fa7110c-8eed-497f-add0-3fea1f2e8447.png)

## CREACION DE LA VIEW
* Hacemos las importaciones necesarias

![image](https://user-images.githubusercontent.com/84333525/139001596-b2d96dd3-5939-41ff-869c-f473d7d6cd6b.png)

* Creamos el ViewSet:

![image](https://user-images.githubusercontent.com/84333525/139001839-593d2ed1-a443-4f05-ace7-be1c123db456.png)

## ADICIONAR URL
* Recordar que tenemos que crear manualmente el archivo *urls.py* de nuestra app
* Importamos lo que vamos a necesitar
* Registramos el viewset
* Agregamos la ruta

![image](https://user-images.githubusercontent.com/84333525/139002248-09e4ae1d-2b7c-4e1d-8e2e-857bd49594a3.png)

## ADICIONAR URL EN EL ARCHIVO PRINCIPAL

![image](https://user-images.githubusercontent.com/84333525/139002345-fc5f080e-57f0-45ee-ac59-1dc674bcfc88.png)

## MODIFICAMOS EL VIEWSET

![image](https://user-images.githubusercontent.com/84333525/139002548-f24b8e97-7f95-480f-aeaa-e99c24560e9d.png)

Este método *def get_queryset(self):* nos va a permitir solo retornar los tags del usuario que los está reqieriendo.

