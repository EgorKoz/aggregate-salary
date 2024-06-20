"""Constants"""
import re


ISO_FORMAT = r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}'
REQUEST_PATTERN = re.compile(
    rf'^{{\"dt_from\": \"{ISO_FORMAT}\", '
    rf'\"dt_upto\": \"{ISO_FORMAT}\", '
    rf'\"group_type\": \"(hour|day|month)\"}}$'
)
ERROR_STRING = (
    'Невалидный запрос. Пример запроса:\n'
    '{"dt_from": "2022-09-01T00:00:00", '
    '"dt_upto": "2022-12-31T23:59:00", "group_type": "month"}'
)
