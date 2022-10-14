from flask import Flask, request, jsonify
from flask_cors import CORS
import jiebaQa



app = Flask(__name__)
CORS(app) 

@app.route('/',methods=['POST'])
def postInput():
    #取得前端傳過來的值
    insertValues = request.get_json()
    input=insertValues['Qa_Typena']
    result=jiebaQa.HMM(input)

    print(f'HMM output:{result}')
    return jsonify({'return':result})

@app.route('/posseg',methods=['POST'])
def postInputseg():
    #取得前端傳過來的值
    insertValues = request.get_json()
    input=insertValues['Qa_Typena']
    result=jiebaQa.posseg(input)

    print(f'posseg output:{result[0],result[1]}')
    return jsonify({'words':result[0],'fseq':result[1]})

@app.route('/test')
def posttest():
    #取得前端傳過來的值
    insertValues = request.get_json()
    input=insertValues['Qa_Typena']
    result=jiebaQa.HMM(input)

    print(f'HMM output:{result}')
    return jsonify({'return': 'ok'})

if __name__ == '__main__':
    app.run(host='192.168.80.113',port=80,debug=True)