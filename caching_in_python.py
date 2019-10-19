#  Function caching in python

import time
from functools import lru_cache # lru is decorator


@lru_cache(maxsize = 3)
def some_work(n):
        # some task taking time
        time.sleep(n)
        return n

if __name__ == '__main__':
        print("Now running some work")
        some_work(5)
        print("done calling again")
        some_work(5)
        print("called again")