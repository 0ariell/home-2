from django.http import HttpResponse
from django.http import JsonResponse

def home(request):
    return HttpResponse("¡Bienvenido a Home+!")

def test_view(request):
    return JsonResponse({"message": "OK"})