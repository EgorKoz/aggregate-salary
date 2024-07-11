"""Module db function"""
import logging

import bson
from datetime import datetime

from pymongo import MongoClient
from pymongo.collection import Collection, CommandCursor


def get_collection() -> Collection:
    logging.info('get collection')
    collection = MongoClient('mongo_db', 27017)['task'].get_collection('salary')
    if not collection.find_one():
        with open('sample_collection.bson', 'rb') as bson_file:
            collection.insert_many(bson.decode_all(bson_file.read()))

    return collection


def aggregate_data(
        dt_from: datetime, dt_upto: datetime, dt_format: str) -> CommandCursor:
    return salary_data.aggregate([
        {"$match": {"dt": {"$gte": dt_from, "$lte": dt_upto}}},
        {"$group": {
            "_id": {"$dateToString": {"format": dt_format, "date": "$dt"}},
            "total": {"$sum": "$value"},
        }},
        {"$sort": {"_id": 1}},
    ])


salary_data = get_collection()
