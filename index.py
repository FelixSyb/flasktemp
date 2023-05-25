from flask import Flask,request
import requests
import json
import random
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return '在此输入apikey 样式:sk-s5S5BoV...'

# @app.route('/message',methods = ['POST'])
# def mess():  # put application's code here
#     global acc
#     message = request.json.get('msg')
#     openai.api_key = "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" #修改这里为自己申请的api_key
    
#     if acc==0:
#         messages = [
#             {"role": "system", "content": "You are a chating robot from windyword"},
#         ]
#     messages.append({"role": "user", "content": message})
#     acc += 1
#     if acc>=3:
#         acc = 0

#     completion = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo-0301", 
#     messages=messages
#     )

#     print(completion)
#     messages.append(completion["choices"][0]["message"])
#     #messages.append({"role": "assistant", "content": response["choices"][0]["message"].content})
#     res = {
#             "resmsg":completion,
#             "code":200
#             }

#     return res

def Completion(input_str:str): 
    output_str = ''
    for i,c in enumerate(input_str,1):
        for j in range(i):
            output_str += c
    return output_str


@app.route('/message',methods = ['POST'])
def mess():  # put application's code here

    message = request.json.get('msg')

    completion = Completion(message)

    print(completion)

    res = {
            "resmsg":completion,
            "code":200
            }

    return res

if __name__ == '__main__':
    # app.run(threaded = False,processes=1,host="0.0.0.0",port="5000",)
    app.run(threaded = False,processes=1,port="5000",)
