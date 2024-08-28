#!/usr/bin/env python3

import logging
import sys

import contextual_logger

logger = logging.getLogger("demo")
logger.setLevel(logging.INFO)
# This utility is much more useful in settings where the extras can be flexibly
# added, for example by using json logging or one that only adds formatting if
# a key is defined.
formatter = logging.Formatter(
    fmt="[demo-log] %(asctime)s %(funcName)s %(message)s %(file)s"
)
handler = logging.StreamHandler(stream=sys.stdout)
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)
