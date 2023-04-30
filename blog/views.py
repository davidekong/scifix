from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from blog.models import Post, CommentModel, CustomUser, Subscribers
from django.contrib.auth.models import User

import datetime
from django.urls import reverse
# Create your views here.


def signup(request):
    context = {
        'error_message': ''
    }
    valid = False
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if username == '' or email == '' or password1 == '' or password2 == '':
            valid = False
            context['error_message'] = 'Please ensure all fields are appropriately filled.'
        elif len(password1) < 5:
            valid = False
            context['error_message'] = 'Please ensure password is not less than 5 characters.'
        else:
            valid = True
        
        if valid == True:
            if password1 == password2:
                user = authenticate(username=username, email=email)
                if user is None:
                    new_user = User.objects.create_user(username=username, email=email, password=password1)

                    new_user.save()
                    login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
                    return redirect('home')
                else:
                    context['error_message'] = "There is already a user associated with the following credentials. Would you like to login?"
            else:
                context['error_message'] = 'Please make sure both passwords match.'
    return render(request, 'blog/signup.html', context)

def forgot_password(request):
    context = {
        "error_message": ""
    }
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user_id = User.objects.get(email=email).id
            send_mail(
                'Open the link to change your password.', 
                request.build_absolute_uri(reverse('change_password', args=(user_id, ))), 
                'scifixblogs@gmail.com', 
                [email], 
                fail_silently=False)
            
            return redirect('forgot_password')
        except User.DoesNotExist:
            context['error_message'] = f"There is no account with email {email}.\nMaybe you signed in with google."
    return render(request, 'blog/forgot_password.html', context)

def change_password(request, pk):
    context = {
        'error_message': ''
    }
    if request.method == "POST":
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.get(pk=pk)
            if (user.password != password1):
                user.set_password(password1)
                user.save()
                return redirect('login')
            else:
                context['error_message'] = "You cannot use your current password."
        else:
            context['error_message'] = 'Please make sure both passwords match.'
    return render(request, 'blog/change_password.html', context)

def logIn(request):
    logout(request)
    context = {
        'error_message': ''
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            print('logged')
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
        else:
            context['error_message'] = "Did you put in the right credentials? Try registering"
    return render(request, 'blog/login.html', context)




def home(request):
    context = {
        'error_message': ''
    }
    if request.method == "POST":
        if 'subscribe_popoup_button' in request.POST:
            email = request.POST["email"]
            obj = Subscribers.objects.get_or_create(email=email, reason="")
            
            if (obj[1]):
                obj[0].save()
                send_mail(
                        'Thanks for subscribing to SCIFIX!!', 
                        'We are happy that you have chosen to subscribe to our blog site SCIFIX, and we will do our best to keep you updated on the latest posts from our blog writers on a frequent basis.', 
                        'scifixblogs@gmail.com', 
                        [email], 
                        fail_silently=False)
            else:
                # Update this to display a message to user that email is already subscribed
                pass
            
            return redirect('home')
        if 'subscribe_button' in request.POST:
            email1 = request.POST["email1"]
            email2 = request.POST["email2"]
            reason = request.POST["message"]
            if (email1 == email2):
                obj = Subscribers.objects.get_or_create(email=email1, reason="")
                if (obj[1]):
                    obj[0].reason = reason
                    obj[0].save()
                    send_mail(
                            'Thanks for subscribing to SCIFIX!!', 
                            'We are happy that you have chosen to subscribe to our blog site SCIFIX, and we will do our best to keep you updated on the latest posts from our blog writers on a frequent basis.', 
                            'scifixblogs@gmail.com',
                            [email1], 
                            fail_silently=False)
                else:
                    # Update this to display a message to user that email is already subscribed
                    pass
                
                return redirect('home')
            else:
                context['error_message'] = 'Please make sure both emails are identical.'

    return render(request, 'blog/home.html')



def blogs(request):
    return render(request, 'blog/blogs.html')


# all post views here:
def dart(request):
    context = {
        'comments': list(Post.objects.get(title='DART').commentmodel_set.all())
    }
    # Put this in Celery before deployment
    if request.method == "POST":
        if 'subscribe_button' in request.POST:
            email = request.POST['email']
            send_mail(
                'Thanks for subscribing to SCIFIX!!', 
                'We are happy that you have chosen to subscribe to our blog site SCIFIX, and we will do our best to keep you updated on the latest posts from our blog writers on a frequent basis.', 
                'davidukemeekong1@gmail.com', 
                [email], 
                fail_silently=False)
        elif 'comment_button' in request.POST:
            comment = request.POST['comment']
            date = datetime.datetime.today().ctime().split(" ")
            c = CommentModel.objects.create(comment_text=comment, post=Post.objects.get(title="DART"), user=request.user, time=f"{date[1]} {date[2]} {date[-1]}")
            c.save()
            return redirect('dart')

    return render(request, 'blog/posts/DART.html', context)

def scifix(request):
    # Put this in Celery before deployment
    context = {
        'comments': list(Post.objects.get(title='SCIFIX').commentmodel_set.all())
    }
    # Put this in Celery before deployment
    if request.method == "POST":
        if 'subscribe_button' in request.POST:
            email = request.POST['email']
            send_mail(
                'Thanks for subscribing to SCIFIX!!', 
                'We are happy that you have chosen to subscribe to our blog site SCIFIX, and we will do our best to keep you updated on the latest posts from our blog writers on a frequent basis.', 
                'davidukemeekong1@gmail.com', 
                [email], 
                fail_silently=False)
        elif 'comment_button' in request.POST:
            comment = request.POST['comment']
            date = datetime.datetime.today().ctime().split(" ")
            c = CommentModel.objects.create(comment_text=comment, post=Post.objects.get(title="SCIFIX"), user=request.user, time=f"{date[1]} {date[2]} {date[-1]}")
            c.save()
            return redirect('scifix')
    return render(request, 'blog/posts/scifix.html', context)

def contact_us(request):
    context = {
        'error_message_email': '',
        'note': ''
    }
    # Sorry, both emails must match.
    if (request.method == "POST"):
        if (request.POST['email1'] == request.POST['email2']):
            email = request.POST['email1']
            message = request.POST['message']
            full_name = request.POST['first_name'] + " " + request.POST['last_name']
            send_mail(
                f'Message from {full_name} via S C I F I X', 
                f'{full_name}: {message}',
                email, 
                ['scifixblogs@hotmail.com'], 
                fail_silently=False)
            send_mail(
                'Thanks for sending this message to SCIFIX!!', 
                f'We are glad to here from you, {full_name}. The email will be responded to in about 2 work days. Thank you for using S C I F I X.',
                'davidukemeekong1@gmail.com', 
                [email], 
                fail_silently=False)
            context['note'] = 'Thank you for your email and have a good day.'
        else:
            context['error_message_email'] = 'Sorry, both emails are supposed to match.'
    return render(request, 'blog/contact_us.html', context)