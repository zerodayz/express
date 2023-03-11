import pytest as pytest
from express import utils


@pytest.mark.parametrize('credentials', utils.load_json('accounts.json'))
def test_generated(actions, credentials):
    actions.set_credentials(credentials["username"], credentials["password"])
    actions.go("https://recaptcha-demo.appspot.com/recaptcha-v3-request-scores.php")
    actions.mouse_click("css=.go")
    actions.take_screenshot(filename="recaptcha_v3.png", element="class=response")
