def test_dropdown(actions):
    actions.go("https://formy-project.herokuapp.com/dropdown")
    actions.take_screenshot("dropdown_1.png", highlight=True, highlight_element="id=dropdownMenuButton",
                            annotate_text="Click the dropdown button to open the menu.")
    actions.click("id=dropdownMenuButton")

    actions.take_screenshot("dropdown_2.png", highlight=True, highlight_element="linkText=File Upload",
                            annotate_text="Click the File Upload link to open the File Upload page.")
    actions.click("linkText=File Upload")

    actions.wait_for_page_to_load("https://formy-project.herokuapp.com/fileupload")
    actions.take_screenshot("dropdown_3.png", annotate_text="The File Upload page should be now open.")
