from flask import Blueprint

# Blueprint(코드에서 부르는 상대적이름, 실제파일명, url에 매칭되는 경로)
cbp = Blueprint('collection', __name__, url_prefix="/board")

# Blueprint 기능을 사용해서 collection/no1/
@cbp.route('/no1')
def hello2():
    return f'{__name__} 첫번째'

# Blueprint 기능을 사용해서 collection/no2/   
@cbp.route('/no2')
def hello3():
    return f'{__name__} 두번째'
    