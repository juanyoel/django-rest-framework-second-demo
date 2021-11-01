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

![image](https://user-images.githubusercontent.com/84333525/139258903-d62b9d7d-ece0-4443-bab7-ebec734d261d.png)

## ADICIONAR TAGS
* Recordemos que estamos trabajando basado en pruebas, por lo que antes de adicionar nuevos Tags debemos crear las pruebas necesarias, para esto nos volvemos a ubicar en el archivo *test_tags_api.py*
* Adicionamos las pruebas correspondientes a la creación de los Tags (cuando es correcto y cuando no es correcto).

![image](https://user-images.githubusercontent.com/84333525/139261664-8c8ad95a-534d-4c5b-9366-f0faa07d15b5.png)

* Creamos ahora el soporte para crear realmente nuestros Tags
  - Para ello vamos a crear primero la vista *(views.py)*
  - Primero heredamos de una nueva clase y se lo pasamos como parámetro a nuestro viewset, esto nos permitirá "crear", como vemos en la siguiente imagen:
  
    ![image](https://user-images.githubusercontent.com/84333525/139262305-aa3da2c8-6ffb-4ed7-a05a-52cf2fc63317.png)

  - Luego definimos la función que nos permitirá crear un nuevo tag

    ![image](https://user-images.githubusercontent.com/84333525/139263070-f596dfed-3c0a-4825-a1ed-c26e63ed0fa0.png)

## CREACION DE API PARA LOS INGREDIENTES

### CREACION DEL TEST DEL MODELO
* El primer paso como hemos hecho antes es crear el modelo de los *ingredientes* para ello lo primero es crear el test del modelo, recordemos que por definición definimos los modelos en al app *core* entonces para definir los test nos ubicamos en el archivo *test_models.py* y escribimos nuestro código:

![image](https://user-images.githubusercontent.com/84333525/139264929-c06378c6-2982-4400-a6b9-0b4a068dbba4.png)

* Al correr el test, obtendremos un error como el siguiente, estos errores no los he puesto antes pero son comunes al momento de crear todos los test, y es debido a que en ese momento aún no se han definido los modelos que se están testeando.

![image](https://user-images.githubusercontent.com/84333525/139265521-0e86f07c-7554-4755-b0ec-555ba3c62b8f.png)

### CREACION DEL MODELO
* Como ya he mencionado tenemos todos los modelos en el archivo *models.py* de la app *core*. Nos ubicamos en el para escribir el código correspondiente.
  
  ![image](https://user-images.githubusercontent.com/84333525/139266376-64d2ff69-acae-47e1-b72e-752429d630a1.png)

### ACCESO AL PANEL DE ADMINISTRACION
* Como ya hemos hecho antes el próximo paso es poder incluir nuestro modelo en el panel de administración para poder tener un control más sencillo de las acciones que se pueden realizar sobre el mismo
* Para ello nos dirijimos al archivo *admin.py* de la app *core* e incluimos el siguiente código:

![image](https://user-images.githubusercontent.com/84333525/139266847-e9044fec-9098-4487-bda6-ea907594f250.png)

### MIGRACIONES BD
* Como es sabido luego de crear o modificar los modelos, debemos actualizar nuestra BD, para ello creamos y corremos las migraciones como hemos hecho antes.
  - *python manage.py makemigrations*
  - *python manage.py migreate*

### LISTAR INGREDIENTES
* Para listar los ingredientes primero realizamos los test correspondientes
* Creamos el archivo *test_ingredientes_api.py*
  - Realizamos las importaciones necesarias

![image](https://user-images.githubusercontent.com/84333525/139268712-37bcd2d0-5a02-4845-adc3-50d1de8ac676.png)

- Definimos las urls para los ingredientes: *INGREDIENTS_URL = reverse('recipe:ingredient-list')*
- Creamos el API con los métodos de accesos que son públicos y el API con los métodos de acceso privados.

![image](https://user-images.githubusercontent.com/84333525/139286099-b8db3358-aba4-4656-b2df-0b5ff1c4c292.png)

### CREAR EL SERIALIZADOR
* Para ello como ya sabemos, nos ubicamos en el archivo *serializers.py*
* Importamos el modelo Ingrediente y creamos el serializador

![image](https://user-images.githubusercontent.com/84333525/139286938-d0c7d88f-c3f0-47f9-872c-44305a986ae4.png)

### CREAR LA VISTA
* El próximo paso lógico luego de creado el serializdor es crear la vista, para ello nos ubicamos en nuestro archivo *views.py*
* Importamos el modelo Ingrediente
* Creamos el viewset, tener en cuenta lo siguiente:
  - Cada vez que creamos una vista necesitaremos definirle algunos parámetros que no podemos olvidar:
    * authentication_classes --> defino la vía que se está usando en el proyecto para manejar la autenticación
    * permission_classes --> como se manejan los permisos para acceder a los diferentes endpoints
    * queryset --> generalmente cuando debemos listar los objetos siempre debemos ponerlo
    * serializer_class --> es de lo más importante ya que es lo que nos permite interpretar la data que viene en request y transformarla a un objeto de la BD

![image](https://user-images.githubusercontent.com/84333525/139289235-99cd4a19-c1f3-4147-9a0c-973dc9351670.png)

### CREAR LA URL ASOCIADA A LA VISTA
* Para ello como ya sabemos nos posicionamos en el archivo *urls.py*
* Registramos la url en el router y listo

![image](https://user-images.githubusercontent.com/84333525/139289665-d8c628ae-1409-4387-9cb5-b86eb5bc941e.png)

### ADICIONAMOS FUNCIONALIDAD PARA CREAR NUEVOS INGREDIENTES
* Como toda nueva funcionalidad sabemos que necesitamos primero crear las pruebas necesarias por lo que nos posicionamos en el archivo *test_ingredients_api.py*
* Primero creamos la prueba para probar que la creación del inrgediente es success
  - Para este test primero definimos un ingrediente (payload)
  - Cargamos el payload a través de la url
  - Es a través de un método post para poder enviar el payload
  - Chequeamos si el ingrediente existe y si existe es lo que necesitamos porque se va haber creado
* Segundo creamos el test para probar comportamiento cuando estamos creando un ingrediente inválido
  - Para este test primero definimos un ingrediente (payload)
  - Cargamos el payload a través del url
  - Chequeamos que si el ingrediente no tiene nombre, retorne un bad request
  
  ![image](https://user-images.githubusercontent.com/84333525/139295292-d0e41b2e-1a0a-4050-b681-c45b415e549e.png)

* Tercero necesitamos crear el viewset, por lo que nos posicionamos en el archivo *views.py*
  - Primero heredamos de *mixins.CreateModelMixin*

  ![image](https://user-images.githubusercontent.com/84333525/139324195-333d79e1-ce2c-4340-aa24-e4d94fa0e338.png)

  - Segundo creamos la función para crear ek ingrediente 

  ![image](https://user-images.githubusercontent.com/84333525/139324515-35776cce-d394-4629-bdbe-6c41c7b37376.png)

### REFACTORIZACION A LO BESTIA (MUY BUENO VER CURSO 4H13M)
* No voy hacer la refactorización para no perderme con las explicaciones e imagenes anteriores, pero si que es importante ver esa refactorización muy buena.

## CREAR RECIPE (LA RECETA)
* Como estamos programando basado en pruebas lo primero es crear los test correspondientes al modelo de recipe, para ello nos ubicamos en el archivo *test_model.py*
* Creamos el test:
  - el cual tendrá una receta de pruebas conformada por
    * el usurario que creo la receta
    * El titulo de la receta
    * el tiempo de cocción
    * precio
 
  ![image](https://user-images.githubusercontent.com/84333525/139326651-7c0a7fc2-b462-4e15-9e65-17e2fd1d8cd4.png)

### CREAR MODELO
* Una vez creado el test y corrido, obtenemos el error normal, debido a que necesitamos crear el modelo correspondiete Recipe
* Para ello nos posicionamos en el archivo *models.py*
* Creamos el modelo, importante fijarse en las relaciones many to many que tienen las recetas con los tags y con los ingredientes

![image](https://user-images.githubusercontent.com/84333525/139328456-bc9aa4b9-8e09-4296-95de-6dd0a4ad0b70.png)

### AGREGAR EL MODELO AL PANEL DE ADMIN
* Luego de creado el modelo pasamos a registrarlo en el archivo *admin.py* para así tener un mayor control de las acciones que podemos realizar sobre el.

![image](https://user-images.githubusercontent.com/84333525/139332087-c38e2168-8408-45ca-97e1-511d2b9e03e5.png)

### CREAMOS Y CORREMOS LAS MIGRACIONES
* *python.exe manage.py makemigrations*
* *python.exe manage.py migrate*

### CREAR PRUEBAS PARA LISTAR LAS RECETAS
* Primero creamos las pruebas para listar las recetas, similar a todo lo que hemos hecho antes.
* Para ello vamos a nuestra carpeta de tests y agregamos el archivo *test_recipe_api.py*
* Realizamos todas las importaciones necesarias, las mimas que en caso anteriores

![image](https://user-images.githubusercontent.com/84333525/139460041-16ff2b87-7820-4a5a-acf3-0d276473efde.png)

* Definimos el url de nuestra receta:

![image](https://user-images.githubusercontent.com/84333525/139460241-a151b6d1-7f44-499c-b4c8-426fdba45cf4.png)

* Creamos una función que nos retorne una receta de prueba para usarla en nuestros test

![image](https://user-images.githubusercontent.com/84333525/139460816-cfc5e6b5-ad85-482c-8d77-0aa684fb44bc.png)

* Creamos las clases PUBICA Y PRIVADA, en la que colocaremos el código de nuestros test en correspondencia
* En la clase Publica como la Privada creamos el setUp ... esta función siempre es obligatoria, tener en cuenta que siempre obligamos al usuario a autenticarse.

![image](https://user-images.githubusercontent.com/84333525/139462989-8ce3bf70-a79c-4cd0-b5af-3ee39f5bc42e.png)

* Como podemos ver en la función setUp creamos el usuario de prueba para los test, esto siempre se debe hacer y en el test primero creamos dos recetas de prueba, hacemos la llamada al api mediante el get, luego hago una llamada para obtener todas las recipes las serializo y compruebo que la llamada haya retornado un status 200.
* Creamos el test para listar las recetas por usuario, al correr el mismo obvio obtenemos el error de que no tenemos el serializer definido que es lo que haremos en el próximo paso.

![image](https://user-images.githubusercontent.com/84333525/139464819-590cdfdd-97e3-4398-8ac0-40da6734171c.png)

### CREAMOS EL SERIALIZADOR
* Este ejemplo es de gran importancia para el estudio ya que debemos recordar que tenemos una relación many to many, por lo que debemos serializar los campos many to many haciendo un *queryset* a todos los ingredientes y todos los tags, primero vamos hacerlo a los ingredientes y luego lo mismo a los tags:
 
 ![image](https://user-images.githubusercontent.com/84333525/139466291-9d44f493-a367-4e56-823c-5f814399c84d.png)

### CREAR LAS VISTAS
* Luego de creado el serializer pasamos a crear las vistas, viewsets. Para ello nos ubicamos en el archivo *views.py*
* Importamos la clase Recipe

![image](https://user-images.githubusercontent.com/84333525/139466644-eba8f7e4-f42f-48bd-9cb5-13c65223b625.png)

![image](https://user-images.githubusercontent.com/84333525/139467627-4f0ed400-6e76-4b2b-8e39-731bad843a93.png)

### CREAR URL
* El próximo paso es vincular la vista con el url para poder tener acceso a la misma, para ello nos ubicamos en ele archivo *urls.py*
* Agregamos la url al router y listo

![image](https://user-images.githubusercontent.com/84333525/139467913-40df6af5-8bfd-4fd3-a687-07f989e5b53b.png)


## FUNCIONALIDAD PARA OBTENER DETALLES DE LA RECETA

### CREAR TEST 
* Como ya sabemos primero debemos programar los test de la nueva funcionalidad por lo que para ello nos ubicamos en el archivo *test_recipe_api.py*
* Como recordamos la receta tiene ingredientes y tags, por lo que el primer paso es importar los modelos desde *core* y además importar un nuevo serializer que aún no he creado
  *RecipeSerializer*
* Luego creamos un ingrediente y un tag de ejemplo.

![image](https://user-images.githubusercontent.com/84333525/139471048-88bc4e73-9703-4f3b-a1c2-8ba6026b1316.png)

* El próximo paso es crear una función que te retorne la url de detalles:

![image](https://user-images.githubusercontent.com/84333525/139471191-5a5c0f80-e8d0-4dc5-b65f-0c4c5b547df1.png)

* Creamos el test:

![image](https://user-images.githubusercontent.com/84333525/139472491-dfb08e53-8514-4964-a9b6-3cbd72b32a4d.png)

### CREAR SERIALIZER
* Como ya sabemos al correr las pruebas obtenemos un error debido a que no hemos implementado el serializador necesario para la función, para ello nos ubicamos en el archivo *serializers.py*

![image](https://user-images.githubusercontent.com/84333525/139486798-07a21bb0-7183-4436-a1bc-e5ccddffef16.png)

Como heredamos de RecipeSerializer solo debemos serializar los objetos con los que tenemos relaciones Ingredientes y Tags

### CREAR VISTA
* Importante , tenemos que tener en cuenta que ahora para las recetas tenemos dos serializadores por lo que debemos hacer ahora es definir una función que nos retorne el serializador indicado:

![image](https://user-images.githubusercontent.com/84333525/139487520-1479d8af-229d-4b80-907d-75c2e4beee10.png)

## FUNCIONALIDAD PARA CREAR UNA RECETA

### CREAR TEST
* Lo primero es crear los test para adicionar cualquier funcionalidad, en este caso vamos a *crear una receta*, para ello os ubicamos en el archivo *test_recipe_api.py*
* Creamos el test:

![image](https://user-images.githubusercontent.com/84333525/139488661-6c3f995c-923e-4157-9bd3-cb1244a45589.png)

- Creamos nuestro payload como siempre se debe hacer cuando vamos ha realizar un post.
- Hacemos la llamada al api y guardamos la respuesta en la variable res.
- Luego comprobamos que el api retorne un status 201 created.
- Obtenemos la receta creada de la BD.
- Por último obtenemos los atributos por cada clave de nuestra receta **ESTUDIAR ESTE CODIGO**

* Creamos el resto de los tests:

![image](https://user-images.githubusercontent.com/84333525/139490810-10e49d38-1913-4c07-b97d-9295c6d3022f.png)

### CREAR RECETAS -- VIEWS
* Para ello lo primero es crear la vista por lo que nos ubicamos en el archivo *views.py*
* Creamos la función *perform_create*

![image](https://user-images.githubusercontent.com/84333525/139492057-48e68245-f94e-47d8-91c3-f9a882e60c8d.png)

Con esto hecho ya podemos correr los test y deberían estar OK.

# TRABAJO CON IAGENES
## PILOW
* Para el trabajo con imágenes debemos instalar un paquete llamado Pilow: *pip install pillow*
* Nos ubicamos en el archivo *settings.py* dónde se encuentra la línea *STATIC_URL = '/static/'* y agregamos la siguiente:

   ![image](https://user-images.githubusercontent.com/84333525/139673607-6ef7ae29-5e61-45b4-90dc-4d789d1baeed.png)

* Luego necesitamos configurar el archivo *urls.py* y para ello, primero debmos hacer las importaciones necesarias:
  
  ![image](https://user-images.githubusercontent.com/84333525/139674026-4a931744-4b3a-4d03-baf2-10df9adcfb4f.png)

* Modificamos el url patterns:
  
  ![image](https://user-images.githubusercontent.com/84333525/139674379-f6b7c493-172b-46c1-aace-0a599ff184f8.png)

* Luego pasamos a implementar la funcionalidad de las imágenes, para ello modificamos el modelo del recipe.
* Como toda nueva funcionalidad primero creamos el test indicado.
  * Tener en cuenta que lo que hacemos al subir una imagen para un recipe es que se modifica el recipe por lo que el método a utilizar para ello es el PATCH.
  * Para poder usar este método en los test hacemos la siguiente importación:

    ![image](https://user-images.githubusercontent.com/84333525/139675375-ba64a805-6e83-43e1-bdf1-7ef7b6808a16.png)

* Luego creamos el test:

![image](https://user-images.githubusercontent.com/84333525/139676223-5939eec8-3854-4359-96c1-53407ab4b057.png)

### MODIFICAMOS EL MODELO
* Primero realizamos las importaciones necesarias para el trabajo con imágenes:

  ![image](https://user-images.githubusercontent.com/84333525/139677439-356a71d8-2f62-44bc-83b1-f8a468ab3790.png)
  
* Segundo creamos una función que nos retornará el path a dónde se encuentran las imágenes.

![image](https://user-images.githubusercontent.com/84333525/139678470-cb471985-b895-4c3c-904b-627da894f910.png)

* Tercero agregamos el campo a las recetas:
  
  ![image](https://user-images.githubusercontent.com/84333525/139678656-8e58de1a-3d56-4d21-afa5-4595c0e1a37b.png)

* Cuarto corremos las migraciones.

### ADICIONAR IMAGENES A LAS RECETAS
* Primero creamos el test para esta funcionalidad
* Hacemos las importaciones necesarias para el trabajo con imágenes

![image](https://user-images.githubusercontent.com/84333525/139680137-539c5686-8ab6-4321-be38-be4147cc83cd.png)

* Creamos una función de prueba que nos retorne la url

![image](https://user-images.githubusercontent.com/84333525/139680287-a992c40f-ff6b-423f-a743-5ff9b099ecaa.png)

* Creamos una clase nueva dónde definimos las pruebas relacionadas con las imágenes, le definimos su función setUp como de costumbre y demás métodos según los test que se vayan a realizar.

![image](https://user-images.githubusercontent.com/84333525/139683033-c89cf4bb-314d-4cf9-968b-554a1e17c1fd.png)

* Creamos un nuevo test para cuando no se puede subir la imágen.
  
  ![image](https://user-images.githubusercontent.com/84333525/139683741-40ac4536-3c95-4b46-b9db-42d411ba12d6.png)

### MODIFICAMOS SERIALIZER
* Debemos crear un recipe_image_serializer, porque debemos ser capaz de serializar las imágenes subidas.

![image](https://user-images.githubusercontent.com/84333525/139684554-1d140302-a48d-4578-801c-bde4741f6d04.png)

### MODIFICAMOS LA VISTA (VIEW)
* Hacemos las importanciones necesarias:

  ![image](https://user-images.githubusercontent.com/84333525/139686875-dd7b0f67-3e4a-491c-a0af-61b227723644.png)

* Creamos el método para la funcionalidad de subir imágenes:

  ![image](https://user-images.githubusercontent.com/84333525/139686983-78dfb218-a704-457e-86dd-e293a9268246.png)
  
* Modificamos la clase get_serializer:

  ![image](https://user-images.githubusercontent.com/84333525/139687080-e96eb16f-4cd2-4e26-9747-13c296bf6717.png)

## ADICIONAR LA FUNCIONALIDAD DE PODER FILTRAR LAS RECETAS POR INGREDIENTES
* Para ello comenzamos por los test como de costumbre :)
  
  ![image](https://user-images.githubusercontent.com/84333525/139693657-57994e0a-1497-4f0f-bb39-7b79b95fa8ce.png)

## MODIFICAMOS LA VISTA PARA FILTRAR
* Estudiar esto con más tiempo para tener una mejor comprensión, al momento de ver el curso no entendí nada, además que los test no me corrieron por lo que tuve que comentarlos :(

![image](https://user-images.githubusercontent.com/84333525/139714442-7ecd3209-4da4-4d1a-8897-5c6d7d92cb5c.png)

## AGREGAR FILTROS DE TAGS E INGREDIENTES
### CREAR LOS TEST
* En amobos casos importamos el modelo de Recipe a los test

![image](https://user-images.githubusercontent.com/84333525/139714732-396b9471-dbd8-4243-9178-a5600b8cbb6e.png)

* Creamos los tests para los tags:

![image](https://user-images.githubusercontent.com/84333525/139715923-443f2387-d597-4d77-9344-7b8c7d40d28e.png)


![image](https://user-images.githubusercontent.com/84333525/139717075-8b22e7a2-fbb0-448f-8d72-5ffee3e5a002.png)


## ADICIONAR FUNCIONALIDAD PARA FILTRAR POR TAGS E INGREDIENTES
### MODIFICAMOS LA VISTA 
* Se le adiciona el siguiente código al metódo get_queryset() de los viewsets

![image](https://user-images.githubusercontent.com/84333525/139719093-b2dc692b-c6cb-44b9-92f7-0d2707059604.png)


## OBSERVACION SOBRE INSTALACION DE PAQUETES:
* Cuando estamos trabajando y no es un proyecto personal, recomiendo usar el .txt requirements para poner los paquetes y la versión de los mismos, así el que vaya a a utilizar la app solo tendrá que usar el comando: *pip install -r requirements.txt* y ya se le descargarán los paquetes necesarios.


