from django.shortcuts import render


def index(request):
	title = "Home"
	context = {
		"title": title
	}
	return render(request, "index.html", context)
