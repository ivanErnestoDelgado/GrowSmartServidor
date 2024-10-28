from django.http import JsonResponse

def root_view(request):
    return JsonResponse({"message": "Bienvenido a la API de GrowSmart"})