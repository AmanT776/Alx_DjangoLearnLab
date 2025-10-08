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