from django.http import HttpResponse,JsonResponse
from .models import Student


def index(request):
    students=Student.objects.all()
    print(students)
    students =list(students.values())
    return JsonResponse(students,safe=False)