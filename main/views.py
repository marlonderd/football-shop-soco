from django.shortcuts import render

def show_main(request):
    context = {
        'app_name' : 'SoCo',
        'name': 'Marlond Leanderd Batara',
        'npm': '2406496201',
        'class' : 'PBP E'
    }
    return render(request, "main.html", context)
# Create your views here.
