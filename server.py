from flask import Flask, jsonify, request
from flask.views import MethodView
from models import Announcement, Session
from sqlalchemy.exc import IntegrityError

app = Flask('app')


class AnnouncementView(MethodView):
    def get(self, announcement_id):
        with Session() as session:
            announcement = session.get(Announcement, announcement_id)
            if announcement is None:
                raise Exception()
            return jsonify({
                'id': announcement.id,
                'title': announcement.title,
                'description': announcement.description,
                'creation_datetime': announcement.creation_datetime,
                'owner': announcement.owner
            })
    
    def post(self):
        json_data = request.json
        with Session() as session:
            announcement = Announcement(**json_data)
            session.add(announcement)
            try:
                session.commit()
            except IntegrityError as err:
                raise err
            return jsonify({
                'id': announcement.id,
                'title': announcement.title,
                'description': announcement.description,
                'creation_datetime': announcement.creation_datetime,
                'owner': announcement.owner
            })
                

    def delete(self, announcement_id):
        with Session() as session:
            announcement = session.get(Announcement, announcement_id)
            if announcement is None:
                raise Exception()
            session.delete(announcement)
            session.commit()
            return jsonify({'status': 'deleted'})
        
app.add_url_rule(
    '/announcement/<int:announcement_id>', 
    view_func=AnnouncementView.as_view('with_id'),
    methods=['GET', 'DELETE'])

app.add_url_rule(
    '/announcement',
    view_func=AnnouncementView.as_view('create_announcement'),
    methods=['POST'])

app.run(host='0.0.0.0', port=5000)