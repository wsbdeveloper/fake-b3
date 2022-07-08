from rest_framework.exceptions import APIException

class TransactionExceptionServer(APIException):
    status_code = 500
    default_detail = 'Service with unavailable, try again later.'
    default_code = 'service_unavailable'


class TransactionExceptionServer(APIException):
    status_code = 404
    default_detail = 'Not Found!'
    default_code = 'not_found'
