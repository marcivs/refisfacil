from django.shortcuts import render


def home(request):
    title = 'REFIS FÁCIL'
    context = {'title': title}
    template = 'home.html'
    return render(request, template, context)
