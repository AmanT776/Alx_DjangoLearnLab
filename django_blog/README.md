## Overview

This Django authentication system provides:

- User registration with email, first name, last name, and password.  
- User login with secure password authentication.  
- Profile management allowing users to view and update their information.  
- Logout functionality to end user sessions.  
- Authentication protections for sensitive pages.  

It uses Django’s built-in authentication framework (`User` model) with both class-based and function-based views.

---

## Setup Instructions

1. Install Django** (if not already installed):
    pip install django
    Create a Django project:
    django-admin startproject myproject
    cd myproject
    Create an app (e.g., blog):
    python manage.py startapp blog
    Add the app and authentication settings in settings.py:

    INSTALLED_APPS = [
        ...,
        'django.contrib.auth',
        'django.contrib.messages',
        'blog',
    ]
    LOGIN_URL = 'login'
    LOGIN_REDIRECT_URL = 'profile'
    LOGOUT_REDIRECT_URL = 'home'
    
### Include app URLs in project/urls.py:
    from django.urls import path, include
    urlpatterns = [
        path('', include('blog.urls')),
    ]
### User Registration
    URL: /register/

    View: RegisterUser (CreateView)

    Form: UserRegistrationForm with extra fields: email, first_name, last_name

### Steps:
    Navigate to /register/.
    Fill out the form and submit.
    On success, redirected to /login/.

### User Login
    URL: /login/
    View: LoginUser (LoginView)
    Template: login.html

#### Features:
    Authenticates users via username and password.
    Redirects logged-in users to /profile/.

#### Steps:
    Navigate to /login/.
    Enter username & password.
    Submit to log in.
    Redirected to /profile/.

### User Profile & Update
    URL: /profile/
    View: profile_view (@login_required)
    Form: UserUpdateForm

#### Features:
    View current information (username, email, first name, last name).
    Update profile information via the form.
    Display success messages after updating.

#### Steps:
    Navigate to /profile/.
    Edit the fields and submit.
    Updated info displayed immediately.

#### User Logout
    URL: /logout/
    View: Django’s LogoutView

## Models

### Post Model
    Field	Type	Description
    title	CharField	Title of the blog post
    content	TextField	Full content of the blog post
    author	ForeignKey(User)	The user who created the post
    created_at	DateTimeField	Timestamp when post is created

The author field is required; posts cannot exist without an associated user.

### URLs
URL                     Pattern	Name	View	        Description
/post/create/	        post-create	    PostCreateView	Create a new post
/posts/	posts	        posts	        PostListView    List all posts
/post/<int:pk>/	        post-detail	    PostDetailView	View single post details
/post/<int:pk>/edit/	post-update	    PostUpdateView	Update an existing post
/post/<int:pk>/delete/	post-delete	    PostDeleteView	Delete a post
## Views
### PostCreateView
    Class-based view: CreateView
    Allows authenticated users to create posts.
    get_success_url redirects to post detail after creation.
    Template: create_blog.html

### PostListView
    Class-based view: ListView
    Displays all posts in reverse chronological order.
    Template: posts.html

### PostDetailView
    Class-based view: DetailView
    Displays post title, content, author, and creation date.
    Template: post.html

### PostUpdateView
    Class-based view: UpdateView
    Allows only the post author to update a post.
    Template: update_post.html
    Redirects to post detail after update.
### PostDeleteView
    Class-based view: DeleteView
    Allows only the post author to delete a post.
    Template: delete_post.html
    Redirects to post list after deletion.

## Templates
    Template	        Description
    create_blog.html	Form for creating new posts
    posts.html	        Lists all posts with links to detail pages
    post.html	        Displays full post details
    update_post.html	Form for editing an existing post
    delete_post.html	Confirmation page to delete a post
