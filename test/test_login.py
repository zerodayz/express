import pytest as pytest
from express import utils


@pytest.mark.parametrize('credentials', utils.load_json('accounts.json'))
def test_login(actions, credentials):
    actions.set_credentials(credentials["username"], credentials["password"])
    actions.go("http://127.0.0.1:8000/login")
    with actions.wait_for_page_to_load():
        actions.login(submit="css=.w3-button")
    actions.take_screenshot(filename="login.png")
    with actions.wait_for_page_to_load():
        actions.go("http://127.0.0.1:8000/logout")
