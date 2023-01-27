from flask_restful import Resource
from sqlalchemy import func

from src.database.models import db, Film


class AggregationApi(Resource):
    def get(self):
        films_count = db.session.query(func.count(Film.id)).scalar()
        max_rating = db.session.query(func.max(Film.id)).scalar()
        min_rating = db.session.query(func.min(Film.id)).scalar()
        avg_rating = db.session.query(func.avg(Film.id)).scalar()
        sum_rating = db.session.query(func.sum(Film.id)).scalar()
        return {
            'count': films_count,
            'max': max_rating,
            'min': min_rating,
            'avg': avg_rating,
            'sum': sum_rating
        }