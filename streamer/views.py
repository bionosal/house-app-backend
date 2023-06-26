from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import Streamer
from .serializers import StreamerSerializer
from django.core.handlers.wsgi import WSGIRequest as Request


@api_view(['GET', 'POST'])
def streamer_list(request: Request):
    if request.method == 'GET':
        streamers = Streamer.objects.all()
        serializer = StreamerSerializer(streamers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StreamerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', "DELETE"])
def streamer_details(request: Request, pk: int):
    try:
        streamer = Streamer.objects.get(pk=pk)
    except Streamer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StreamerSerializer(streamer)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StreamerSerializer(streamer, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        streamer.delete()
        return HttpResponse(status=204)
