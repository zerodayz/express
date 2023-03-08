from express import utils


def validate_style(style):
    """
    This function validates the given style.

    Args:
       style (str): The style to validate.

    Returns:
       str: The validated style.

    Raises:
       Exception: If the style is not valid.
    """
    if not style.endswith(";"):
        style = style + ";"
    return style


def get_style(self, element):
    """
    This function gets the style of an element.

    Params:
        element (str): An element locator.

    Returns:
        str: The style of the element.

    Raises:
        Exception: In case of any error.
    """
    locator = utils.determine_locator(element)
    try:
        self.wait_for_element_presence(locator)
        return self.driver.find_element(*locator).get_attribute("style")
    except Exception as e:
        print("Error: ", e)
        self.driver.quit()
        raise e
