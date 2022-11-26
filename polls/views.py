from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    question_list = [
        "プログラミングは好きですか？",
        "数学は好きですか？",
        "国語は好きですか？",
    ]
    context = {
        "question_list": question_list,  # list 型を渡す
        "is_polled": False,
        "polled_msg": "投票ありがとうございました。",
        "not_polled_msg": "投票をお願いします。",
    }
    return render(request, "polls/index.html", context)
