from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.coalIndia, name='viewVatikas'),
    path('coal/',views.coal, name='coal'),
    # path('edit/<int:id>', views.edit, name='edit'),
    path('edit/',views.edit,name='edit'),
    path('export/',views.export,name='export'),
    path('download/<str:project_name>',views.single,name='download'),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

