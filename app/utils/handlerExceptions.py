from rest_framework.views import exception_handler

from datetime import datetime
from django.http import Http404


from rest_framework import exceptions, status

from rest_framework.response import Response
from django.http import JsonResponse




def custom_exception_handler(exc, context):

    print("............ USANDO HANDLER")

    print()
    print(isinstance(context))
    print()

    response = exception_handler(exc, context)

    print(response is None, response is not None)

    if response is not None:
        if response.status == status.HTTP_404_NOT_FOUND:
            print("--->")
            print(response.data)
            return JsonResponse({"error": "NO ENCONTRADO....."}, status=404)
        if response.status == status.HTTP_500_INTERNAL_SERVER_ERROR:
            print("--->")
            print(response.data)
            return JsonResponse({"error": " error INTERNo"}, status=404)
    return response

#
#     handlers = {
#         'Http404': handle_generic_error,
#         'Http500': handle_generic_error
#     }
#
#     response = exception_handler(exc, context)
#
#     exception_class = exc.__class__.__name__
#
#     if response is not None:
#         import pdb
#         pdb.set_trace()
#
#         response.data['status_code'] = response.status_code
#         response.data['time'] = datetime.now()
#         response.data['detail'] = ""
#
#     return response
#
#     if exception_class in handlers:
#         return handlers[exception_class](exec, context, response)
#     return response
#
#
# def handle_generic_error(exec, context, response):
#     return response
