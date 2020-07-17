from django.shortcuts import render

# Create your views here.
def home(request):
    context={
        'hello':'Hello from Django'
    }
    return render(request,'core/index.html',context)

def error_404(request, exception):
    return render(request, 'error_404.html', status='404')

def error_500(request):
    return render(request, 'error_500.html', status='500')