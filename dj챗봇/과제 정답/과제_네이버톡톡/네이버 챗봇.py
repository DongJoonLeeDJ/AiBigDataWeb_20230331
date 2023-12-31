import requests, json
import urllib.request #json api 가져오기
from flask import Flask,request,jsonify,abort
import sys
application = Flask(__name__)



# 개발자도구->챗봇api설정->webhook
@application.route("/mytalk", methods=['POST'])
def mytalk():
    
    # 개발자도구->챗봇api설정->webhook
    authorization_key = '5YlPTtw4SrqjmQXLieja'
    
    headers = {
        'Content-Type' : 'application/json;charset=UTF-8',
        'Authorization' : authorization_key
    }
    print(request.get_json())
    getReqJson = request.get_json()
    user_key = getReqJson['user']
    
    userMsg = getReqJson['textContent']['text']
    lottodata=''
    data = {
        'event':"send",
        'user':user_key,
        'textContent':{
            "text":lottodata
        }
    }
    if userMsg.split()[0]=='로또':
        isImg = False
        url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=%s'% userMsg.split()[1]
        response = urllib.request.urlopen(url)
        response_message = response.read().decode('utf8')
        jresponse = json.loads(response_message)
        print(jresponse)
        print(response_message)
        print(jresponse['returnValue'])
        
        if jresponse['returnValue'] != 'success':
            lottodata = '잘못된 입력입니다.'
            print(lottodata)
        else:
            lottodata = "{} {} {} {} {} {} 보너스 : {}".format(jresponse['drwtNo1'],jresponse['drwtNo2'],jresponse['drwtNo3'],jresponse['drwtNo4'],jresponse['drwtNo5'],jresponse['drwtNo6'],jresponse['bnusNo'])   
            print(lottodata)
        data = {
                'event':"send",
                'user':user_key,
                'textContent':{
                    "text":lottodata
                }
            }
    message = json.dumps(data)
    response = requests.post('https://gw.talk.naver.com/chatbot/v1/event',
                            headers=headers,
                            data=message)


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000)
