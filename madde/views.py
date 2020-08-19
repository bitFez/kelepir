from urllib.parse import quote_plus
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Maddeler, Votes, Kuponlar, Katagoriler, Comment, Commentlike
from hesaplar.models import Kullanici
# list view adds a queryset for us and looks up all records in the DB.
# Detailview only looks up 1 id!
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.db.models import Q
from . forms import CreateUserForm, DealForm, KuponForm, CommentForm, UserEditForm, ProfileEditForm
import urllib
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from social_django.models import UserSocialAuth
from datetime import datetime, timedelta

def index(request):
    kelepirler = Maddeler.objects
    katagoriler = Katagoriler.objects
    yorumlar = Comment.objects.filter(active=True)
    h1 = 'Günün Kelepirleri'
    one_week_ago = datetime.today() - timedelta(days=7)
    haftanin = Maddeler.objects.filter(duyurmaTarihi__gte=one_week_ago).order_by('-derece')

    # This section is for the search bar!
    query = request.GET.get('q')
    if query:
        kelepirler = Maddeler.objects.filter(aktif=True).filter(
            Q(baslik__icontains=query)|
            Q(paylasan__username=query)|
            Q(ayrintilar__icontains=query)
            )


    context = {'yorumlar': yorumlar,'kelepirler':kelepirler, 'katagoriler':katagoriler, 'h1':h1, 'haftanin':haftanin}
    return render(request, 'madde/index.html', context)

def proper_pagination(yorumsayfasi, index):
    start_index = 0
    end_index = 7
    if yorumsayfasi.number > index:
        start_index = yorumsayfasi.number-index
        end_index = start_index + end_index
    return (start_index, end_index)

def dealcategory(request, kat_id):
    kelepirler = Maddeler.objects.filter(katagori=kat_id)
    katagoriler = Katagoriler.objects
    yorumlar = Comment.objects.filter(active=True)
    h1 = 'Günün Kelepirleri'
    context = {'yorumlar': yorumlar,'kelepirler':kelepirler, 'katagoriler':katagoriler, 'h1':h1}
    return render(request, 'madde/index.html', context)

def newdeals(request):
    kelepirler = Maddeler.objects.order_by('-duyurmaTarihi')
    katagoriler = Katagoriler.objects
    yorumlar = Comment.objects.filter(active=True)
    h1 = 'En Yeni Kelepirleri'
    context = {'yorumlar': yorumlar,'kelepirler':kelepirler, 'katagoriler':katagoriler, 'h1':h1}
    return render(request, 'madde/index.html', context)

def hottestdeals(request):
    kelepirler = Maddeler.objects.order_by('derece')
    katagoriler = Katagoriler.objects
    yorumlar = Comment.objects.filter(active=True)
    h1 = 'Kaynayan Kelepirler'
    context = {'yorumlar': yorumlar,'kelepirler':kelepirler, 'katagoriler':katagoriler, 'h1':h1}
    return render(request, 'madde/index.html', context)

def kuponlarindeksi(request):
    kuponlar = Kuponlar.objects

    context = {'kuponlar':kuponlar}
    return render(request, 'madde/kuponlarindeksi.html', context)

@login_required()
def upvote(request):
    if request.POST.get('action')=='post':

        id=request.POST.get("maddeid") # gets id from AJAX function on html sheet
        madde = get_object_or_404(Maddeler, id=id)
        if not madde.oyveren.filter(id=request.user.id).exists():
            result = ''
            madde.oyveren.add(request.user)
            madde.oylar +=1
            madde.derece +=2
            result = madde.derece
            madde.save()

        return JsonResponse({'result':result})

@login_required()
def downvote(request):
    if request.POST.get('action')=='post':

        id=request.POST.get("maddeid")

        madde = get_object_or_404(Maddeler, id=id)
        if not madde.oyveren.filter(id=request.user.id).exists():
            result=''
            madde.oyveren.add(request.user)
            madde.oylar +=1
            madde.derece -=2
            result = madde.derece
            madde.save()

    return JsonResponse({'result':result})

def profil_detay(request, pk):
    kullanici = get_object_or_404(User, pk=pk)
    profil = get_object_or_404(Kullanici, pk=pk)
    bookmarked = Maddeler.objects.filter(bookmarked=kullanici.id)
    kelepirler = Maddeler.objects.filter(paylasan=kullanici.id)
    instagram = 'http://www.instagram.com/'
    insta_handle = urllib.parse.urljoin(instagram, profil.insta)
    context = {'profil':profil, 'kullanici':kullanici, 'kelepirler':kelepirler, 'bookmarked':bookmarked, 'insta_handle':insta_handle}
    return render(request, 'registration/profil_gor.html', context)

