from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import Flask


db = SQLAlchemy()
def create_app(app):
    app.config['SECRET_KEY'] = 'piss'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)
    import models
    User = models.User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    import auth
    import main
    import social
    auth_blueprint = auth.auth
    main_blueprint = main.main
    user_blueprint = social.social
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(user_blueprint)
    return app
