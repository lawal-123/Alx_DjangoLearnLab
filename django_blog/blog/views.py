# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm # Used for profile editing
from django.contrib import messages
from .forms import BlogUserCreationForm # Our custom form

# ----------------- Registration View -----------------
"CommentCreateView", "CommentUpdateView", "CommentDeleteView
def register(request):
    if request.method == 'POST':
        form = BlogUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optional: Log the user in immediately after registration
            # from django.contrib.auth import login
            # login(request, user)
            messages.success(request, f'Account created for {user.username}! You can now log in.')
            return redirect('login') # Redirect to the login page
    else:
        form = BlogUserCreationForm()
        
    return render(request, 'blog/register.html', {'form': form})

# ----------------- Profile Management View -----------------

# The @login_required decorator ensures only logged-in users can access this page
@login_required
def profile(request):
    # UserChangeForm allows viewing/editing the built-in User model fields
    if request.method == 'POST':
        # Pass the current user instance to the form for modification
        form = UserChangeForm(request.POST, instance=request.user) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile') # Redirect to refresh the profile page
    else:
        form = UserChangeForm(instance=request.user)
        
    return render(request, 'blog/profile.html', {'form': form})
# blog/views.py (Replace existing content or add these classes)
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserChangeForm # Assuming you still use this for the profile view
from .models import Post
from .forms import PostForm, BlogUserCreationForm # Assuming you keep your custom forms

# --- READ Operations ---
# Accessible to all users
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-published_date'] # Order posts from newest to oldest

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# --- CREATE Operation ---
# Requires login
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog-home') # Redirect to home on success

    # Override form_valid to inject the author before saving
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# --- UPDATE Operation ---
# Requires login AND user must be the post author
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog-home')

    # Override form_valid to ensure the author remains the current user (although it shouldn't change)
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # test_func is required by UserPassesTestMixin to check permissions
    def test_func(self):
        post = self.get_object()
        # Returns True if the current user is the author of the post
        return self.request.user == post.author

# --- DELETE Operation ---
# Requires login AND user must be the post author
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog-home') # Redirect to home after deletion

    # test_func is required by UserPassesTestMixin to check permissions
    def test_func(self):
        post = self.get_object()
        # Returns True if the current user is the author of the post
        return self.request.user == post.author
# blog/forms.py (Add this to your existing file)
from django import forms
from .models import Comment
# ... (Your existing forms like PostForm, BlogUserCreationForm)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # Only the content is input by the user. post and author are set by the view.
        fields = ['content'] 
        
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Write your comment here...'}),
        }
# blog/views.py (Update PostDetailView)
from .forms import CommentForm # Make sure this is imported

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass an empty CommentForm to display on the detail page
        context['form'] = CommentForm() 
        return context
# --- Other Views (kept for context) ---
# Assuming you have a basic home view mapped to PostListView
# and the authentication views (register, profile) defined previously.
