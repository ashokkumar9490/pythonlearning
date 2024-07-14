from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    __table_args__ = (
        db.UniqueConstraint('name', 'store_id', name='unique_item_in_store'),
    )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey(
        "stores.id"), unique=False, nullable=False)

    store = db.relationship("StoreModel", back_populates="items")
