from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    "december": "Become the best",
}

# Create your views here.


def home(request):
    months = ""
    required_month = None

    for key in monthly_challenges.keys():
        required_month = key
        month_path = reverse("month-challenge", args=[required_month])
        months += f"<a href={month_path}><h1><li>{key.capitalize()}</li></h1>"

    response_data = f"""
    <ul>{months}</ul>
    """

    return HttpResponse(response_data)


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
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
