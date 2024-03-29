from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView
from job_app.models import EmployeeModel,Job_seeker
from job_app.forms import CarModelForm,jobsekeerFrom
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.


class AddJobCreateView(CreateView):
    model = EmployeeModel
    form_class = CarModelForm
    template_name = 'add_job.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["type"] = "Add"
        return context
    
    def form_invalid(self, form):
        messages.error(self.request, 'Something went wrong. your job not added in the list.')
        return super().form_invalid(form)
    
    def form_valid(self, form):
        messages.success(self.request, 'Job added successful')
        return super().form_valid(form)
    
class JobDetailsView(DetailView):
    model = EmployeeModel
    template_name = 'job_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        job = self.object
        if self.request.user.is_authenticated:
            employee_id = job.id  
            context['user_has_applied'] = Job_seeker.objects.filter(user=self.request.user, employee=employee_id).exists()
        else:
             context['user_has_applied'] = False
        context['service'] = job 
        return context
        

    
class JobSeekerCreateView(CreateView):
    model = Job_seeker
    form_class = jobsekeerFrom
    template_name = 'job.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        job_seeker = form.save(commit=False)
        job_seeker.user = self.request.user
        job_seeker.save()
        subject = 'Thanks for applying'
        message = f'Hi {self.request.user.first_name} {self.request.user.last_name}, You have applied successfully'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [self.request.user.email, ]
        send_mail( subject, message, email_from, recipient_list )
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)