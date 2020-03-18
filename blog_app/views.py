from django.contrib import messages
from django.shortcuts import render, redirect
from blog_app.forms import *
from blog_app.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import Http404
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
# Create your views here.

# def login_view(request):
#     context = {}
#     return render(request, "login.html", context)

def common_data():
    return{
        "menu_list": Menu.objects.filter(status=True),
        # "footer": Footer.objects.last()
        "footer": Footer.objects.all(),
        "categories": Categories.objects.all(),
    }


def index(request):
    context = common_data()
    # context["header"] = HomePage.objects.last()
    context["header"] = HomePage.objects.all()
    context["article_list"] = Post.objects.all()
    context["slider_article"] = Post.objects.all()[:5]
    return render(request, "index.html", context)


def about(request):
    context = common_data()
    context["about"] = AboutPage.objects.all()
    return render(request, "about.html", context)


def contact(request):
    context = common_data()
    context["contact"] = ContactInfo.objects.all()
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST or None)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            from_emaill = form.cleaned_data['from_emaill']
            message = form.cleaned_data['message']
            try:
                msg = EmailMessage(fullname, message, from_emaill, ['gulnarnecefova1996@gmail.com'], reply_to=[from_emaill])
                msg.send()
                # send_mail(fullname, message, from_emaill, ['gulnarnecefova1996@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('index')
    context['form'] = form
    return render(request, "contact.html", context)


def detail_article(request, pk):
    context = common_data()
    context["article"] = Post.objects.get(pk=pk)
    return render(request, "detail.html", context)


def login_view(request):
    context = {}
    if not request.user.is_authenticated:
        context["form"] = AuthenticationForm()
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('user_account')
                else:
                    return render(request, "login.html", context)
            else:
                return render(request, "login.html", context)
        else:
            return render(request, "login.html", context)
    else:
        return redirect("user_account")


@login_required(login_url="login_view")
def user_account(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            article_id = request.POST.get("article_id")
            context = common_data()
            article = Post.objects.filter(
                id=article_id,
                article_author=request.user
            )
        context = common_data()
        context["article_list"] = Post.objects.filter(
            article_author=request.user
        )
    # context["article_list"] = Post.objects.all()
        return render(request, "user_account.html", context)
    else:
        return redirect("/")


def logout_view(request):
    logout(request)
    return redirect("/")


@login_required(login_url="login_view")
def add_blog(request):
    today = timezone.now()
    context = common_data()
    context["form"] = BlogForm()
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.article_author = request.user
            article.save()
            return redirect("user_account")
        else:
            context["form"] = form
    return render(request, "add_blog.html", context)


@login_required(login_url="login_view")
def edit_blog(request, pk):
    context = common_data()
    article = Post.objects.filter(article_author=request.user, pk=pk).last()
    if article:
        context["edit"] = True
        context["category"] = article.category
        context["title"] = article.title
        context["sub_title"] = article.sub_title
        context["body"] = article.body
        context["image"] = article.image.url if article.image else False
        context["status"] = article.status
        context["form"] = BlogForm(instance=article)
        if request.method == "POST":
            form = BlogForm(request.POST,
                            request.FILES,
                            instance=article)
            if form.is_valid():
                form.save()
                return redirect("user_account")
            else:
                context["form"] = form
        return render(request, "add_blog.html", context)
    else:
        return Http404("Not found")


@login_required(login_url="login_view")
def delete_blog(request, pk):
    post = Post.objects.filter(article_author=request.user, pk=pk)
    post.delete()
    return redirect(user_account)


@login_required(login_url="login_view")
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password has been chanegd successfully!')
            logout(request)
            return redirect('login_view')
        else:
            messages.warning(request, 'Make sure you type the password according to the rules.')  
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'change_password.html', args)



def test(request):
    context = common_data()
    return render(request, "change_password.html", context)



