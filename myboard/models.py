from myboard import db

class Content(db.Model):

    __tablename__ = 'contents'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    text = db.Column(db.Text)

    def __repr__(self):
        return '<Entry id={} name={!r} text={!r}>'.format(
                self.id, self.name, self.text)

def init():
    db.create_all()
