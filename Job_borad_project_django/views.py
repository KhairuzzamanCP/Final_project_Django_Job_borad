from django.shortcuts import render
from django.views.generic import ListView
from job_app.models import EmployeeModel
from service_app.models import ServiceModel


# class JobListView(ListView):
#     model = EmployeeModel
#     template_name = 'home.html'
#     context_object_name = 'jobs'
 
#     # def get(self, request, *args, **kwargs):
#     #     brand_slug = kwargs.get('brand_slug')
#     #     self.object_list = self.model.objects.all()
 
#     #     if brand_slug:
#     #         brand = ServiceModel.objects.get(slug=brand_slug)
#     #         self.object_list = self.object_list.filter(brand=brand)
 
#     #     context = self.get_context_data()
#     #     return self.render_to_response(context)
 
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['services'] = ServiceModel.objects.all()
#         return context
    
 
# def category(request, category_slug=None):
#     employees = EmployeeModel.objects.all()
#     services = ServiceModel.objects.all()
 
#     if category_slug is not None:
#             category = ServiceModel.objects.filter(slug=category_slug).first()
#             print(category)
#             employees = EmployeeModel.objects.filter(service=category)

 
#     return render(request, 'home.html', {'jobs': employees, 'categories': services})

def ContactUSview(request):
    return render (request,'contact.html')

def AboutUsView(request):
    return render(request,'about.html')
    

def home(request, id=None):
    jobs = EmployeeModel.objects.all()
    if id is not None:
        service= ServiceModel.objects.get(id=id)
        jobs =EmployeeModel.objects.filter(service=service)
    services = ServiceModel.objects.all()
    return render(request, 'home.html', {'jobs':jobs, 'services':services})