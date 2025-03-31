from flask import Flask, render_template, request
import os
from ml_model import load_model, predict
import config
from forms import InsuranceForm  # forms.py에서 폼 클래스 가져오기

app = Flask(__name__)
app.config.from_object(config)

# 실습1. '/'에 접속하면 바로 form.html에 접속하도록 경로 설정
@app.route('/', methods=['GET', 'POST'])
def home():
    form = InsuranceForm()  # forms.py에 정의된 폼 객체 생성

    # 실습2. forms.py에 작성된 form을 활용하여 데이터를 한번에 입력받을 수 있도록 활용
    if form.validate_on_submit():  # 폼이 제출되고 유효성 검사를 통과한 경우
        age = form.age.data
        bmi = form.bmi.data
        children = form.children.data
        smoker = 1 if form.smoker.data == "예" else 0
        sex = 1 if form.sex.data == "남성" else 0
        region = form.region.data

        # 지역을 원-핫 인코딩
        region_nw = 1 if region == "북서" else 0
        region_ne = 1 if region == "북동" else 0
        region_sw = 1 if region == "남서" else 0

        # 모델 로드 및 예측
        model = load_model()
        input_values = [[age, bmi, children, smoker, sex, region_nw, region_ne, region_sw]]
        prediction = predict(input_values, model)
        print(prediction)

        # 결과 페이지 렌더링
        return render_template('result.html', prediction=prediction[0])

    # 폼 페이지 렌더링
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=5000)


# 우리가 개발 중인 flask01 서비스에 ml_model이라는 서브기능을 만들어서
# ml_model과 관련된 model, form, template, view를 정리해서 합쳐주세요.
# 로그인을 한 사람한테만 navbar에 ML MODEL이라는 항목이 보이도록 변경해서 
# 로그인을 한 사람만 ML MODEL의 입력창 / 결과창에 접근할 수 있도록 변경해 주십시오.
# DB에 모델에 사용자가 입력한 결과와 그 추론결과가 저장되도록 insurance라는 테이블을 만들어서 user에 대한 정보 + 넣은 값 + 추론결과가 하나의 테이블에 저장되도록 만들어주십시오.