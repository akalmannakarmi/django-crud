from django.urls import path
from . import views

app_name = "crud"

urlpatterns = [
	path("createInfo",views.CreateInfo.as_view(),name="createInfo"),
	path("infos",views.Infos.as_view(),name="infos"),
	path("info/<int:pk>",views.Info.as_view(),name="info"),
	path("editInfo/<int:pk>",views.EditInfo.as_view(),name="editInfo"),
	path("deleteInfo/<int:pk>",views.DeleteInfo.as_view(),name="deleteInfo"),
]