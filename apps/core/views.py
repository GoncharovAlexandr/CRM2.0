from django.http import HttpRequest, JsonResponse

def main(request: HttpRequest) -> JsonResponse:
    return JsonResponse(data={
        'error':False,
        'status': "put in address /admin and connect with your account",
        'details':None

    }, status=200)