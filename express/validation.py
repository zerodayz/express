from express import utils


class Validation:
    @staticmethod
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
