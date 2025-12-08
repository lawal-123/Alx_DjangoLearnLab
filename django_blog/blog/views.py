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
# blog/views.py (Add these views to your existing file)
from django.db.models import Q # New Import
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
# ... (other imports like Post, PostListView, etc.)

# --- Search Functionality ---
class PostSearchView(ListView):
    model = Post
    template_name = 'blog/search_results.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q') # Get the search query from the URL
        if query:
            # Use Q objects for complex lookups: searching across title, content, OR tags
            object_list = Post.objects.filter(
                Q(title__icontains=query) | # Case-insensitive title match
                Q(content__icontains=query) | # Case-insensitive content match
                Q(tags__name__icontains=query) # Case-insensitive tag name match
            ).distinct() # Use distinct to avoid duplicate results if a post matches multiple criteria
        else:
            object_list = Post.objects.none() # Return no results if no query
            
        return object_list.order_by('-published_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context

# --- Tag Filtering Functionality ---
class PostTagView(ListView):
    model = Post
    template_name = 'blog/post_by_tag.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # Filter posts by the tag slug passed in the URL
        tag_slug = self.kwargs.get('tag_slug')
        if tag_slug:
            # Use TaggableManager's filter function
            object_list = Post.objects.filter(tags__slug=tag_slug).order_by('-published_date')
        else:
            object_list = Post.objects.all().order_by('-published_date')

        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_slug = self.kwargs.get('tag_slug')
        # Get the actual tag name for display in the template
        if tag_slug:
             # Look up the tag by its slug to pass the name
            from taggit.models import Tag
            context['tag_name'] = get_object_or_404(Tag, slug=tag_slug).name
        return context
# --- Other Views (kept for context) ---
# Assuming you have a basic home view mapped to PostListView
# and the authentication views (register, profile) defined previously.
