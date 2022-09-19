class InternalServerError(Exception):
    pass


class BadRequestError(Exception):
    pass


class InputError(Exception):
    pass


class UnauthorizedError(Exception):
    pass


class UnprocessableEntityError(Exception):
    pass


class NotFoundError(Exception):
    pass


errors = {
    "InternalServerError": {"message": "Something went wrong", "status": 500},
    "BadRequestError": {
        "message": "Error in JSON parsing. Please check again your input",
        "status": 400,
    },
    "InputError": {
        "message": "Somethin went wrong. Please check again your input",
        "status": 400,
    },
    "UnauthorizedError": {"message": "Access unauthorized.", "status": 401},
    "UnprocessableEntityError": {
        "message": "Cannot Process This Type of Input",
        "status": 422,
    },
    "NotFoundError": {"message": "Request not found on database", "status": 404},
}


# errors = {
#     "InternalServerError": {
#         "status": 500,
#         "data": {"error_code": "500", "error_message": "Something went wrong"},
#     },
#     "BadRequestError": {
#         "status": 400,
#         "data": {
#             "error_code": "400",
#             "error_message": "Error in JSON parsing. Please check again your input",
#         },
#     },
#     "InputError": {
#         "status": 400,
#         "data": {
#             "error_code": "400",
#             "error_message": "Somethin went wrong. Please check again your input",
#         },
#     },
#     "UnauthorizedError": {
#         "message": "UnauthorizedError",
#         "status": 401,
#         # "data": {"error_code": 401, "error_message": "Access unauthorized."},
#     },
#     "UnprocessableEntityError": {
#         "status": "UnprocessableEntityError",
#         "data": {
#             "error_code": "422",
#             "error_message": "Cannot Process This Type of Input",
#         },
#     },
#     "NotFoundError": {
#         "status": "NotFoundError",
#         "data": {"error_code": "404", "error_message": "Request not found on database"},
#     },
# }
