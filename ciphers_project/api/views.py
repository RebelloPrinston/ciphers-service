from django.http import JsonResponse

# Create your views here.
def greetings(request):
    request = {"message":"Welcome to ciphers service!"}
    return JsonResponse(request)
