from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q

from account_engine.models import Property,City,Contact,Amenities
# Create your views here.

# def index(request):
#     cities = City.objects.all()
#     property = Property.objects.filter(property_type='R')
#     commercial = Property.objects.filter(property_type='C')

#     if request.method == 'POST':
#         location = request.POST.get('location')
#         print(location)
#         try:
#             city = City.objects.get(id=request.POST.get('city'), location=location)
#         except:
#             return HttpResponse("No data found!!")
#         if not city == None:
#             return redirect(get_search, city.id)

#     return render(request, 'index.html',{
#         'cities': cities,
#         'property':property,
#         'commercial':commercial
        
        
#     })

def index(request):
    cities = City.objects.all()
    properties = Property.objects.filter(property_type='R')
    commercial = Property.objects.filter(property_type='C')

    if request.method == 'POST':
        location = request.POST.get('location')
        city_id = request.POST.get('city')

        if not city_id == None:
            return redirect('properties', city_id, location)

    return render(request, 'index.html',{
        'cities': cities,
        'properties': properties,
        'commercial': commercial,
        
    })



def get_search(request, city_id, location=None):
    cities = City.objects.all()
    properties = Property.objects.all()

    city = City.objects.get(id=city_id)


    # Filter the properties queryset based on the city and location
    properties = Property.objects.filter(city=city).filter(Q(location__icontains=location) | Q(location__isnull=True))
    
    return render(request, 'properties.html',{
        'city_id':city_id,
       'cities':cities,
       'properties':properties,

    })



def residential(request,):
    property = Property.objects.filter(property_type='R')
   
    return render(request, 'residential.html',{
       'property':property,
       
    })


def residential_Single_Listing(request,slug):
    property = Property.objects.get(slug=slug)
    amenities = Amenities.objects.all()



    if 'contact' in request.POST :
        name = request.POST.get('name')
        print(name)
        email = request.POST.get('email')
        print(email)
        mobile_number = request.POST.get('mobile_number')
        print(mobile_number)
        city = request.POST.get('city')
        print(city)
        contact = Contact.objects.create(name=name, email=email, mobile_number=mobile_number, city=city)

    return render(request, 'residential-Single-Listing.html',{
        'property': property,
        'amenities'  : amenities
    })


def commercial(request):
    property = Property.objects.filter(property_type='C')

    return render(request, 'commercial.html',{
        'property': property,
    })


def commercial_Single_Listing(request,slug):
    property = Property.objects.get(slug=slug)

    return render(request, 'commercial-Single-Listing.html',{
        'property':property
    })


def contact(request):
    if request.method == 'POST':
        if 'write_to_us' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            mobile_number = request.POST.get('mobile_number')
            message = request.POST.get('message')
            contact = Contact.objects.create(name=name, email=email, mobile_number=mobile_number, message=message)



    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def copyright_policy(request):
    return render(request, 'footer_pages/copyright_policy.html')

def privacy_policy(request):
    return render(request, 'footer_pages/privacy_policy.html')

def terms_and_conditions(request):
    return render(request, 'footer_pages/terms_and_conditions.html')

def career(request):
    return render(request, 'footer_pages/career.html')

def properties(request, city_id=None, location=None):
    cities = City.objects.all()
    
    try:
        city = City.objects.get(id=city_id)
        # Filter the properties queryset based on the city and location
        properties = Property.objects.filter(city=city).filter(Q(location__icontains=location) | Q(location__isnull=True))
        print()
        print()
        print(properties)
    except:
        properties = Property.objects.all()

    return render(request, 'properties.html',{
        'city_id':city_id,
        'cities':cities,
        'properties':properties,
    })






