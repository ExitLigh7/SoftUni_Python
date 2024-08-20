from django.urls import path
from django101.tasks.views import bare_minimum_view, show_all_tasks, index

urlpatterns = [
    path('', index),
    path('it-works', bare_minimum_view),
    path('all/', show_all_tasks)
]
