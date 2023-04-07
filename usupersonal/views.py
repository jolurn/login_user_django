from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import CustomUser
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm,CustomUserCreationForm,CustomUserForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import redirect
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

class CustomUserListView(ListView):
    model = CustomUser
    template_name = 'customuser_list.html'
    context_object_name = 'usuarios'

class CustomUserCreateView(CreateView):
    model = CustomUser
    template_name = 'customuser_form.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('customuser_list')

    def form_valid(self, form):
        form.instance.username = form.cleaned_data['email']
        return super().form_valid(form)

class CustomUserUpdateView(UpdateView):
    model = CustomUser
    template_name = 'customuser_form.html'
    form_class = CustomUserForm
    success_url = reverse_lazy('customuser_list')

class CustomUserDeleteView(DeleteView):
    model = CustomUser
    template_name = 'customuser_confirm_delete.html'
    success_url = reverse_lazy('customuser_list')

class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = CustomAuthenticationForm
    success_url = '/'

class CustomPasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('customuser_list')
    template_name = 'change_password.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        logout(self.request)
        return response
    
def signout(request):
    logout(request)
    return redirect('home')