import json
from src.models.history_model import HistoryModel
from src.models.user_model import UserModel

user_mock = {"name": "um nome", "level": "admin", "token": "um token"}
history_mock_1 = {
    "text-to-translate": "ola me chamo Ana",
    "translate-from": "pt",
    "translate-to": "en",
}
history_mock_2 = {
    "text-to-translate": "hello my name is Jhon",
    "translate-from": "en",
    "translate-to": "pt",
}


def test_history_delete(app_test):
    UserModel(user_mock).save()
    HistoryModel(history_mock_1).save()
    HistoryModel(history_mock_2).save()

    id = json.loads(HistoryModel.list_as_json())[0]["_id"]
    app_test.delete(
        f"/admin/history/{id}",
        headers={
            "Authorization": "um token",
            "User": "um nome",
        },
    )

    assert len(json.loads(HistoryModel.list_as_json())) == 1
