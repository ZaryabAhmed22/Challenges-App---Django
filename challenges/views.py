from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render

monthly_challenges = {
    "january": "Stop your shitty plans",
    "february": "Take your ass to gym",
    "march": "Learn something new",
    "april": "Complete Django course",
    "may": "Larn something related to FYP",
    "june": "No fap month",
    "july": "Start reading a book",
    "august": "Start freelancing",
    "september": "Work on networking",
    "october": "Complete pending tution classes",
    "november": "Complete pending course",
    "december": None,
}

# Create your views here.


def home(request):
    months = monthly_challenges.keys()
    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month-1]

    # this is not hardcoded
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
    # this is hard coded
    # return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):

    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month": month,
            "text": challenge_text
        })

    except:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        raise Http404()
