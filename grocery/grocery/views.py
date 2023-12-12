from django.shortcuts import render

def project_template(request):
    return render(request, 'project_template.html')