from django.urls import path, include

app_name = 'reserve'
urlpatterns = [
    path('reserve/', include('reserve.api.router')),
]
