import http
import json
from unittest.mock import patch
from dataclasses import dataclass

from src import create_app

app = create_app()


@dataclass
class FakeActor:
    name = 'Fake Name'
    birthday = '2002-12-03'
    is_active = False


class TestActors:
    id = []

    def test_get_actors_with_db(self):
        client = app.test_client()
        resp = client.get('/actors')

        assert resp.status_code == http.HTTPStatus.OK

    @patch('src.services.actor_service.ActorService.fetch_all_actors', autospec=True)
    def test_actors_mock_db(self, mock_db_call):
        client = app.test_client()
        resp = client.get('/actors')
        mock_db_call.assert_called_once()
        assert resp.status_code == http.HTTPStatus.OK
        assert len(resp.json) == 0

    def test_create_actor_with_db(self):
        client = app.test_client()
        data = {
            'name': 'Sake Name',
            'birthday': '2002-12-03',
            'is_active': True
        }
        resp = client.post('/actors', data=json.dumps(data), content_type='application/json')
        assert resp.status_code == http.HTTPStatus.CREATED
        assert resp.json['name'] == 'Sake Name'
        self.id.append(resp.json['id'])

    def test_create_actor_with_mock_db(self):
        with patch('src.database.models.db.session.add', autospec=True) as mock_session_add, \
                patch('src.database.models.db.session.commit', autospec=True) as mock_session_commit:
            client = app.test_client()
            data = {
                'name': 'Test Name',
                'birthday': '2002-12-03',
                'is_active': True
            }
            resp = client.post('/actors', data=json.dumps(data), content_type='application/json')
            mock_session_add.assert_called_once()
            mock_session_commit.assert_called_once()

    def test_update_film_with_db(self):
        id = '9'
        client = app.test_client()
        url = f'/actors/{id}'

        data = {
            'name': 'Test Name',
            'birthday': '2002-12-03',
            'is_active': False
        }
        resp = client.put(url, data=json.dumps(data), content_type='application/json')
        assert resp.status_code == http.HTTPStatus.OK
        assert resp.json['is_active'] == False

    def test_update_film_with_mock_db(self):
        with patch('src.services.actor_service.ActorService.fetch_actor_by_id') as mocked_query, \
                patch('src.database.models.db.session.add', autospec=True) as mock_session_add, \
                patch('src.database.models.db.session.commit', autospec=True) as mock_session_commit:
            mocked_query.return_value = FakeActor()
            client = app.test_client()
            url = f'/actors/1'
            data = {
                'name': 'Test Name',
                'birthday': '2002-12-03',
                'is_active': False
            }
            resp = client.put(url, data=json.dumps(data), content_type='application/json')
            mock_session_add.assert_called_once()
            mock_session_commit.assert_called_once()


    def test_patch_actor_with_db(self):
        id = '2'
        client = app.test_client()
        url = f'/actors/{id}'

        data = {
            'name': 'Name'
        }
        resp = client.patch(url, data=json.dumps(data), content_type='application/json')
        assert resp.status_code == http.HTTPStatus.OK
        assert resp.json['name'] == 'Name'


    def test_patch_actor_with_mock_db(self):
        with patch('src.services.actor_service.ActorService.fetch_actor_by_id') as mocked_query, \
                patch('src.database.models.db.session.add', autospec=True) as mock_session_add, \
                patch('src.database.models.db.session.commit', autospec=True) as mock_session_commit:
            mocked_query.return_value = FakeActor()
            client = app.test_client()
            url = f'/actors/1'
            data = {
                'name': 'Update Name'
            }
            resp = client.patch(url, data=json.dumps(data), content_type='application/json')
            mock_session_add.assert_called_once()
            mock_session_commit.assert_called_once()

    def test_delete_actor_with_db(self):
        id = '10'
        client = app.test_client()
        url = f'/actors/{id}'
        resp = client.delete(url)
        assert resp.status_code == http.HTTPStatus.NO_CONTENT
