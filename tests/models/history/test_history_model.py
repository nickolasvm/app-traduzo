import json
from src.models.history_model import HistoryModel


def test_request_history() -> None:
    history = json.loads(HistoryModel.list_as_json())

    assert history[0]["text_to_translate"] == "Hello, I like videogame"
    assert history[1]["text_to_translate"] == "Do you love music?"
