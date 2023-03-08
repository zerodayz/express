import pytest as pytest


@pytest.mark.parametrize(
    "credentials",
    [
        {
            "username": "demo",
            "password": "demo"
        },
        {
            "username": "admin",
            "password": "admin"
        }
    ],
)
def test_login(actions, credentials):
    actions.set_credentials(credentials["username"], credentials["password"])

    actions.login(url="http://127.0.0.1:8000/login", submit="css=.w3-button")
    actions.take_screenshot("login.png")
    actions.go("http://127.0.0.1:8000/logout")
