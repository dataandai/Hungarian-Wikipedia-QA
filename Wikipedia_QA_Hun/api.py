from flask import Flask,request,jsonify
from flask_cors import CORS
import squad
import entity_recognition
import nltk
import transformers
import wiki_parser

app = Flask(__name__)
CORS(app)


@app.route("/qa",methods=['POST'])
def predict_qa():

    q = request.json["question"]
    
    docEntities = entity_recognition.recognize_entities(q)
    doc = wiki_parser.parse_entity(docEntities)
  
    try:
        return jsonify({"result": squad.get_answer(q,doc)})
    except Exception as e:
        print(e)
        return jsonify({"result":"Model Failed"})

@app.route("/",methods=['GET'])
def index():
    return "api: /qa (post)\n example: { \"question\": \"Ki volt Dobó István?\" }"

if __name__ == "__main__":
    app.run('0.0.0.0',port=8000)