
class ZibalError(Exception):
    """
    Custom exception for Zibal-related errors.

    Attributes:
        message (str): A description of the error.
        code (int): An optional error code from Zibal's API.
    """

    def __init__(self, message: str, code: int = None, details: dict = None):
        """
        Initializes the ZibalError with a message, optional error code, and optional details.

        Args:
            message (str): A description of the error.
            code (int, optional): The error code returned by Zibal's API, if available.
            details (dict, optional): Additional details or data related to the error.
        """
        self._message = message
        self._code = code
        self._details = details or {}  # Extra details, if any
        super().__init__(self._format_error())

    def _format_error(self) -> str:
        """
        Formats the error message for better readability.

        Returns:
            str: The formatted error message.
        """
        base_message = f"ZibalError: {self._message}"
        if self._code:
            base_message = f"ZibalError {self._code}: {self._message}"

        if self._details:
            return f"{base_message} | Details: {self._details}"
        return base_message

    @property
    def message(self) -> str:
        """
        Returns the error message.
        """
        return self._message

    @property
    def code(self) -> int:
        """
        Returns the error code, if any.
        """
        return self._code

    @property
    def details(self) -> dict:
        """
        Returns any additional error details.
        """
        return self._details

    def __str__(self) -> str:
        """
        Returns a string representation of the error.

        Returns:
            str: The error message as a string.
        """
        return self._format_error()
