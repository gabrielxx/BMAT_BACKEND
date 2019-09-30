# demo-BMAT
servicio realizado usando Falcon python framework, 

## Instalar requisitos
`pip install -r requirements.txt`

## Ejecutar servidor de desarrollo de falcon mediante gunicorn
`gunicorn api:api -b :8080`

## Endpoint para consumir el microServicio (cargar los datos mediante archivo input)
`http://127.0.0.1:8080/fileUpload ó http://localhost:8080/fileUpload`
`se debera enviar en el body de la petición http el archivo del input, usando como nombre "files"`

