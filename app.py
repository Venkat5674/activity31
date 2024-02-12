from flask import Flask,request  #get () is used
from model import predict_model
app=Flask(__name__)

@app.route('/')
def basic():
    return 'API Server is Started'

@app.route('/soil', methods=['get'])
def soil():
    value=request.args.get('soil')
    print(value)
    value=int(value)
    response=predict_model(value)
    print(response)
    return ({'msg':str(response)})

if __name__ == '__main__':
    app.run('0.0.0.0',port=5001,debug=True)
