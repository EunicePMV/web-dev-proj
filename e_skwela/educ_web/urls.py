from django.urls import path

from . import views 

urlpatterns = [
    
    path("submission", views.submission , name="submission"),
    path("mark", views.mark, name="mark"), # for the instructors' marks page
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("calendar", views.calendar, name="calendar"),

    path("course_instruct", views.instruct_stream, name="instruct_stream"),
    path("people", views.instruct_people, name="instruct_people"),
    path("classwork", views.instruct_classwork, name="instruct_classwork"),

    path("indiv_file_comment", views.indiv_file_comment, name="indiv_file_comment"),

    path("home", views.home, name="home"),
    path("todo", views.todo, name="todo"),
    path("todo/missing", views.todo_missing, name="todo_missing"),
    path("todo/done", views.todo_done, name="todo_done"),
    path("course", views.student_stream, name="student_stream"),
    path("course/classwork", views.student_classwork, name="student_classwork"),
    path("course/people", views.student_people, name="student_people"),

    # footer web pages
    path("about", views.about, name="about"),
    path("goals", views.goals, name="goals"),
    path("mission", views.mission, name="mission"),
    path("vision", views.vision, name="vision"),
    
]

# path("course", views.course , name=""),
# path("classwork", views.classwork , name=""),
# path("mark", views.mark , name="mark"),
# path("hwTab", views.hwTab , name="hwTab"),
# path("studFile", views.studFile , name="studFile"),



# login
# register 
# home
# calendar 
# todo 
# indiv course 
# submission

# instrcutor:
# index
# classwork
# people
# mark
# assignment tab when mark's page is click
# submitted file is click in assignment tab