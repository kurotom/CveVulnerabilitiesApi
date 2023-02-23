from django.urls import path
from .views import (
    ApiGetByNameView,
    SearchCveIdApiView,
    ByDateCvesView,
)


urlpatterns = [
    path("query", ApiGetByNameView.as_view(), name="query"),
    path("cveid", SearchCveIdApiView.as_view(), name="cveid"),
    path("date", ByDateCvesView.as_view(), name="date"),

]
