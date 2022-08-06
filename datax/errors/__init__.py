# pylint: disable=super-init-not-called
class DataxException(Exception):
    def __init__(self, message=None, status_code=500):
        self.status_code = status_code
        self.message = message if message else "Datax Error"

    def get_status_code(self):
        return self.status_code

    def to_dict(self):
        dto = {"status_code": self.status_code, "message": self.message}
        return dto


class InvalidConfigurationError(DataxException):
    def __init__(self, message=None):
        self.status_code = 400
        self.message = message if message else "Datax: Invalid configuration provided"

class InvalidSourceFileError(DataxException):
    def __init__(self, message=None):
        self.status_code = 400
        self.message = message if message else "Datax: Invalid source file provided"
