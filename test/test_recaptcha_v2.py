def test_recaptcha_v2(actions):
    actions.go("https://patrickhlauke.github.io/recaptcha/")
    actions.switch_to_iframe("css=.g-recaptcha iframe")
    actions.click("css=.recaptcha-checkbox-border")
    actions.wait_for_element("class=recaptcha-checkbox-checked")
    actions.switch_to_default_content()
    actions.take_screenshot("recaptcha_v2.png")
