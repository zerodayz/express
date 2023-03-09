class Style:
    def style_get_attribute(self, element):
        """
        This function gets the style of an element.

        Params:
            element (str): An element locator.

        Returns:
            str: The style of the element.

        Raises:
            Exception: In case of any error.
        """
        locator = self.determine_locator(element)
        try:
            self.wait_for_presence_of_element(locator)
            return self.driver.find_element(*locator).get_attribute("style")
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def style_remove_highlight(self, element, style=None):
        """
        This function clears the highlight from the given element on the web page.

        Args:
           element (tuple): The highlighted element to be cleared.
           style (str): The style to use for the highlight.

        Returns:
           None

        Raises:
           Exception: If the element is not located on the page.
        """
        locator = self.determine_locator(element)
        # If no style was specified, just reset the style to an empty string.
        # otherwise, use the style that was specified.
        if style is None:
            style = ''
        else:
            style = style
        try:
            self.wait_for_presence_of_element(locator)
            self.driver.execute_script("arguments[0].style = arguments[1];",
                                       self.driver.find_element(*locator), style)

        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def style_highlight(self, element, style="border: 2px solid rgb(255, 0, 0);"):
        """
        This function highlights the given element on the web page.

        Args:
           element (tuple): The element to be highlighted.
           style (str): The style to use for the highlight.

        Returns:
           None

        Raises:
           Exception: If the element is not located on the page.
        """
        locator = self.determine_locator(element)
        # validate css style
        style = self.validate_style(style)
        try:
            self.wait_for_presence_of_element(locator)
            # remove any color transition from the element https://github.com/SeleniumHQ/selenium/issues/11740
            # and update the element style to the given style
            self.driver.execute_script("arguments[0].style = arguments[1];",
                                       self.driver.find_element(*locator),
                                       style + "transition: none !important;")

        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e
