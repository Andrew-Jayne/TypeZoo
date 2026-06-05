import json
from logging import (
    Formatter,
    LogRecord,
)
from typing import override


class JSONFormatter(Formatter):
    @override
    def format(self, record: LogRecord) -> str:
        return json.dumps(
            {
                "level": record.levelname,
                "time": self.formatTime(record, self.datefmt),
                "module": record.name,
                "text": record.getMessage(),
            }
        )
