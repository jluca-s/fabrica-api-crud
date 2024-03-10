from django.urls import include, path

from fipe import views

urlpatterns = [
    path('', views.index, name='index'),
    path('marcas/', views.allApiBrands, name='allBrands'),
    path('marcas/<str:brandCode>/modelos/', views.allApiModels, name='allModels'),
    path('apiModelsRedirect/', views.allApiModelsRedirect, name='apiModelsRedirect'),
    path('marcas/<str:brandCode>/modelos/<str:modelCode>/anos/', views.allApiYears, name='allYears'),
    path('marcas/<str:brandCode>/modelos/<str:modelCode>/anos/<str:yearCode>/', views.getApiFipe, name='getFipe'),
    path('createOrUptadeVehicle/', views.createOrUpdateVehicle, name='CreateOrUpdateVehicle'),
    path('allVehicles/', views.allVehicles, name='allVehicles'),
    path('getVehicle/<str:codeFipe>', views.getVehicle, name='getVehicle'),
    path('deleteVehicle/<str:codeFipe>', views.deleteVehicle, name='deleteVehicle'),
    path('updateVehicle/<str:codeFipe>', views.updateVehicle, name='updateVehicle'),
    path('updateVehicleForm/<str:codeFipe>', views.updateVehicleForm, name='updateVehicleForm'),
]