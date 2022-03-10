from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello,World")

def HelloPl(request):
    return HttpResponse("Cześć!")



def HelloView(request):
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    html = "Cześć"
    return HttpResponse(html)