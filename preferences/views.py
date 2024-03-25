from django.shortcuts import render
from django.views import View

# Create your views here.
class PreferencesView(View):
  def index(request):
      return render(request, 'preferences/index.html')
