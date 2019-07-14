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
 * Avoiding use naive times will make your life better.

I posted this to Facebook along with a gist that demonstrated my findings. As it happens, the code didn't work for Python 2.7.

I fiddled with it some more, trying to backport it. This very simple project is what I came up with.

