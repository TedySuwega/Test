from flask_restful import reqparse


def non_empty_string(s):
    """
    Checking whether or not the value of request key is an
    empty string or check if value only int type.
    """
    if not s:
        raise ValueError("Must not be empty string")
    return True


def non_integer(i):
    """
    Checking whether or not the value of request key is only int type.
    """
    if type(i) == int:
        raise ValueError("Must unique combine string and integer")
    return True


def user_id_type(u):
    """
    Cheking request suitablility
    """
    if (non_empty_string(u) and non_integer(u)) is False:
        raise ValueError("Something wrong with input data")
    return u


class Validators:
    """
    This class is used for validating the request that came to our endpoints.
    """

    def __init__(self):
        """
        The class constructor. Set up the validator here.
        """
        self._set_headers_validators()
        self._set_message_validators()

    def _set_headers_validators(self) -> None:
        """
        Set validators for headers found in requests.
        """
        self.headers_parser = reqparse.RequestParser(bundle_errors=True)
        self.headers_parser.add_argument(
            "Content-Type", required=True, nullable=False, location="headers",
        )
        self.headers_parser.add_argument(
            "Auth-Unique-Token", required=True, nullable=False, location="headers",
        )

    def _set_message_validators(self) -> None:
        """
        Set validators for messages found in requests.
        """
        self.root_parser = reqparse.RequestParser(bundle_errors=True)
        self.root_parser.add_argument("data", type=dict, nullable=False, required=True)

    def get_validators(self) -> dict:
        """
        Get message validators as dict so all of the parser can be accomodated
        in one go.
        """
        req_val = dict()
        req_val["root"] = self.root_parser
        req_val["headers"] = self.headers_parser

        return req_val

    def get_validators_related(self) -> dict:
        """
        Get message validators as dict so all of the parser can be accomodated
        in one go.
        """
        req_val = dict()
        req_val["root"] = self.root_parser
        req_val["headers"] = self.headers_parser

        return req_val
