import datetime
import time

try:
    utc = datetime.timezone.utc
except AttributeError:
    # workaround for pre Python 3.2

    class FixedOffsetTimeZone(datetime.tzinfo):
        __slots__ = ("name", "offset")

        def __init__(self, name, offset):
            self.name = name
            self.offset = offset

        def utcoffset(self, dt):
            return self.offset

        def tzname(self, dt):
            return self.name

        def dst(self, dt):
            return self.offset

        def __repr__(self):
            return "<{} '{}' {}>".format(
                self.__class__.__name__, self.name, self.offset
            )

    utc = FixedOffsetTimeZone("UTC", datetime.timedelta(0))

EPOCH = datetime.datetime.fromtimestamp(0, utc)


def to_datetime(ts):
    """ return a timezone aware datetime representing the instant `ts` seconds since the epoch.

    `ts` the number of seconds elapsed since the epoch
    """
    return datetime.datetime.fromtimestamp(ts, utc)


def current_datetime():
    """ return a timezone aware datetime representing the current system time
    """
    return datetime.datetime.fromtimestamp(time.time(), utc)


def from_datetime(dt):
    """return the number of seconds elapsed since the epoch.
    
    `dt` a timezone aware datetime
    """
    return (dt - EPOCH).total_seconds()
