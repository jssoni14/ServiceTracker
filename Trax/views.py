from django.shortcuts import render
from django.views import View
from Trax.models import User, Car, Service

from django.http import JsonResponse


class Add_Driver(View):
    def get(self, request):
        return render(request, "main/add_driver.html")

    def post(self, request):
        add_new_driver = User()
        add_new_driver.name = request.POST.get("name")
        add_new_driver.save()
        return render(request, "main/add_driver_successful.html")


class Add_Car(View):
    def get(self, request):
        the_driver = User.objects.only("name")
        context = {'driver': the_driver}
        return render(request, "main/add_car.html", context)

    def post(self, request):
        get_driver = request.POST.get("add_car_to_driver")
        add_new_car = Car()
        add_new_car.make = request.POST.get("make")
        add_new_car.model = request.POST.get("model")
        add_new_car.year = request.POST.get("year")
        add_new_car.mileage = request.POST.get("mileage")
        add_new_car.name = User.objects.get(name=get_driver)
        add_new_car.save()
        return render(request, "main/add_car_successful.html")


class Add_Service(View):
    def get(self, request):
        the_car = Car.objects.only("model")
        context = {'car': the_car}
        return render(request, "main/add_service.html", context)

    def post(self, request):
        the_car = request.POST.get("add_service_to_car")
        add_new_service = Service()

        add_new_service.location = request.POST.get("location")
        add_new_service.price = request.POST.get("price")
        add_new_service.service = request.POST.get("service")

        add_new_service.date = request.POST.get("date")
        add_new_service.car = the_car
        add_new_service.mileage = request.POST.get("mileage");
        add_new_service.save()
        return render(request, "main/add_service_successful.html")


class View_Driver(View):
    def get(self, request):
        all_driver = User.objects.all()
        context = {'driver': all_driver}
        return render(request, "main/view_driver.html", context)


class View_Car(View):
    def get(self, request):
        all_driver = User.objects.all()
        context = {'driver': all_driver}
        return render(request, "main/view_car.html", context)

    def post(self, request):
        find_driver = request.POST.get("view_car_by_driver")

        car_return = Car.objects.filter(name__name=find_driver)
        context = {'my_car': car_return}

        return render(request, 'main/view_car.html', context)


class View_Service(View):
    def get(self, request):
        all_car = Car.objects.all()
        context = {'cars': all_car}
        return render(request, "main/view_service.html", context)

    def post(self, request):
        service = list(Service.objects.filter(car=request.POST.get("view_service_by_car")).values())
        the_service = list(Service.objects.all().values())
        return JsonResponse(the_service, safe=False)





class Manufacture(View):
    def get(self, request):
        return render(request, "main/manufacture.html")
class Main(View):
    def get(self, request):
        return render(request, "main/main.html")
# Create your views here.
