from django.http import JsonResponse


def say_hello(request):
    return JsonResponse({'hello': 'Cześć tu ja serwer :)'})
