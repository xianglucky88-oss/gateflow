import pytest

def test_session_is_open_gap():
    from src.gateflow import session
    with pytest.raises(NotImplementedError):
        session.process({"id": "x"})

def test_steps_is_open_gap():
    from src.gateflow import steps
    with pytest.raises(NotImplementedError):
        steps.process({"id": "x"})
