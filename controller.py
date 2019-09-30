import io
import os
import mimetypes
import falcon
import json
from Ancestor import AncestorClass

class AncestorApi():

        def on_post(self, req, resp,  **kwargs):
            
            filer = req.get_param("files")
            content = filer.file.read().decode('utf-8').split('\n')
            ancestor = AncestorClass()
            ancestor.setItemQuestion(content[0])
            if ancestor.setItemQuestion(content[0]) is False:
            	raise falcon.HTTPBadRequest(
                    "Error datos archivo input",
                    "Formato de datos invalidos, verifique."
                )

            ancestor.setRoot(content[1])
            cont = 0
            for i in range(2, len(content)):
                if(cont < ancestor.items - 1):
                    ancestor.setItems(content[i])
                elif(cont < (ancestor.items +  ancestor.items + ancestor.question - 1) and content[i] != ''):
                    ancestor.setQuestions(content[i])
                cont +=1
            # implementar response file text con data
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(ancestor.questions)

