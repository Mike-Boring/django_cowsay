from django.shortcuts import render, HttpResponseRedirect, reverse

from homepage.models import Text_line
from homepage.forms import TextForm
import subprocess

# Create your views here.


def index(request):
    user_text = None
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user_text = data.get('Text')
            new_text = Text_line.objects.create(
                Text=data.get('Text')
            )
        # used for reference:: https://queirozf.com/entries/python-3-subprocess-examples#run-example-store-output-and-error-message-in-string
        if user_text:
            cowsay_process = subprocess.run(
                ["cowsay", user_text], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            form = TextForm()
            return render(request, "index.html", {"form": form, "cowsay_process": cowsay_process.stdout})
    form = TextForm()
    return render(request, "index.html", {"form": form})


def history_view(request):
    history_list = []
    for line in Text_line.objects.all():
        history_list.append(line)
    history_list = history_list[::-1][:10]
    return render(request, "history.html", {"history_list": history_list})
