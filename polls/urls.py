from django.urls import path 
from . import views
from django.conf import settings 
from django.conf.urls.static import static 
urlpatterns = [
    # path('',views.index,name = 'index'),
    path('', views.upload, name = 'index'), 
    # path('success', success, name = 'success'), 
    # path('<int:question_id>/',views.detail,name='detail')
]
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)