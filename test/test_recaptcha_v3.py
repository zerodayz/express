import time


def test_recaptcha_v3(actions):
    actions.prepare_tests("test_recaptcha_v3")
    actions.go("https://recaptcha-demo.appspot.com/recaptcha-v3-request-scores.php")
    actions.click("css=.go")
    actions.take_screenshot("recaptcha_v3.png", element="class=response")
