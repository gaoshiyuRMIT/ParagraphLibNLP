import sqlalchemy as _sa
from app import db

class PostManager(object):
    TABLE = "Post join Author on Post.author_id = Author.id"
    FIELDS = "Post.id as post_id, Post.*, Author.*"

    @property
    def conn(self):
        return db.connect()

    def get_many(self, filt: dict) -> list:
        sql = f"select {self.FIELDS} from {self.TABLE}"
        if len(filt) > 0:
            sql += " where "
        conds = []
        for k in filt.keys():
            conds.sppend(f"{k} = :{k}")
        sql += " and ".join(conds)
        result = None
        with self.conn as conn:
            result = conn.execute(sql, **filt)
        return [self.transformRow(r) for r in result]

    @staticmethod
    def transformRow(row):
        d = dict(row)
        d.pop("id")
        return d
        
