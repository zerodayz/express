def test_generated(actions):
    actions.go("https://recaptcha-demo.appspot.com/recaptcha-v3-request-scores.php")
    actions.mouse_click("css=.go")
    actions.take_screenshot("recaptcha_v3.png", "class=response")
