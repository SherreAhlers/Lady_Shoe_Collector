from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shoes/', views.shoes_index, name='index'),
    path('shoes/<int:shoe_id>/', views.shoes_detail, name='detail'),
    path('shoes/create/', views.ShoeCreate.as_view(), name='shoes_create'),
    path('shoes/<int:pk>/update/', views.ShoeUpdate.as_view(), name='shoes_update'),
    path('shoes/<int:pk>/delete/', views.ShoeDelete.as_view(), name='shoes_delete'),
    path('shoes/<int:shoe_id>/add_cleaning/', views.add_cleaning, name='add_cleaning'),
    path('shoes/<int:shoe_id>/assoc_outfit/<int:outfit_id>/', views.assoc_outfit, name='assoc_outfit'),
    path('outfits/', views.OutfitList.as_view(), name='outfits_index'),
    path('outfits/<int:pk>/', views.OutfitDetail.as_view(), name='outfits_detail'),
    path('outfits/create/', views.OutfitCreate.as_view(), name='outfits_create'),
    path('outfits/<int:pk>/update/', views.OutfitUpdate.as_view(), name='outfits_update'),
    path('outfits/<int:pk>/delete/', views.OutfitDelete.as_view(), name='outfits_delete'),
]