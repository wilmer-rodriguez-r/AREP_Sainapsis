# AREP_Sainapsis
En este taller intengramos un pequeño aplicativo que consulta en unos documentos que cargamos previamente en vectores en pinecone. La idea de este taller es aprender más sobre los modelos de lenguaje y como hacer uso de la API de OpenAI.

## Iniciando
Antes de ejecutar el proyecto es necesario poseer las siguiente herramientas.
### Prerrequisitos

* Git 
* Python

### Instalando el proyecto

Lo primero será traer del repositorio remoto el proyecto a la máquina local, para esto ejecutamos el siguiente comando por medio de consola.

```
git clone https://github.com/wilmer-rodriguez-r/AREP_Taller07.git
```

Esto creará un directorio nuevo, al acceder debemos entrar al ambiente virtual del proyecto ya que este trae todas las librerias necesarias para su ejecución.

```
.\venv\Scripts\activate
```
En caso de que el ambiente de ejecución falle, las librerias que se deben instalar para el funcionamiento del proyecto son las siguientes.

* langchain 
* openai==0.27.8
* tiktoken
* requests
* pydantic
* pinecone-client
* flask
* flask-sqlalchemy
* flask-restful
* flask-marshmallow

Despues de haber configurado en ambiente de ejecución, podremos iniciar la aplicación web.

```
python .\app\app.py
```

### Corriendo Localmente

Despues de ejecutar los anteriores comandos, podremos acceder al siguiente enlace https://localhost:5000, el cual nos mostrara lo siguiente.

![image](https://github.com/wilmer-rodriguez-r/AREP_Sainapsis/assets/77862048/a1102a2e-dde8-43d0-9c7c-60a99243d3b7)

Si realizamos una consulta podemos ver que nos da la siguiente información, relacionada a las carreras acreditadas de la Escuela.

![image](https://github.com/wilmer-rodriguez-r/AREP_Sainapsis/assets/77862048/47741955-4ea7-468e-89be-bacf1b52219a)

Y nos dara la siguiente respuesta.

![image](https://github.com/wilmer-rodriguez-r/AREP_Sainapsis/assets/77862048/9fd8acb9-2477-4504-bcf2-1b902d23b1a3)


## Version

1.0-SNAPSHOT

## Autores

Wilmer Arley Rodríguez Ropero - [wilmer-rodriguez-r](https://github.com/wilmer-rodriguez-r)

## Licencia

GNU General Public License family

## Agradecimientos

* Luis Daniel Benavides Navarro

## Referencias

[1] 	B. N. L. Daniel, "Introducción a esquemas de nombres, redes, clientes y servicios con Java," p. 18, 20 Agos
