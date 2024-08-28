#!/usr/bin/env python3

import logging
import random

try:
    import json_log
except ImportError:
    import log


LOGGER = logging.getLogger("demo")


def read_and_process(filename):
    with LOGGER(file=filename):
        # Would actually open a file and read in a real function
        f = ["example data1", "more data2", "", "last data3"]
        LOGGER.info("Reading from file!")
        data = []
        for i, line in enumerate(f):
            with LOGGER(line_number=i):
                if line:
                    data.append(parse_data(line))
        LOGGER.info("Munging the data")
        data = [transform_data(d) for d in data]


def per_line_processor(filename):
    with LOGGER(file=filename):
        # Would actually open a file and read in a real function
        f = ["example data1", "more data2", "", "last data3"]
        LOGGER.info("Reading from file!")
        data = []
        for i, line in enumerate(f):
            with LOGGER(line_number=i):
                if line:
                    d = parse_data(line)
                    d = transform_data(d)
                    data.append(d)


def parse_data(line):
    dtype, data = line.split()
    LOGGER.info(f"Parsed: {data} of type {dtype}")
    return data


def transform_data(d):
    r = random.random()
    with LOGGER(rval=r):
        if r < 0.5:
            return small_transform(d)
        return big_transform(d)


def small_transform(d):
    LOGGER.info("This data was tiny, quick process")
    return d


def big_transform(d):
    with LOGGER(d=d):
        LOGGER.info("This data was HUGE, need an inner processing function.")
        return inner_transform(d)


def inner_transform(d):
    LOGGER.info("Nested processing dude!")
    return d


def main():
    read_and_process("my_file.txt")
    per_line_processor("my_file.txt")


if __name__ == "__main__":
    main()
