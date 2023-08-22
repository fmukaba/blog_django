from django.urls import path
from . import views
# from django.conf.urls import url, include,

urlpatterns = [
    path('', views.home),
    path('add', views.add),
    path('show/<int:id>', views.show),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('<path:path>', views.not_found)
]
