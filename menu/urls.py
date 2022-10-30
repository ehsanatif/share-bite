from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from menu import views

urlpatterns = [
    path('section-list-create/', views.SectionList.as_view(), name='section-list-create'),
    path('section-detail/<int:pk>/', views.SectionDetail.as_view(), name='section-detail'),
    path('modifier-list-create/', views.ModifierList.as_view(), name='modifier-list-create'),
    path('modifier-detail/<int:pk>/', views.ModifierDetail.as_view(), name='modifier-detail'),
    path('item-list-create/', views.ItemList.as_view(), name='item-list-create'),
    path('item-detail/<int:pk>/', views.ItemDetail.as_view(), name='item-detail'),
    path('menu/', views.MenutList.as_view(), name='menu'),
    path('map-item/', views.MapItems.as_view(), name='map-item'),

]

# urlpatterns = format_suffix_patterns(urlpatterns)
