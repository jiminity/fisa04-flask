# flask run --debug --port 5001
from flask import Flask

# 입구 파일을 하나 만들어줍니다.
# Flask 어플리케이션을 생성하는 코드
# 이 파일에 다른 파일 경유 없이 main.py를 통해 실행된다면 __name__ 변수에는 'main'라는 문자열이 담김
app = Flask(__name__)

# app의 주소에 매핑해주세요
@app.route('/hello2')
def hello():
    return f'{__name__}  hello'

@app.route('/hello3')
def hello2():
    return f'두번째'

if __name__ == '__main__' :
    app.run(debug=True, port=5001)