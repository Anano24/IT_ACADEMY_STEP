from typing import Any
from django.forms import BaseModelForm
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, DetailView, CreateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Q
from .models import Blog
from .forms import BlogForm, RegistrationForm
from django.contrib.auth import logout, login
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin
from django.http.response import HttpResponse as HttpResponse, HttpResponseRedirect

# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:

        query = request.GET.get('blog_query')

        if query:
            blogs = Blog.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
        else:
            blogs = Blog.objects.all()

        return render(request, self.template_name, {'blogs': blogs})



class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog_detail.html"
    context_object_name = 'detailed_blog'



class AddBlogView(PermissionRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'add_blog.html'
    success_url = reverse_lazy('blogapp:homepage')
    permission_required = 'blogapp.add_blog'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user

        return super().form_valid(form)
    
    def handle_no_permission(self) -> HttpResponseRedirect:
        return redirect('blogapp:homepage')



class DeleteBlogView(PermissionRequiredMixin, DeleteView):
    model = Blog
    template_name = 'delete.html'
    success_url = reverse_lazy('blogapp:homepage')
    permission_required = 'blogapp.delete_blog'

    def test_func(self) -> bool | None:
        blog_post = self.get_object()
        return self.request.user == blog_post.author or self.request.user.is_superuser

    def handle_no_permission(self) -> HttpResponseRedirect:
        return redirect('blogapp:homepage')




class UserSignUpView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/sign_up.html'
    success_url = reverse_lazy('blogapp:homepage')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response



class UserLoginView(LoginView, UserPassesTestMixin):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('blogapp:homepage')

    def test_func(self) -> bool | None:
        return not self.request.user.is_authenticated
    
    def handle_no_permission(self) -> HttpResponseRedirect:
        return redirect('blogapp:homepage')
    


class UserLogoutView(LogoutView):
    def get(self, request):
        logout(request)
        return redirect('blogapp:login')
    



