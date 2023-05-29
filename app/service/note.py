from app.dao.note import NoteDAO


class NoteService:
    def __init__(self, dao: NoteDAO):
        self.dao = dao

    def get_one(self, nid):
        return self.dao.get_one(nid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, note_d):
        return self.dao.create(note_d)

    def update(self, note_d):
        self.dao.update(note_d)
        return self.dao

    def delete(self, nid):
        self.dao.delete(nid)