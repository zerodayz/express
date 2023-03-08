from express import utils


def find_nearest_xpath(self, element):
    """
    The checkbox can't be highlighted, we need to find the nearest element that can be.

    Args:
        element (string): String representing the inner element of the element
                          to be highlighted (xpath)

    Returns:
        tuple: The nearest element that can be highlighted

    Raises:
        Exception: If element not found or if any exception occurs
    """
    element = utils.determine_locator(element)
    # Check the element is type XPath
    if element[0] != "xpath":
        self.driver.quit()

        raise Exception(f"element '{element}' is not of type XPath. Please use XPath element.")
    try:

        self.wait_for_element_presence(element)
        # find the nearest wrapping element that can be highlighted
        return element[0], element[1] + "/.."
    except Exception as e:
        print("Error: ", e)
        self.driver.quit()
        raise e
