from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CodeForm
import requests

from .utils import save_device_id


def submit_code(request):
    if request.method == "POST":
        form = CodeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            try:
                headers = {"Content-Type": "application/json"}
                response = requests.post(
                    "http://127.0.0.1:5000/authorize_device",
                    json={"code": text},
                    headers=headers,
                )

                if response.status_code == 200:
                    data = response.json()
                    save_device_id(data["device_id"])
                    messages.success(request, data.get("message"))
                else:
                    messages.error(request, "Invalid code. Try again?")
            except requests.RequestException as e:
                messages.error(request, f"Request failed: {e}")

            return redirect("submit_code")

    else:
        form = CodeForm()

    return render(request, "raspberryauth/submit_code.html", {"form": form})