def madde_detay(request, pk):
    #template_name = 'madde/maddeler_detail.html'
    madde = get_object_or_404(Maddeler, pk=pk)

    ### Bookmarks
    bookmarked = False
    if madde.bookmarked.filter(id=request.user.id).exists():
        bookmarked = True
    else:
        bookmarked = False


    yorumlar = madde.comments.filter(active=True)

    new_comment = None


    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.madde = madde
            # Assign the current post to an poster
            kullanici = Kullanici.objects.get(id=request.user.id)
            new_comment.kullanici = kullanici
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    ### Comments Paginator
    #comment_c = request.build_absolute_uri
    paginator = Paginator(yorumlar, 3) # Show 10 comments per page.
    page_number = request.GET.get('page')
    try:
        yorumsayfasi = paginator.page(page_number)
    except PageNotAnInteger: #leads to page 1
        yorumsayfasi = paginator.page(1)
    except EmptyPage:
        yorumsayfasi = paginator.page(paginator.num_pages)

    if page_number is None:
        start_index = 0
        end_index = 7
    else:
        (start_index, end_index) = proper_pagination(yorumsayfasi, index=4)
    page_range = list(paginator.page_range)[start_index:end_index]


    context = {'madde':madde, 'yorumlar': yorumlar, 'new_comment': new_comment,'comment_form': comment_form,
    'page_range':page_range, 'bookmarked':bookmarked,'yorumsayfasi':yorumsayfasi}
    return render(request, 'madde/maddeler_detail.html', context)


def registration(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            Kullanici.objects.create(kullanici=user)

            messages.success(request, 'Account created, now log in '+ username)
            return redirect('login')
        else:
            context = {'form':form}
            return render(request, 'registration/register.html', context)
    else:

        context = {'form':form}
        return render(request, 'registration/register.html', context)

@login_required
def edit_profile(request):
    kullanici = get_object_or_404(User, pk=request.user.id)
    profil = get_object_or_404(Kullanici, pk=request.user.id)
    kelepirler = Maddeler.objects.filter(paylasan=kullanici.id)
    instagram = 'http://www.instagram.com/'
    insta_handle = urllib.parse.urljoin(instagram, profil.insta)
    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST or None, instance=request.user)
        profile_form = ProfileEditForm(data=request.POST or None, instance=request.user.kullanici, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('edit_profile'))
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.kullanici)
    context = {
        'user_form': user_form,
        'profile_form':profile_form,
        'profil':profil,
        'kullanici':kullanici,
        'kelepirler':kelepirler,
        'insta_handle':insta_handle,
    }
    return render(request, 'registration/edit_profile.html', context)


@login_required(login_url="login/")
def submitdeal(request):
    form = DealForm()
    if request.method == 'POST':
        form = DealForm(request.POST, request.FILES)
        #form = ReviewForm(request.POST, request.DATA or None, instance=request.user)
        if form.is_valid():
            kullanici = Kullanici.objects.get(id=request.user.id)
            madde = form.save(commit=False) # dont save juts yet!
            madde.paylasan = kullanici # attach author to the instance of the review

            madde.save() # now save it with the author attached!
            return redirect('index')
        else:
            form = DealForm()

    return render(request, 'madde/paylasforma.html', {'form':form})

@login_required(login_url="login/")
def submitkupon(request):
    form = KuponForm()
    if request.method == 'POST':
        form = KuponForm(request.POST, request.FILES)
        #form = ReviewForm(request.POST, request.DATA or None, instance=request.user)
        if form.is_valid():
            kullanici = Kullanici.objects.get(id=request.user.id)
            madde = form.save(commit=False) # dont save juts yet!
            madde.paylasan = kullanici # attach author to the instance of the review

            madde.save() # now save it with the author attached!
            return redirect('index')
        else:
            form = KuponForm()

    return render(request, 'madde/kuponforma.html', {'form':form})

@login_required
def like_comment(request):
    if request.method =='GET':
        comment_id = request.GET['commentlike_id']
        likedcomment = Comment.objects.get(id=comment_id)
        newlike = Commentlike(comment=likedcomment)
        newlike.save()
        return HttpResponse('You liked this comment')
    else:
        return HttpResponse('Like was not successful')

    '''user = request.user
    if request.method == 'POST':
        pk = request.POST.get('comment_id')
        comment_obj = Comment.objects.get(pk=pk)
        if user in comment_obj.likes.all():
            comment_obj.likes.remove(user)
        else:
            comment_obj.likes.add(user)
    return HttpResponse()'''

def madde_serialised(request):
    data = list(Comment.objects.values())
    return JsonResponse(data, safe=False)

class SettingsView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        user = request.user

        try:
            github_login = user.social_auth.get(provider='github')
        except UserSocialAuth.DoesNotExist:
            github_login = None

        try:
            twitter_login = user.social_auth.get(provider='twitter')
        except UserSocialAuth.DoesNotExist:
            twitter_login = None

        try:
            facebook_login = user.social_auth.get(provider='facebook')
        except UserSocialAuth.DoesNotExist:
            facebook_login = None

        can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

        return render(request, 'registration/settings.html', {
            'github_login': github_login,
            'twitter_login': twitter_login,
            'facebook_login': facebook_login,
            'can_disconnect': can_disconnect
        })


@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'registration/password.html', {'form': form})


@login_required
def bookmark(request,id):
    madde = get_object_or_404(Maddeler, id=id)
    if madde.bookmarked.filter(id=request.user.id).exists():
        madde.bookmarked.remove(request.user)
    else:
        madde.bookmarked.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def expire(request,id):
    madde = get_object_or_404(Maddeler, id=id)
    if not madde.tukenmiscagiri.filter(id=request.user.id).exists():
        madde.bookmarked.add(request.user)
        if madde.tukenmiscagiri.count >= 5:
            madde.aktif = False
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
