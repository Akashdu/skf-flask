
from skf.database import db


class checklists_kb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_pre_ID = db.Column(db.Integer)
    question_sprint_ID = db.Column(db.Integer)
    codeID_php = db.Column(db.Integer)
    codeID_asp = db.Column(db.Integer)
    codeID_java = db.Column(db.Integer)
    codeID_python = db.Column(db.Integer)
    include_always = db.Column(db.Boolean)
    include_first = db.Column(db.Boolean)
    checklistID = db.Column(db.String)
    content = db.Column(db.String)
    kbID = db.Column(db.Integer, db.ForeignKey("kb_items.kbID"))
    kb_items = db.relationship("kb_items", foreign_keys=[kbID])
    checklist_type = db.Column(db.Integer)

    def __init__(self, checklistID, content, kbID, checklist_type, include_always,include_first, question_pre_ID, question_sprint_ID):
        self.question_pre_ID = question_pre_ID
        self.question_sprint_ID = question_sprint_ID
        self.codeID_php = 0
        self.codeID_asp = 0
        self.codeID_java = 0
        self.codeID_python = 0
        self.include_always = include_always
        self.include_first = include_first
        self.checklistID = checklistID
        self.checklist_type = checklist_type
        self.content = content
        self.kbID = kbID
        self.kb_items = kbID
