from django.shortcuts import render

def index(request):
    language_list = [
        "HTML",
        "CSS",
        "JavaScript",
        "Python",
        "Java",
        "C",
        "PHP",
        "R",
        "Swift",
        "Kotlin",
    ]

    context = {
        "language_list":language_list,
    }
    return render(request,"forum/index.html",context)

def forum(request, topic):
   pass
   
# Create your views here.
