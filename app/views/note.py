from flask_restx import Resource, Namespace
from flask import request

from app.dao.model.note import NoteSchema
from app.container import note_service

note_ns = Namespace('notes')


@note_ns.route('/')
class NotesView(Resource):
    def get(self):
        notes = note_service.get_all()
        res = NoteSchema(many=True).dump(notes)
        return res, 200

    def post(self):
        req_json = request.json
        note = note_service.create(req_json)
        return "status: ok", 201, {"location": f"/notes/{note.id}"}


@note_ns.route('/<int:nid>')
class GenreView(Resource):
    def get(self, nid):
        note = note_service.get_one(nid)
        res = NoteSchema().dump(note)
        return res, 200

    def put(self, nid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = nid
        note_service.update(req_json)
        return "changed", 204

    def delete(self, nid):
        note_service.delete(nid)
        return "deleted", 204
