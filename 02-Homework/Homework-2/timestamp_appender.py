#!/usr/bin/python3

from datetime import datetime
import os


def append_timestamp_to_file_name(file_name):
    """Append timestamp to file name"""
    # current date time
    now = datetime.now()

    # convert to string
    date_time_str = now.strftime("%Y-%m-%d_%H:%M:%S_%f")

    file_path = os.path.dirname(file_name)
    file_name, file_extension = os.path.splitext(os.path.basename(file_name))

    # append timestamp to file name
    file_name_with_timestamp = file_name + "_" + date_time_str

    full_file_name = file_path + "/" + file_name_with_timestamp + file_extension
    return full_file_name
