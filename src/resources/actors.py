from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from datetime import datetime
from src.schemas.actors import ActorSchema
from sqlalchemy.orm import selectinload
from src.database.models import db, Actor
from src.services.actor_service import ActorService


class ActorListApi(Resource):
    actor_schema = ActorSchema()

    def get(self, id=None):
        if not id:
            actors = ActorService.fetch_all_actors(db.session).options(
                selectinload(Actor.films)
            )
            # actors = db.session.query(Actor).all()
            return self.actor_schema.dump(actors, many=True), 200
        # actor = db.session.query(Actor).filter_by(id=id).first()
        actor = ActorService.fetch_actor_by_id(db.session, id)
        if not actor:
            return 'not film', 404
        return self.actor_schema.dump(actor), 200

    def post(self):
        try:
            actor = self.actor_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(actor)
        db.session.commit()
        return self.actor_schema.dump(actor), 201

    def put(self, id):
        actor = ActorService.fetch_actor_by_id(db.session, id)
        # actor = db.session.query(Actor).filter_by(id=id).first()
        if not actor:
            return "", 404
        try:
            actor = self.actor_schema.load(request.json, instance=actor, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(actor)
        db.session.commit()
        return self.actor_schema.dump(actor), 200

    def patch(self, id):
        actor = ActorService.fetch_actor_by_id(db.session, id)
        if not actor:
            return "", 404

        actor = self.actor_schema.load(request.json, instance=actor, session=db.session, partial=True)

        # actor_json = request.json
        # name = actor_json.get('name')
        # is_active = actor_json.get('is_active')
        # birthday = datetime.strptime(actor_json.get('birthday'), '%Y-%m-%d') if actor_json.get(
        #     'birthday') else None
        #
        # if name:
        #     actor.name = name
        # elif is_active:
        #     actor.is_active = is_active
        # elif birthday:
        #     actor.birthday = birthday

        db.session.add(actor)
        db.session.commit()
        return self.actor_schema.dump(actor), 200

        # return {'message': 'Updated successfully'}, 200

    def delete(self, id):
        actor = ActorService.fetch_actor_by_id(db.session, id)
        if not actor:
            return "", 404
        db.session.delete(actor)
        db.session.commit()
        return '', 204
