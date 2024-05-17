from django.http import HttpResponse,HttpRequest,HttpResponseRedirect


def sayhello(request):
    return HttpResponse("Hello to Django")


def say_hello_with_name(request: HttpRequest,name):
    print(request.headers)
    return HttpResponse("Hello to Django %s" % name)