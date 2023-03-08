def test_checkbox(actions):
    actions.go("https://formy-project.herokuapp.com/checkbox")

    for checkbox in range(1, 4):
        actions.click(f"xpath=//input[@id='checkbox-{checkbox}']")
        # Highlighting checkbox is not possible, highlight the nearest element instead.
        # Requires XPath
        outer_element = actions.find_nearest_xpath(f"xpath=//input[@id='checkbox-{checkbox}']")
        outline = "border: 2px solid rgb(255, 0, 0);"
        # outline = "background-color: yellow; border: 2px solid rgb(255, 0, 0);"
        # outline = "background-color: yellow;"
        actions.take_screenshot(f"checkbox_{checkbox}.png", highlight=True, highlight_element=outer_element,
                                annotate_text=f"Click checkbox {checkbox} to select it.", highlight_style=outline)
