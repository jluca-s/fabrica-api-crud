from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
import requests

from fipe.models import Vehicle

def index(request):
    return render(request, 'index.html')

def allApiBrands(request):
    
    urlFipeApi = 'https://parallelum.com.br/fipe/api/v1/carros/marcas/'
    
    response = requests.get(urlFipeApi)
    brands = response.json()
    
    
    #fazer tratamento
    allBrands = []
    for brand in brands:
        
        brandName = brand.get("nome", '')        
        brandID = brand.get("codigo", '')
        
        allBrands.append({'nome': brandName, 'codigo': brandID})
    
    
    return render(request, 'allApiBrands.html', {'allBrands': allBrands})

def allApiModels(request, brandCode):
    
    urlFipeApi = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{brandCode}/modelos/'
    
    response = requests.get(urlFipeApi)
    modelsJson = response.json()
    
    models = modelsJson.get("modelos", [])    
    
    allModels = []
    for model in models:
        
        modelName = model.get("nome", '')
        modelID = model.get("codigo", '')
        
        allModels.append({'nome': modelName, 'codigo': modelID})
        
    return render(request, 'allApiModels.html', {'allModels': allModels, 'brandCode': brandCode, 'modelCode': modelID})

def allApiModelsRedirect(request):
    brandCode = request.GET.get('brandCode')
    
    return redirect('allModels', brandCode=brandCode)
    
def allApiYears(request, brandCode, modelCode):
    
    urlFipeApi = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{brandCode}/modelos/{modelCode}/anos/'
    
    response = requests.get(urlFipeApi)
    yearsJson = response.json()
    
    allYears = []
    for year in yearsJson:
        
        yearName = year.get("nome", '')
        yearCode = year.get("codigo", '')

        allYears.append({'nome': yearName, 'codigo': yearCode})
    
    
    return  render(request, 'allApiYears.html', {'allYears': allYears, 'brandCode': brandCode, 'modelCode': modelCode})

def getApiFipe(request, brandCode, modelCode, yearCode):
    
    urlFipeApi = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{brandCode}/modelos/{modelCode}/anos/{yearCode}'
    
    response = requests.get(urlFipeApi)
    fipeData = response.json()
        
    return render(request, 'fipeApiInfo.html', {'fipeData': fipeData})

def createOrUpdateVehicle(request):
    
    vehicle = {
        'price': request.POST.get('price'),
        'brand': request.POST.get('brand'),
        'model': request.POST.get('model'),
        'modelYear': request.POST.get('modelYear'),
        'fuel': request.POST.get('fuel'),
        'codeFipe': request.POST.get('codeFipe'),
        'vehicleType': request.POST.get('vehicleType'),
        'fuelType': request.POST.get('fuelType'),
    }
    
    Vehicle.objects.update_or_create(
        codeFipe = vehicle['codeFipe'],
        defaults = vehicle
    )
        
    return redirect('allVehicles')

def allVehicles(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'allVehicles.html', {'vehicles': vehicles})

def getVehicle(request, codeFipe):
    vehicle = get_object_or_404(Vehicle, codeFipe=codeFipe)
    return render(request, 'getVehicle.html', {'vehicle': vehicle})

def deleteVehicle(request, codeFipe):
    vehicle = get_object_or_404(Vehicle, codeFipe=codeFipe)
    vehicle.delete()
    return redirect('allVehicles')

def updateVehicle(request, codeFipe):
    vehicle = get_object_or_404(Vehicle, codeFipe=codeFipe)
    
    vehicle.price = request.POST.get('price', '')
    vehicle.brand = request.POST.get('brand', '')
    vehicle.model = request.POST.get('model', '')
    vehicle.modelYear = request.POST.get('modelYear', '')
    vehicle.fuel = request.POST.get('fuel', '')
    vehicle.vehicleType = request.POST.get('vehicleType', '')
    vehicle.fuelType = request.POST.get('fuelType', '')
    vehicle.save()
    
    return redirect('getVehicle', codeFipe=codeFipe)

def updateVehicleForm(request, codeFipe):
    vehicle = get_object_or_404(Vehicle, codeFipe=codeFipe)
    return render(request, 'updateVehicleForm.html', {'vehicle': vehicle})