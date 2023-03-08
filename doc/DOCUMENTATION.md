# express package

## Submodules

## express.expected_conditions module


### express.expected_conditions.element_attribute_is(locator, attribute_, expected_value)
An expectation for checking if the given attribute is set to expected value.

locator, attribute

## express.express module


### _class_ express.express.Actions(driver, caplog)
Bases: `object`


#### \__init__(driver, caplog)

#### click(element)
Click on an element.

Args:

    element (string): String representing the element to be clicked

Returns:

    None

Raises:

    Exception: If element not found or if any exception occurs


#### drag_and_drop(element_from, element_to)
This function drags an element to another element.

Args:

    element_from (str): The element to drag.
    element_to (str): The element to drop the first element on.

Returns:

    None

Raises:

    Exception: In case of any error.


#### find_nearest_xpath(element)
The checkbox can’t be highlighted, we need to find the nearest element that can be.

Args:

    element (string): String representing the inner element of the element

        to be highlighted (xpath)

Returns:

    tuple: The nearest element that can be highlighted

Raises:

    Exception: If element not found or if any exception occurs


#### get_style(element)
This function gets the style of an element.

Params:

    element (str): An element locator.

Returns:

    str: The style of the element.

Raises:

    Exception: In case of any error.


#### go(url)
Navigates the web driver to the given URL, and waits for the page to load.

Params:

    url (str): The URL that the browser should navigate to.

Returns:

    None

Raises:

    Exception: If there was an error loading the page.


#### highlight(element, style='border: 2px solid rgb(255, 0, 0);')
This function highlights the given element on the web page.

Args:

    element (tuple): The element to be highlighted.
    style (str): The style to use for the highlight.

Returns:

    None

Raises:

    Exception: If the element is not located on the page.


#### hover(element)
This function hovers to an element on the page and performs an action.

Args:

    element: The element to be hovered.

Returns:

    None.

Raises:

    Exception: If any error occurs.


#### load_json(filename)
This function loads a JSON file and returns the data.

Args:

    filename (str): The name of the JSON file.

Returns:

    dict: The data from the JSON file.

Raises:

    Exception: If there is an error loading the JSON file.


#### login(url, username=None, password=None, username_locator='name=username', password_locator='name=password', submit='name=submit')
Logs into the website using the provided username and password

Args:

    url (str): The URL of the website
    username_locator (str): The locator for the username field
    username (str): The username for authenticating the account
    password_locator (str): The locator for the password field
    password (str): The password for authenticating the account
    submit (str): The locator for the login button

Returns:

    None

Raises:

    Exception: If there is an error while logging in


#### move_mouse_to(x, y)
This function moves the mouse to the given coordinates.

Args:

    x (int): The x coordinate to move the mouse to.
    y (int): The y coordinate to move the mouse to.

Returns:

    None

Raises:

    Exception: In case of any error.


#### move_mouse_to_element(element)
This function moves the mouse to the given element.

Params:

    element (str): An element locator.

Returns:

    None

Raises:

    Exception: In case of any error.


#### prepare_tests(test_name)

#### remove_highlight(element, style=None)
This function clears the highlight from the given element on the web page.

Args:

    element (tuple): The highlighted element to be cleared.
    style (str): The style to use for the highlight.

Returns:

    None

Raises:

    Exception: If the element is not located on the page.


#### scroll_into_element(element)
This function is waiting for it to be present before executing the script.

Params:

    element (tuple): The element to be scrolled into view.

Returns:

    None

Raises:

    Exception: In case of any error.


#### set_credentials(username, password)
Sets the username and password for the actions class

Params:

    username (str): The username to be used
    password (str): The password to be used

Returns:

    None


#### switch_to_default_content()
This function switches the web driver to the default content.

Params:

    None

Returns:

    None

Raises:

    Exception: In case of any error.


#### switch_to_iframe(element)
This function switches the web driver to the given iframe.

Params:

    element (str): The iframe to switch to.

Returns:

    None

Raises:

    Exception: In case of any error.


#### take_screenshot(filename, element='tag=body', highlight=False, highlight_element=None, highlight_style='border: 2px solid rgb(255, 0, 0);', annotate_text=None)
This function takes a screenshot of the web page and saves it in filename.

Params:

    locator (string): Name of the element to take a screenshot of.
    filename (string): Name of the file to save the screenshot.
    highlight (bool): If true, the element will be highlighted before taking the screenshot.
    highlight_style (string): The style to use for the highlight.
    annotate_text (string): Text to annotate the screenshot with.

Returns:

    None

Raises:

    Exception: In case of any error.


#### type(element, text)
This function will type text into an element on a web page.

Args:

    element (str): An element locator.
    text (str): The text to type into the element.

Returns:

    None

Raises:

    Exception: In case of any error.


#### wait_between(w_min, w_max)
This function waits for a random amount of time between min and max.

Params:

    w_min (int): The minimum amount of time to wait.
    w_max (int): The maximum amount of time to wait.

Returns:

    None

Raises:

    Exception: In case of any error.


#### wait_for_element_clickable(element, timeout=60)
This function waits for an element to be clickable on the web page.

Params:

    element (str): An element locator.
    timeout (int): The number of seconds to wait before timing out.

Returns:

    None

Raises:

    Exception: In case of any error.


#### wait_for_element_presence(element, timeout=60)
This function waits for an element to be present on the web page.

Params:

    element (str): An element locator.
    timeout (int): The number of seconds to wait before timing out.

Returns:

    None

Raises:

    Exception: In case of any error.


#### wait_for_page_to_load(url)
This function checks if the current page URL is the same as the given URL.

Params:

    url (str): The URL to check.

Returns:

    None

Raises:

    Exception: In case of any error.


#### wait_for_style(element, style, timeout=60)
This function waits for an element to have a specific style.

Params:

    element (str): An element locator.
    style (str): The style to wait for.
    timeout (int): The number of seconds to wait before timing out.

Returns:

    None

Raises:

    Exception: In case of any error.


### express.express.determine_locator(element)
This function determines the locator used to find an element on a web page.

Params:

    locator (str): The locator used to locate an element on a web page.

Returns:

    By (object): An object of the selenium.webdriver.common.by class.
    Name (str): The name of the locator.

Raises:

    ValueError: If the locator prefix is invalid.


### express.express.validate_style(style)
This function validates the given style.

Args:

    style (str): The style to validate.

Returns:

    str: The validated style.

Raises:

    Exception: If the style is not valid.

## express.utils module


### express.utils.annotate(image, text, color=(255, 0, 0), size=64)
## Module contents
