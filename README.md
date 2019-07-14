# Unix Time

I spent way too much time figuring out how to use Unix timestamps. Two class methods of `datetime.datetime` do not work the way I expected them to work.

This is what I figured out:
 * The `datetime` module handles two different types of datetimes:
   1. "naive" times don't know their timezone
   2. "aware" times do know their timezone
 * Most functions treat a naive time as a local time
 * `datetime.utcnow()` is evil: it creates a naive time that is not local time
 * Use `datetime.now(UTC)` instead
 * `datetime.utcfromtimestamp()` has the same problem. Use `datetime.fromtimestamp(ts,UTC)` instead.
 * Avoiding use of naive datetimes will make your life better.

Read the [datetime module documentation](https://docs.python.org/3/library/datetime.html). Pay attention to the section at the beginning of the page that discusses *naive* datetimes and *aware* datetimes. If you don't fully understand the difference, **you *will* create subtle, hard-to-diagnose bugs**.

I posted this to Facebook along with a gist that demonstrated my findings. As it happens, the code didn't work for Python 2.7.

I fiddled with it some more, trying to backport it. This very simple project is what I came up with.

```
>>> import unixtime
>>> unixtime.now()
1563079528.8492017
>>> unixtime.to_datetime(_)
datetime.datetime(2019, 7, 14, 4, 45, 28, 849202, tzinfo=datetime.timezone.utc)
>>> unixtime.from_datetime(_)
1563079528.849202
>>> unixtime.current_datetime()
datetime.datetime(2019, 7, 14, 4, 46, 37, 249627, tzinfo=datetime.timezone.utc)
>>> unixtime.from_datetime(_)
1563079597.249627
>>> unixtime.to_datetime(_)
datetime.datetime(2019, 7, 14, 4, 46, 37, 249627, tzinfo=datetime.timezone.utc)
>>>
```

The code for this module is simple enough that there is no need to install it. All of these functions are one-liners. Just learn from it the correct way to use the `datetime` module. If you are stuck maintaining Python 2.7 code :-( and are not using `pytz`, you can steal `FixedOffsetTimeZone` to define UTC.