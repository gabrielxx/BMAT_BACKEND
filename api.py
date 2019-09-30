import falcon
from controller import AncestorApi
from falcon_multipart.middleware import MultipartMiddleware


api = application = falcon.API(middleware=[MultipartMiddleware()])
api.add_route('/fileUpload', AncestorApi())
