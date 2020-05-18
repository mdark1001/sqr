from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

app_name = 'survey'

urlpatterns = [
                  path('', views.index, name="index"),
                  path('<int:survey_id>/', views.detail, name='detail'),
                  path('<int:survey_id>/edit', views.edit, name='edit'),
                  path('<int:survey_id>/result', views.result, name='result'),
                  path('<int:survey_id>/vote/', views.vote, name='vote'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
