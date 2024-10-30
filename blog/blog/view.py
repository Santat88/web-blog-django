from django.http import HttpResponse

def helloPage(request):
    return HttpResponse("<h1>Hello page</h1>")