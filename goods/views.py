from django.shortcuts import render

def catalog(request):
    context = {
        
    }
    return render(request, "goods/catalog.html", context)
