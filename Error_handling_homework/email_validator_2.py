class NameTooShortError(Exception):
    def __init__(self, message="Name must be more than 4 characters"):
        self.message = message
        super().__init__(message)


class MustContainAtSymbolError(Exception):
    """ Raised when the email is missing @ """
    def __init__(self, message="Email must contain @"):
        self.message = message
        super().__init__(message)


class InvalidDomainError(Exception):
    """ Raise when email has invalid domain """

    def __init__(self, message="Domain must be one of the following: .com, .bg, .org, .net"):
        self.message = message
        super().__init__(message)


def validate_name(email):
    username = email.split("@")[0]
    if len(username) <= 4:
        raise NameTooShortError()


def validate_at_symbol(email):
    if '@' not in email:
        raise MustContainAtSymbolError()


def validate_domain(email, valid_domains):
    domain = email.split(".")[-1]
    if domain not in valid_domains:
        raise InvalidDomainError()


while True:
    line = input()
    valid_domains = ("com", "net", "bg", "org")
    if line == "End":
        break

    validate_name(line)
    validate_at_symbol(line)
    validate_domain(line, valid_domains)

    print("Email is valid")