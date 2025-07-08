from django.shortcuts import render
from django.http import JsonResponse
from .phishing_checker import predict_url_legitimacy

def check_url(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        url = request.POST.get('url')
        is_phishing = predict_url_legitimacy(url)  # Implement phishing detection logic
        return JsonResponse(is_phishing)
    return JsonResponse({'error': 'Invalid request'})



def index(request):
    # is_phishing = predict_url_legitimacy('https://www.kaggle.com/')
    is_phishing = 1
    return render(request, 'index.html', {'result': is_phishing})