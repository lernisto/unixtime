"""
Convenience functions for working with Unix timestamps.

1. Read the [datetime module documentation](https://docs.python.org/3/library/datetime.html). Pay attention to the section at the beginning of the page that discusses *naive* datetimes and *aware* datetimes. If you don't fully understand the difference, **you *will* create subtle, hard-to-diagnose bugs**.

2. Never use `datetime.datetime.utcfromtimestamp` or `datetime.datetime.utcnow` unless you **really** know what you are doing. These class methods create naive datetimes that are not in the local timezone. (see step #1)

3. Use aware datetimes whenever possible. This will just make your life better.

"""
import datetime
from time import time as now

try:
    utc = datetime.timezone.utc
except AttributeError:
    # workaround for Python <3.2

    class UTC(datetime.tzinfo):
        offset = datetime.timedelta(0)

        def utcoffset(self, dt):
            return self.offset

        def tzname(self, dt):
            return "UTC"

        def dst(self, dt):
            return self.offset

        def __repr__(self):
            return "datetime.timezone.utc"

    utc = UTC()

EPOCH = datetime.datetime.fromtimestamp(0, utc)


def from_datetime(dt):
    """return the number of seconds elapsed since the Unix epoch.
    
    `dt` a timezone aware datetime
    
    This function exists only because Python 2.7 `datetime` class is missing the `timestamp()` method. Unlike that method, this function will raise a TypeError 
    if you pass it a naive datetime. (This is a good thing. See step #1.)
    """
    return (dt - EPOCH).total_seconds()


def to_datetime(ts):
    """ return a timezone aware datetime (UTC) representing the instant `ts` seconds since the Unix epoch.

    `ts` the number of seconds elapsed since the epoch
    """
    return datetime.datetime.fromtimestamp(ts, utc)


def current_datetime(tzinfo=utc):
    """ return a timezone aware datetime representing the current system time.
    
    By default, the time will be in the UTC time zone. If you want something else, use [`.astimezone()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.astimezone) or pass this function the desired timezone.
    """
    return datetime.datetime.now(tzinfo)
