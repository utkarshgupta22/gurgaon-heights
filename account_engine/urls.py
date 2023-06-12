from django.urls import path
from account_engine import views


urlpatterns = [
    path('', views.index, name='index'),
    path('residential/', views.residential, name='residential'),
    path('residential-Single-Listing/<slug:slug>/', views.residential_Single_Listing, name='residential_Single_Listing'),
    path('commercial/', views.commercial, name='commercial'),
    path('commercial-Single-Listing/<slug:slug>/', views.commercial_Single_Listing, name='commercial_Single_Listing'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('residential-Single-Listing/<slug:slug>/', views.residential_Single_Listing, name='residential_Single_Listing'),
    path('commercial-Single-Listing/<slug:slug>/', views.commercial_Single_Listing, name='commercial_Single_Listing'),
    path('copyright_policy/', views.copyright_policy, name='copyright_policy'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('terms_and_conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('career/', views.career, name='career'),
    # path('properties/', views.properties, name='properties'),
    path('properties/<int:city_id>/<str:location>/', views.properties, name='properties'),
]