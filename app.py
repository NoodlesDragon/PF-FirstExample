from flasgger import Swagger, LazyString, LazyJSONEncoder
from flask import Flask, jsonify, request, url_for
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

app.json_encoder = LazyJSONEncoder
app.config['SWAGGER'] = {
    'title': 'TestAPI',
}

swagger = Swagger(app, template_file='swagger.json')

class NewProduct(Resource):
    def post(self):
        return '', 501

api.add_resource(NewProduct, '/product')

if __name__ == "__main__":
    app.run()