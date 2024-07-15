#!/usr/bin/python3
"""
This script processes lines of input from standard input (stdin), typically
log entries, to count occurrences of specific HTTP status codes and sum the
sizes of responses. It maintains a count of occurrences for status codes
200, 301, 400, 401, 403, 404, 405, and 500. Every 10 lines, it prints the
total file size and the counts for each status code that has been seen at
least once. When the script ends, it prints the same information again.
"""
import sys


cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            code = line_list[-2]
            size = int(line_list[-1])
            if code in cache.keys():
                cache[code] += 1
            total_size += size
            counter += 1

        if counter == 10:
            counter = 0
            print('File size: {}'.format(total_size))
            for key, value in sorted(cache.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
