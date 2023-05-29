from app.dao.note import NoteDAO
from app.service.note import NoteService
from app.setup_db import db

note_dao = NoteDAO(session=db.session)

note_service = NoteService(dao=note_dao)
