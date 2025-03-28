# flask run --debug --port 5001
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()
def create_app():
    
    # 입구 파일을 하나 만들어줍니다.
    # Flask 어플리케이션을 생성하는 코드
    # 이 파일에 다른 파일 경유 없이 main.py를 통해 실행된다면 __name__ 변수에는 'main'라는 문자열이 담김
    app = Flask(__name__)
    app.config.from_object(config)
    app.config['SQLALCHEMY_ECHO'] = True  # 디버깅용 설정

    # ORM을 적용
    db.init_app(app)
    migrate.init_app(app, db)
    

    # 커스텀 진자 필터 등록
    from filters import format_datetime, format_datetime2
    app.jinja_env.filters['date_time'] = format_datetime
    app.jinja_env.filters['date_time2'] = format_datetime2
    
    from board.views import main_views, board_views, answer_views
    app.register_blueprint(main_views.mbp)
    app.register_blueprint(board_views.cbp)
    app.register_blueprint(answer_views.abp)
    return app