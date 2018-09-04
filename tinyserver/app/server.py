from flask import Flask, jsonify, make_response
from flask_restplus import Api, Resource, fields
from flask_cors import CORS
import subprocess
import uuid


app = Flask(__name__)
api = Api(app, version='0.0.1', title='Tiny Server API', description='Execute Tiny Python Script')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

ns = api.namespace('api')

python_shell_parameter = api.model('SuggestionParam', {
    'key_word': fields.String(readOnly=True)
})


@ns.route('/python-shell')
class ArticleEstimations(Resource):
    @ns.expect(python_shell_parameter)
    def post(self):
        script = api.payload['content']

        tmp_file_name = str(uuid.uuid1())
        tmp_file_path = '/tmp/{}.py'.format(tmp_file_name)
        with open(tmp_file_path.format(), 'w') as f:
            f.write(script)
            f.close()

        command = 'python {}'.format(tmp_file_path)
        responses = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        result = {'output': responses.decode()}
        return make_response(jsonify(result))
