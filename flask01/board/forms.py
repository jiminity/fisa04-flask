from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email
from wtforms import IntegerField, FloatField, BooleanField, RadioField, SelectField, SubmitField
from wtforms.validators import InputRequired, NumberRange


class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('10글자 넘지 마세요.'), Length(max=10)])
    content = TextAreaField('내용', validators=[DataRequired('내용을 꼭 입력하셔야 합니다.')])

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired()])

class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])

class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired(), Length(min=3, max=25)])   


class InsuranceForm(FlaskForm):
    age = IntegerField('나이', validators=[InputRequired(), NumberRange(min=0, max=99)], default=25)
    bmi = FloatField('BMI', validators=[InputRequired(), NumberRange(min=0.0, max=100.0)], default=25)
    children = IntegerField('자녀 수', validators=[InputRequired(), NumberRange(min=0, max=99)], default=0)
    smoker = BooleanField('흡연 여부')
    sex = RadioField('성별', choices=[('남성', '남성'), ('여성', '여성')], validators=[InputRequired()])
    region = SelectField('지역', choices=[('북동', '북동'), ('북서', '북서'), ('남동', '남동'), ('남서', '남서')], validators=[InputRequired()])
    submit = SubmitField('예측')