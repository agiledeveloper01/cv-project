from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
app.debug = True
swagger = Swagger(app)

@app.route('/v1/img_for_word', methods=['GET'])
def test_api():
  """
    Get img for word
    ---
    tags:
      - Node APIs
    produces: application/json,
    parameters:
    - name: word
      in: query
      type: string
      required: true
    responses:
      200:
        description: Retrieve image for word
        examples:
          ans: {"main_color":"red", "main_shape":["00100", "01010", "10001", "00100", "01010"]}
  """
  return jsonify(ans={"main_color":"red", "main_shape":["00100", "01010", "10001", "01010", "00100"]})

if __name__  == '__main__':
    app.debug = True
    app.run(host="0.0.0.0",port=5777)