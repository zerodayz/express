import time


def test_recaptcha_v2(actions):
    actions.prepare_tests("test_recaptcha_v2")
    actions.go("https://patrickhlauke.github.io/recaptcha/")
    actions.driver.switch_to.frame(0)
    actions.click("css=.recaptcha-checkbox-border")
    actions.take_screenshot("recaptcha_v2.png")
