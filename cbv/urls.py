from django.urls import path

from cbv import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='cbv_index'),
    path('2/', views.IndexTemplateView.as_view(), name='cbv_index 2'),
    path('3/', views.TemplateView.as_view(template_name='cbv/index.html'), name='cbv_index 3'),
    path('list/', views.PetForExampleListView.as_view(), name='cbv_index list'),
    path('details/<int:pk>', views.PetForExampleDetailsView.as_view(), name='cbv_index_details'),
    path('create/', views.PetForExampleCreateView.as_view(), name='cbv_index_create'),
]