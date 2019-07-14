import pytest

from unixtime.cli import main


def test_main(capsys):
    with pytest.raises(SystemExit) as e:
        main()
    assert e.type == SystemExit
    assert e.value.code == 0
    cap = capsys.readouterr()
    assert cap.out == "hello\n"
