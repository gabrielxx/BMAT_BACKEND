# demo-BMAT
servicio realizado usando Falcon python framework, 

## Instalar requisitos
`pip install -r requirements.txt`

## Ejecutar servidor (gunicorn) para desplegar el servicio rest.
`gunicorn api:api`

## Endpoint para consumir el microServicio (cargar los datos mediante archivo input)
Para consumir o hacer uso del microServicio debera realizar una peticion POST a la url:
`http://127.0.0.1:8000/fileUpload` ó `http://localhost:8000/fileUpload`
donde se debera enviar en el body de la petición http el archivo del input, usando como nombre del parametro `files`, 
`NOTA: este dara como respuesta (response) un array, con el resultado de cada pregunta de ancestro, que se encuentre en el archivo input.`

