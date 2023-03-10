from datetime import datetime
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy.orm import selectinload
from src.database.models import db, Film
from src.resources.auth import token_required
from src.schemas.films import FilmSchema
from src.services.film_service import FilmService


class FilmListApi(Resource):
    film_schema = FilmSchema()

    # @token_required
    def get(self, uuid=None):
        if not uuid:
            films = FilmService.fetch_all_films(db.session).options(
                selectinload(Film.actors)
            )
            return self.film_schema.dump(films, many=True), 200
        film = FilmService.fetch_film_by_uuid(db.session, uuid)
        if not film:
            return 'not film', 404
        return self.film_schema.dump(film), 200

    def post(self):
        try:
            film = self.film_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(film)
        db.session.commit()
        return self.film_schema.dump(film), 201

    def put(self, uuid):
        film = FilmService.fetch_film_by_uuid(db.session, uuid)
        if not film:
            return "", 404
        try:
            film = self.film_schema.load(request.json, instance=film, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(film)
        db.session.commit()
        return self.film_schema.dump(film), 200

    def patch(self, uuid):
        film = FilmService.fetch_film_by_uuid(db.session, uuid)

        # film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return "", 404
        film = self.film_schema.load(request.json, instance=film, session=db.session, partial=True)

        # film_json = request.json
        # title = film_json.get('title')
        # distributed_by = film_json.get('distributed_by')
        # rating = film_json.get('rating')
        # length = film_json.get('length')
        # description = film_json.get('description')
        # release_date = datetime.strptime(film_json.get('release_date'), '%Y-%m-%d') if film_json.get(
        #     'release_date') else None
        #
        # if title:
        #     film.title = title
        # elif release_date:
        #     film.release_date = release_date
        # elif distributed_by:
        #     film.distributed_by = distributed_by
        # elif rating:
        #     film.rating = rating
        # elif length:
        #     film.length = length
        # elif description:
        #     film.description = description
        #

        db.session.add(film)
        db.session.commit()
        return self.film_schema.dump(film), 200

        # return {'message': 'Updated successfully'}, 200

    def delete(self, uuid):
        film = FilmService.fetch_film_by_uuid(db.session, uuid)
        if not film:
            return {'message': 'None'}, 404
        db.session.delete(film)
        db.session.commit()
        return "", 204
