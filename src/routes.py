# from datetime import datetime
# from flask import request
# from flask_restful import Resource
# from marshmallow import ValidationError
#
# from .models import db, Film
# from .schemas import FilmSchema
#
#
# class Smoke(Resource):
#     def get(self):
#         return {'message': 'ok'}, 200
#
#
# class FilmListApi(Resource):
#     film_schema = FilmSchema()
#
#     def get(self, uuid=None):
#         if not uuid:
#             films = db.session.query(Film).all()
#             return self.film_schema.dump(films, many=True), 200
#             # return [f.to_dict() for f in films], 200
#         film = db.session.query(Film).filter_by(uuid=uuid).first()
#         if not film:
#             return 'not film', 404
#         return self.film_schema.dump(film), 200
#         # return film.to_dict(), 200
#
#     def post(self):
#         try:
#             film = self.film_schema.load(request.json, session=db.session)
#         except ValidationError as e:
#             return {'message': str(e)}, 400
#         db.session.add(film)
#         db.session.commit()
#         return self.film_schema.dump(film), 201
#
#         # film_json = request.json
#         # if not film_json:
#         #     return {'message': 'Wrng data'}, 400
#         # try:
#         #     film = Film(
#         #         title=film_json['title'],
#         #         release_date=datetime.strptime(film_json['release_date'], '%B %d, %Y'),
#         #         distributed_by=film_json['distributed_by'],
#         #         description=film_json.get('description'),
#         #         length=film_json.get('length'),
#         #         rating=film_json.get('rating')
#         #     )
#         #     db.session.add(film)
#         #     db.session.commit()
#         #     print('exelent')
#         # except (ValueError, KeyError):
#         #     return {'message': 'Wrongg data'}, 400
#         # return {'message': 'Created successfully'}, 201
#
#     def put(self, uuid):
#         film = db.session.query(Film).filter_by(uuid=uuid).first()
#         if not film:
#             return "", 404
#         try:
#             film = self.film_schema.load(request.json, instance=film, session=db.session)
#         except ValidationError as e:
#             return {'message': str(e)}, 400
#         db.session.add(film)
#         db.session.commit()
#         return self.film_schema.dump(film), 200
#
#         # film_json = request.json
#         # if not film_json:
#         #     return {'message': 'Wrong data'}, 400
#         # try:
#         #     db.session.query(Film).filter_by(uuid=uuid).update(
#         #         dict(
#         #             titel=film_json['title'],
#         #             release_date=datetime.strptime(film_json['release_date'], '%B %d, %Y'),
#         #             distributed_by=film_json['distributed_by'],
#         #             description=film_json.get('description'),
#         #             length=film_json.get('length'),
#         #             rating=film_json.get('rating')
#         #         )
#         #     )
#         #     db.session.commit()
#         # except (ValueError, KeyError):
#         #     return {'message': 'Wrong data'}, 400
#         # return {'message': 'Updated successfully'}, 200
#
#     def patch(self, uuid):
#         film = db.session.query(Film).filter_by(uuid=uuid).first()
#         if not film:
#             return '', 404
#         film_json = request.json
#         title = film_json.get('titel'),
#         release_date = datetime.strptime(film_json['release_date'], '%B %d, %Y'),
#         distributed_by = film_json.get['distributed_by'],
#         description = film_json.get('description'),
#         length = film_json.get('length'),
#         rating = film_json.get('rating')
#
#         if title:
#             film.title = title
#         elif release_date:
#             film.release_date = release_date
#         elif distributed_by:
#             film.distributed_by = distributed_by
#         elif rating:
#             film.rating = rating
#         elif length:
#             film.length = length
#         elif description:
#             film.description = description
#
#         db.session.add(film)
#         db.session.commit()
#         return {'message': 'Updated successfully'}, 200
#
#     def delete(self, uuid):
#         film = db.session.query(Film).filter_by(uuid=uuid).first()
#         if not film:
#             return "", 404
#         db.session.delete(film)
#         db.session.commit()
#         return '', 204
#
#
# class ActorListApi(Resource):
#
#     def get(self, uuid=None):
#         pass
#
#     def post(self):
#         pass
#
#     def put(self):
#         pass
#
#     def patch(self):
#         pass
#
#     def delete(self):
#         pass
