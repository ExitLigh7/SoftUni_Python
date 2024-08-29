from django.urls import path

from demo_templates.ts_demo.views import index, redirect_to_home, show_about

urlpatterns = [
    path('', index, name='index'),
    path('go-to-home/', redirect_to_home, name='redirect to home'),
    path('about/', show_about, name='about'),
]
