from flask import Flask
from config import Config
from extensions import db, ma

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    from routes.daily_entry import daily_entry_bp
    app.register_blueprint(daily_entry_bp, url_prefix='/entries')

    with app.app_context():
        db.create_all()
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
