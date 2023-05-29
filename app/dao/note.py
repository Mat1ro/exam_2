from app.dao.model.note import Note


class NoteDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, nid):
        return self.session.query(Note).get(nid)

    def get_all(self):
        return self.session.query(Note).all()

    def create(self, note_d):
        note = Note(**note_d)
        self.session.add(note)
        self.session.commit()
        return note

    def delete(self, nid):
        note = self.get_one(nid)
        self.session.delete(note)
        self.session.commit()

    def update(self, note_d):
        note = self.get_one(note_d.get("id"))
        note.text = note_d.get("text")

        self.session.add(note)
        self.session.commit()
