from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice


# Create your views here.


def index(request):
    return render(request, "index.html", {
        "qlist" : Question.objects.order_by("-date")
    })


def detail(request, question_id):
    return render(request, "detail.html", {
        "question": get_object_or_404(Question, pk=question_id)
    })


def results(request, question_id):
    return HttpResponse("Result of question: %s" % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "detail.html", {
            "question": question,
            "message": "ERROR"
        })
    else:
        choice.count += 1
        choice.save()
        return HttpResponseRedirect(redirect_to="/%s/" % question.id)

