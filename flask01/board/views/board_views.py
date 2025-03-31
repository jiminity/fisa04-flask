from flask import Blueprint, render_template, redirect, url_for, request, g, flash
from ..models import Question, Answer
from ..forms import QuestionForm, AnswerForm
from app import db
from datetime import datetime
from board.views.auth_views import login_required

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
@login_required # 실습 - answer_views에도 적용
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now(),user_id=g.user.id)
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('board.list'))
    return render_template('board/questionForm.html', form=form)



# 개별 게시글을 수정
# 로그인 여부 확인
@cbp.route('/modify/<int:answer_id>', methods=('GET', 'POST'))
@login_required
def modify(answer_id):
    # db에서 글을 가져온다
    answer = Answer.query.get_or_404(answer_id)
    # 댓글이 포함된 글번호도 가져옵니다.
    question_id=answer.question_id
    # 현재 작성자와 로그인한 사람이 같은 사람이지 확인
    if answer.user != g.user:
        # 아니면 '권한이 없습니다' 에러 flash
        flash('수정 권한이 없습니다.')
        # 글의 본문으로 돌려보냅니다.
        return redirect(url_for('board.detail', question_id=question_id))

    # 글의 작성자와 로그인한 사람이 같으면(권한 O), POST인지 확인하고
    if request.method == 'POST':
       # QuestionForm에 값을 미리 가져온 다음에 
        form = AnswerForm()
        if form.validate_on_submit():
        # 변경한 값을 db에 다시 반영
            form.populate_obj(answer) # 화면에 원래 db에서 가져온 값을 form에 넣어서 보여줍니다.
            db.session.commit()
            # 수정된 글의 본문으로 돌려보냅니다.
            return redirect(url_for('board.detail', question_id=question_id))
    else: # GET으로 왔을 때
        # 수정화면으로 form과 돌려보냅니다.
        form = AnswerForm(obj=answer) 
    return render_template('board/questionForm.html', form=form, answer_id=answer_id, modify=True)



# 개별 게시글을 삭제
@cbp.route("/delete/<int:question_id>")
@login_required
def delete(answer_id):
    # 글을 가져옴
    answer = Answer.query.get_or_404(answer_id)
    question_id=answer.question_id
    # 현재 접속한 사용자와 글의 작성자가 일치하는지 확인
    if g.user != answer.user: 
        flash('삭제권한이 없습니다')
    #     일치하지 않으면 -> 삭제권한이 없습니다 메시지 출력
        return redirect(url_for('board.detail', question_id=question_id))
    #     원래 글로 되돌아감
    db.session.delete(answer)
    db.session.commit()
    # 댓글이 삭제된 게시글 상세 페이지로 되돌아가
    return redirect(url_for('board.list', question_id=question_id, modify=True))




# Blueprint 기능을 사용해서 collection/no1/
@cbp.route('/no1')
def hello2():
    return f'{__name__} 첫번째'

# Blueprint 기능을 사용해서 collection/no2/   
@cbp.route('/no2')
def hello3():
    return f'{__name__} 두번째'
    