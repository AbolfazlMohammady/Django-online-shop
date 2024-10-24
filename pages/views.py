from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.utils import translation
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import ContacUsForm


def home_page_viwe(request):
    return redirect(reverse('product-list'))


def about_page_view(request):

    if request.method == "POST":
        form = ContacUsForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContacUsForm()
            messages.success(request, 'پیام شما با موفقیت ثبت شد')

    else:
        form = ContacUsForm()
    
    return render(request, 'pages/about.html', context={
        'form': form
    })



class TestPageView(TemplateView):
    template_name= 'pages/test.html'


def change_language(request, lang_code):
    # تغییر زبان به زبان جدید
    translation.activate(lang_code)
    request.session[translation.LANGUAGE_SESSION_KEY] = lang_code
    # هدایت مجدد به صفحه اصلی یا هر صفحه‌ای که می‌خواهید
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('home')))