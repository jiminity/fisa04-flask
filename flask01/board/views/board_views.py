from flask import Blueprint, render_template, redirect, url_for, request
from ..models import Question
from ..forms import QuestionForm, AnswerForm
from app import db
from datetime import datetime

# Blueprint(코드에서 부르는 상대적이름, 실제파일명, url에 매칭되는 경로)
cbp = Blueprint('board', __name__, url_prefix="/board")


# templates 디렉토리 안에 들어있는
# 전체 게시글을 db에서 조회해서 가져오는 함수
# @cbp.route('/list')
# def list():
#     question = Question.query.all()
#     return render_template('board/boardList.html', question_list=question)

@cbp.route('/list')
def list():
    page = request.args.get('page', type=int, default=1)  # 페이지
    question_list = Question.query.order_by(Question.create_date.desc())
    question_list = question_list.paginate(page=page, per_page=10)
    return render_template('board/boardList.html', question_list=question_list)


# 개별 게시글을 조회할 수 있는 함수
@cbp.route('/details/<int:question_id>/')
def detail(question_id):
    # get_or_404() 메서드로 값을 조회하면 404에러를 발생시킵니다.
    # question = Question.query.get(question_id)
    question = Question.query.get_or_404(question_id)
    form = AnswerForm()
    return render_template('board/boardDetail.html', question=question, form=form, question_id=question_id)


# 개별 게시글을 작성
# 1. 작성 버튼을 누르면 게시글을 작성하기 위한 form으로 이동
# 2. 폼에서 완료 버튼을 누르면 DB에 글을 저장하고, 저장된 글을 확인하게 하기 위해 전체 List로 이동
@cbp.route('/create/', methods=('GET', 'POST'))
# @login_required # 실습 - answer_views에도 적용
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('board.list'))
    return render_template('board/questionForm.html', form=form)


# 개별 게시글을 삭제


# 개별 게시글을 수정


# Blueprint 기능을 사용해서 collection/no1/
@cbp.route('/no1')
def hello2():
    return f'{__name__} 첫번째'

# Blueprint 기능을 사용해서 collection/no2/   
@cbp.route('/no2')
def hello3():
    return f'{__name__} 두번째'
    