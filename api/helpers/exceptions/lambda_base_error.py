class LambdaBaseError(Exception):
    def __init__(self, message):
        self.message = message
        self.return_code = "Undefined"
        self.return_text = 'Undefined'

    def getHTTPReturnCode(self):
        return self.return_code

    def getHTTPReturnText(self):
        return self.return_text

    def __str__(self):
        return f"Message: {self.message}, Return Code: {self.return_code}, Return Text: {self.return_text}"


