#!/usr/bin/env python3

import logging
import sys

import logging_json

import contextual_logger

logger = logging.getLogger("demo")
logger.setLevel(logging.INFO)
formatter = logging_json.JSONFormatter(
    fields={
        "level_name": "levelname",
        "timestamp": "asctime",
        "module_name": "module",
        "function_name": "funcName",
        "logger": "name",
    }
)
handler = logging.StreamHandler(stream=sys.stdout)
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)
