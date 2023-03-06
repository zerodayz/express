def test_checkbox(actions):
    actions.prepare_tests("test_checkbox")
    actions.go("https://formy-project.herokuapp.com/checkbox")

    for checkbox in range(1, 4):
        actions.click(f"xpath=//input[@id='checkbox-{checkbox}']")
        # Highlighting checkbox is not possible, highlight the nearest element instead.
        # Requires XPath
        actions.highlight_nearest_xpath(f"xpath=//input[@id='checkbox-{checkbox}']")
        actions.take_screenshot(f"checkbox_{checkbox}.png")
        actions.remove_highlight_nearest_xpath(f"xpath=//input[@id='checkbox-{checkbox}']")
