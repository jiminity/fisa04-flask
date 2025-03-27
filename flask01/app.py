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

    # ORM을 적용
    db.init_app(app)
    migrate.init_app(app, db)

    from board.views import main_views, board_views
    app.register_blueprint(main_views.mbp)
    app.register_blueprint(board_views.cbp)

    return app