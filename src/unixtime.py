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


def to_datetime(ts):
    """ return a timezone aware datetime representing the instant `ts` seconds since the epoch.

    `ts` the number of seconds elapsed since the epoch
    """
    return datetime.datetime.fromtimestamp(ts, utc)


def current_datetime():
    """ return a timezone aware datetime representing the current system time
    """
    return datetime.datetime.fromtimestamp(now(), utc)


def from_datetime(dt):
    """return the number of seconds elapsed since the epoch.
    
    `dt` a timezone aware datetime
    """
    return (dt - EPOCH).total_seconds()
