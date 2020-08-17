from django.shortcuts import render, HttpResponseRedirect, reverse

from homepage.models import Text_line
from homepage.forms import TextForm

# Create your views here.


def index(request):
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_text = Text_line.objects.create(
                user_text=data.get('user_text')
            )
    form = TextForm()
    return render(request, "index.html", {"text_form": form})
