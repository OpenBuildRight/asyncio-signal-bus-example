# __main__.py
import logging
import sys

import uvicorn
from uvicorn.config import LOGGING_CONFIG

from asyncio_signal_bus_example.order_example.app import APP

if __name__ == "__main__":
    log_level = logging.INFO
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(fmt=formatter)

    root_logger.addHandler(handler)
    uvicorn.run(APP, port=8000)
