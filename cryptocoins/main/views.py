from django.shortcuts import render
from django.views import View


class MainPageView(View):
    def get(self, request):
        data = {

        }

        return render(request, 'main/mainpage.html', data)
