from django.shortcuts import render

def home(request):
    articles = [
        {
        'title': 'Blog Article 1',
        'date_posted': 'September 11, 2024'
        },

        {
        'title': 'Blog Article 2',
        'date_posted': 'September 5, 2024'
        }   
    ]
    return render(request, 'blog/home.html', {'articles': articles})