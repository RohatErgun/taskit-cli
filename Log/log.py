from datetime import datetime

"""
    adding logs of user's commands which functions used and what is the outcome
    keeps the record in the txt file
"""


class LogSystem:
    @staticmethod
    def logged(function):

        def wrapper(*args, **kwargs):
            now = datetime.now()
            values = function(*args, **kwargs)

            with open('logfile.txt', 'a+') as f:
                fun_name = function.__name__
                timestamp = now.day, now.month, now.year
                f.write(f"\nUser used: <{fun_name}> function has returned with:\t{values}\ttimestamp:{timestamp}")

            return values
        return wrapper

