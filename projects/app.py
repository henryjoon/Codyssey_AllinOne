from flask import Flask #flask 라이브러리에서 Flask 클래스 가져옴. => Flask앱(=서버)을 만드는 역할

app = Flask(__name__) #만들어진 앱을 app이라는 변수에 저장

@app.route("/") #데코레이터임. 루트경로로 접속했을 때 바로 아래 함수를 실행하게 함.
def hello_world():
    return "Hello, DevOps!"

if __name__ == "__main__": # 직접 실행했을 때, 서버를 작동시켜라
    app.run(host="0.0.0.0", port=80) #0.0.0.0: 모든 ip 주소에서 접속 가능, 127.0.0.1은 자신만 가능, 
                                     #80번 포트: HTTP 프로토콜의 기본 포트. 
                                     #같은 네트워크에 있으면 http://<my_ip_address>:port_num 해서 접속 가능

# Run without Debugging: 코드 중단 없이 빠르게 결과 확인. 이 app.py와 같은 환경에서는 이 실행 추천
# Start Debugging: 중단점에서 해당 코드가 멈추는 등 디버깅 모드로 실행하기 때문에 변수값 추적이나 문제 있는 코드 찾고 수정할 때 유용함.