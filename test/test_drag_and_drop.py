def test_drag_and_drop(actions):
    actions.go("https://formy-project.herokuapp.com/dragdrop")
    actions.take_screenshot("drag_and_drop_1.png")
    actions.mouse_drag_and_drop("id=image", "id=box")
    actions.take_screenshot("drag_and_drop_2.png")
