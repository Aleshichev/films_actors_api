from flask import Flask, render_template, request
from flask_restful import Api
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint
import config
from src.resources.aggregation import AggregationApi

migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Config)
    from src.database.models import db
    db.init_app(app)
    migrate.init_app(app, db)

    api = Api(app)

    from src.resources.films import FilmListApi
    from src.resources.smoke import Smoke
    from src.resources.actors import ActorListApi
    from src.resources.auth import AuthRegister, AuthLogin
    api.add_resource(Smoke, '/smoke', strict_slashes=False)
    api.add_resource(FilmListApi, '/films', '/films/<uuid>', strict_slashes=False)
    api.add_resource(ActorListApi, '/actors', '/actors/<id>', strict_slashes=False)
    api.add_resource(AggregationApi, '/aggregations', strict_slashes=False)
    api.add_resource(AuthRegister, '/register', strict_slashes=False)
    api.add_resource(AuthLogin, '/login', strict_slashes=False)

    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': 'Flask tutorial'
        }
    )
    app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        return render_template('index.html')

    @app.route('/greeting', methods=['POST'])
    def greeting():
        name = request.form.get('name')
        if not name:
            return 'Please, enter a value', 400
        return render_template('greeting.html', name=name)

    return app
