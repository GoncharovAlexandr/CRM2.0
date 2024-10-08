from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create_task/', views.create_task, name='create_task'),
    path('history/', views.history, name='history'),
    path('get_task/<int:task_id>/', views.get_task, name='get_task'),
    path('update_status/<int:task_id>/', views.update_status, name='update_status'),
    path('sort_by_responsible/', views.sort_by_responsible, name='sort_by_responsible'),
    path('get_task_events/', views.get_task_events, name='get_task_events'),
    path('get_employee_data/', views.get_employee_data, name='get_employee_data'),
    path('download_task_file/<str:file_name>/', views.download_task_file, name='download_file'),
    path('download_report_file/<str:file_name>/', views.download_report_file, name='download_file'),
    path('upload_report_file/<int:task_id>/', views.upload_report_file, name='upload_report_file'),
    path('update_report_text/<int:task_id>/', views.update_report_text, name='upload_report_text'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),  # Для отдельного представления

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)