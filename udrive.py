from app import create_app
from app.models import db
import sqlalchemy as sa
import sqlalchemy.orm as so
from app.models import Users, Docs
app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'Users': Users, "Docs": Docs}