from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Course
# Create your views here.

def index(req):
    courses=Course.objects.all()
    return render(req,'courses/index.html',{"courses":courses})


def detail(req,course_id):
    course_detail=get_object_or_404(Course,pk=course_id)
    return render(req,'courses/detail.html',{"course":course_detail})
