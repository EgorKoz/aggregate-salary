"""Module common function"""
from datetime import datetime as dt
from json import dumps

from utils.db import aggregate_data
from utils.constant import TYPE_FORMATS, ERROR_STRING


def get_aggregate_salary(params: dict) -> str:
    try:
        dt_from = dt.fromisoformat(params['dt_from'])
        dt_upto = dt.fromisoformat(params['dt_upto'])
        dt_format = TYPE_FORMATS.get(params['group_type'])
    except ValueError:
        return ERROR_STRING

    aggregated_results = aggregate_data(dt_from, dt_upto, dt_format)

    dataset, labels = zip(
        *[
            [result["total"], dt.strptime(result["_id"], dt_format).isoformat()]
            for result in aggregated_results
        ]
    )

    return dumps({"dataset": dataset, "labels": labels})
