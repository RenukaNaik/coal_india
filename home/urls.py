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
    path('download/<int:id>',views.single,name='download'),
    path('search/',views.search,name='search'),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

