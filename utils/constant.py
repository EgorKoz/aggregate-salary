"""Constants"""


TYPE_FORMATS = {
    "month": "%Y-%m-01T00:00:00",
    "day":   "%Y-%m-%dT00:00:00",
    "hour":  "%Y-%m-%dT%H:00:00",
}
ERROR_STRING = (
    'Допустимо отправлять только следующие запросы:\n'
    '{"dt_from": "2022-09-01T00:00:00", "dt_upto": "2022-12-31T23:59:00", "group_type": "month"}\n'
    '{"dt_from": "2022-10-01T00:00:00", "dt_upto": "2022-11-30T23:59:00", "group_type": "day"}\n'
    '{"dt_from": "2022-02-01T00:00:00", "dt_upto": "2022-02-02T00:00:00", "group_type": "hour"}'
)
