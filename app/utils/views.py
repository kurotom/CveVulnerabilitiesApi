from django.http import JsonResponse


def error_404(request, exception):
    message = "Resource not found."
    return JsonResponse(data={'message': message}, status=404)


def error_500(exception):
    message = "D\'oh, something was wrong."
    return JsonResponse(data={'error': message}, status=404)
