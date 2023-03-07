from selenium.common.exceptions import StaleElementReferenceException


def element_attribute_is(locator, attribute_, expected_value):
    """An expectation for checking if the given attribute is included in the
    specified element.

    locator, attribute
    """

    def _predicate(driver):
        try:
            element_attribute = driver.find_element(*locator).get_attribute(attribute_)
            return element_attribute == expected_value
        except StaleElementReferenceException:
            return False

    return _predicate
