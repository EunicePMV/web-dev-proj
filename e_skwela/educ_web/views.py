from django.shortcuts import render

def home(request):
    return render(request, 'S_home/S_home.html')

def submission(request):
    return render(request, 'S_submission/S_submission.html')

def mark(request):
    return render(request, 'I_mark/I-marks-page.html')

def login(request):
    return render(request, 'login/login.html')

def register(request):
    return render(request, 'register/register.html')

def calendar(request):
    return render(request, 'S_calendar/S_calendar.html')

def instruct_stream(request):
    return render( request, 'I_home/I_home.html')

def instruct_people(request):
    return render(request, 'I_people/I_people.html')

def instruct_classwork(request):
    return render(request, 'I_classwork/I_classwork.html')

def indiv_file_comment(request):
    return render(request, 'I_indiv_file/I_indiv_file_comment.html')

def about(request):
    return render(request, 'footer-pages/about.html')

def goals(request):
    return render(request, 'footer-pages/goals.html')

def mission(request):
    return render(request, 'footer-pages/mission.html')

def vision(request):
    return render(request, 'footer-pages/vision.html')

def todo(request):
    return render(request, 'S_todo/S_todo.html')

def todo_missing(request):
    return render(request, 'S_todo/S_todo_missing.html')

def todo_done(request):
    return render(request, 'S_todo/S_todo_done.html')

def student_stream(request):
    return render(request, 'S_course/S_course_student-stream.html')

def student_classwork(request):
    return render(request, 'S_course/S_course_classwork.html')

def student_people(request):
    return render(request, 'S_course/S_course_people.html')

# favicon (ok)
# footer web pages - about us, goal, mission, vision (ok)
# marks web page (ok)
# navbar (ok)