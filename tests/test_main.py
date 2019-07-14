import pytest

import unixtime


def test_main():
    now = unixtime.now()
    dtcurrent = unixtime.current_datetime()
    tscurrent = unixtime.from_datetime(dtcurrent)
    dtnow = unixtime.to_datetime(now)
    tsnow = unixtime.from_datetime(dtnow)
    assert round(now) == round(tsnow)
    assert round(now) == round(tscurrent)
    assert dtnow.isoformat().endswith("+00:00")
    assert dtcurrent.isoformat().endswith("+00:00")
