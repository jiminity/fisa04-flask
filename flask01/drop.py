# drop.py
# flask db upgrade 오류나면 이 파일 실행하기

from app import create_app, db
from sqlalchemy import text  # ← 이거 추가!

app = create_app()

with app.app_context():
    db.session.execute(text("DROP TABLE IF EXISTS _alembic_tmp_answer"))
    db.session.commit()
    print("✅ 임시 테이블 삭제 완료!")