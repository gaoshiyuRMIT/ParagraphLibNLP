from flask import request, jsonify
from app import logger, db, app
from managers import PostManager


@app.route('/ping')
def ping():
    return "hello world"


@app.route('/search', methods=["POST"])
def search():
    filt = request.json or {}
    mgr = PostManager()
    return jsonify(mgr.get_many(filt))
