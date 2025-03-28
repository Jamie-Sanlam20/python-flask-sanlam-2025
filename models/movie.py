import uuid

from extensions import db

# CREATE TABLE movies (
#     id NVARCHAR(50) PRIMARY KEY,
#     name NVARCHAR(100),
#     poster NVARCHAR(255),
#     rating FLOAT,
#     summary NVARCHAR(500),
#     trailer NVARCHAR(255)
# );

# need same information in create on python side


# Schema equivalent
class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(
        db.String(50), primary_key=True, default=lambda: str(uuid.uuid4())
    )  # converting uuid into str # uuid4 vs uuid1 -> as number increases, the randomness increases
    name = db.Column(db.String(100))
    poster = db.Column(db.String(255))
    rating = db.Column(db.Float)
    summary = db.Column(db.String(500))
    trailer = db.Column(db.String(255))

    # database returns as an object, convert to dict
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "poster": self.poster,
            "rating": self.rating,
            "summary": self.summary,
            "trailer": self.trailer,
        }
