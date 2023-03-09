def test_datepicker(actions):
    actions.go("https://formy-project.herokuapp.com/datepicker")
    actions.take_screenshot("datepicker_1.png")

    actions.mouse_click("id=datepicker")
    actions.take_screenshot("datepicker_2.png", highlight=True, highlight_element="css=.datepicker-days",)

    # select a random date, 2nd row, 7th column
    actions.mouse_click("css=tr:nth-child(2) > .day:nth-child(7)")
    actions.take_screenshot("datepicker_3.png")
