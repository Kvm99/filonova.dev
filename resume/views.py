from django.shortcuts import render

def show_main_page(request):
    return render(request, 'resume/index.html', {})


def show_resume(request):
    return render(request, 'resume/srt-resume.html', {})


def show_certificates(request):
    return render(request, 'resume/certificates.html', {})
