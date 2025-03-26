from flask import Blueprint

# 특정 /url/ 하위에 있는 함수들을 일괄적으로 관리하기 위한 속성 
# Blueprint(코드에서 부르는 상대적이름, 실제파일명, url에 매칭되는 경로)
mbp = Blueprint('main', __name__, url_prefix='/main')

# localhost:5001/main/
@mbp.route('/')
def hello():
    return f'{__name__} hello'

# Flask에서 값을 주소줄로 입력받아서 사용하는 방법
# <변수명> /변수명
@mbp.route('/<username>')
def print_string(username):
    return f'{__name__} {username} hello'

# <자료형:변수명>
# <path:변수명>: /를 포함한 서브경로 전달
# <float: 변수명>: float 전달
# <int: 변수명>: int 전달
@mbp.route('/path/<path:subpath>')
def print_path(subpath):
    return f'{__name__} {subpath} hello'

# 아무런 값을 저장하지 않았을 때 디폴트값인 기본값이 출력된다
# http://localhost:5001/main/상품명/사과 -> 에러
# http://localhost:5001/main/items/사과 -> 가능
@mbp.route('/상품명/')
@mbp.route('/items/')
@mbp.route('/items/<itemname>')
@mbp.route('/items/<itemname>/<float:quantity>')
def print_itemname(itemname='기본값', quantity=0):
    print(type(quantity))
    return f'{__name__} {itemname, quantity} hello'