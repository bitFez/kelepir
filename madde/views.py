from urllib.parse import quote_plus
from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.models import User
from .models import Maddeler, Votes, Kuponlar, Katagoriler
from hesaplar.models import Kullanici
# list view adds a queryset for us and looks up all records in the DB.
# Detailview only looks up 1 id!
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.db.models import Q, F
from . forms import CreateUserForm, DealForm, KuponForm, UserEditForm, ProfileEditForm, DealEditForm, KuponEditForm
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
#from django_comments_xtd.models import XtdComment
from comment.models import Comment
from hesaplar.models import Kullanici as User

def index(request):
    kelepirler = Maddeler.objects.all
    katagoriler = Katagoriler.objects
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


    context = {'kelepirler':kelepirler, 'katagoriler':katagoriler, 'h1':h1, 'haftanin':haftanin,}
    return render(request, 'madde/index.html', context)


def dealcategory(request, kat_id):
    kelepirler = Maddeler.objects.filter(katagori=kat_id)
    katagoriler = Katagoriler.objects
    #yorumlar = Comment.objects.filter(active=True)
    h1 = 'Günün Kelepirleri'
    context = {'kelepirler':kelepirler, 'katagoriler':katagoriler, 'h1':h1}
    return render(request, 'madde/index.html', context)

def newdeals(request):
    kelepirler = Maddeler.objects.order_by('-duyurmaTarihi')
    katagoriler = Katagoriler.objects
    #yorumlar = Comment.objects.filter(active=True)
    h1 = 'En Yeni Kelepirleri'
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
    context = {'kelepirler':kelepirler, 'katagoriler':katagoriler, 'h1':h1}
    return render(request, 'madde/index.html', context)

def hottestdeals(request):
    kelepirler = Maddeler.objects.order_by('-derece')
    katagoriler = Katagoriler.objects
    #yorumlar = Comment.objects.filter(active=True)
    h1 = 'Kaynayan Kelepirler'
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
    context = {'kelepirler':kelepirler, 'katagoriler':katagoriler, 'h1':h1}
    return render(request, 'madde/index.html', context)

def kuponlarindeksi(request):
    kuponlar = Kuponlar.objects.all
    h1 = 'Günün Kuponları'

    one_week_ago = datetime.today() - timedelta(days=7)
    haftanin = Kuponlar.objects.filter(duyurmaTarihi__gte=one_week_ago).order_by('-derece')

    # This section is for the search bar!
    query = request.GET.get('q')
    if query:
        kelepirler = Kuponlar.objects.filter(aktif=True).filter(
            Q(baslik__icontains=query)|
            Q(paylasan__username=query)|
            Q(ayrintilar__icontains=query)
            )
    context = {'kuponlar':kuponlar,'h1':h1, 'haftanin':haftanin,}
    return render(request, 'madde/kuponlarindeksi.html', context)

def ateslikuponlar(request):
    kuponlar = Kuponlar.objects.order_by('-derece')
    h1 = 'En Yüksek puanlı Kuponlar'

    one_week_ago = datetime.today() - timedelta(days=7)
    haftanin = Kuponlar.objects.filter(duyurmaTarihi__gte=one_week_ago).order_by('-derece')

    # This section is for the search bar!
    query = request.GET.get('q')
    if query:
        kelepirler = Kuponlar.objects.filter(aktif=True).filter(
            Q(baslik__icontains=query)|
            Q(paylasan__username=query)|
            Q(ayrintilar__icontains=query)
            )
    context = {'kuponlar':kuponlar,'h1':h1, 'haftanin':haftanin,}
    return render(request, 'madde/kuponlarindeksi.html', context)

def yenikuponlar(request):
    kuponlar = Kuponlar.objects.order_by('-duyurmaTarihi')
    h1 = 'En Yeni Kuponlar'

    one_week_ago = datetime.today() - timedelta(days=7)
    haftanin = Kuponlar.objects.filter(duyurmaTarihi__gte=one_week_ago).order_by('-derece')

    # This section is for the search bar!
    query = request.GET.get('q')
    if query:
        kelepirler = Kuponlar.objects.filter(aktif=True).filter(
            Q(baslik__icontains=query)|
            Q(paylasan__username=query)|
            Q(ayrintilar__icontains=query)
            )
    context = {'kuponlar':kuponlar,'h1':h1, 'haftanin':haftanin,}
    return render(request, 'madde/kuponlarindeksi.html', context)

@login_required
def product_upvote(request, id):
    
    # get information from request about what item id it is
    madde = Maddeler.objects.get(id=id)

    if not madde.oyveren.filter(id=request.user.id).exists():
        madde.oyveren.add(request.user)
        madde.oylar +=1
        madde.derece +=2
        madde.save()

    return render(request, 'madde/partials/madde.html', {'kelepir': madde})


@login_required
def product_downvote(request, id):
    # get information from request about what item id it is
    madde = Maddeler.objects.get(id=id)

    if not madde.oyveren.filter(id=request.user.id).exists():
        madde.oyveren.add(request.user)
        madde.oylar +=1
        madde.derece -=2
        madde.save()

    return render(request, 'madde/partials/madde.html', {'kelepir': madde})


@login_required
def coupon_vote(request):
    if request.POST.get('action') == 'postvote':
        # get information from request about what item id it is
        id = int(request.POST.get('kuponid'))
        # And also which button was pressed
        button = request.POST.get('button')
        kupon = Kuponlar.objects.get(id=id)
        #madde = get_object_or_404(Maddeler, id=id)


        if button == 'downvote_button':
            if not kupon.oyveren.filter(id=request.user.id).exists():
                kupon.oyveren.add(request.user)
                kupon.oylar +=1
                kupon.derece -=2
                kupon.save()


        elif button == 'upvote_button':
            if not kupon.oyveren.filter(id=request.user.id).exists():
                kupon.oyveren.add(request.user)
                kupon.oylar +=1
                kupon.derece +=2
                kupon.save()

        # return result
        kupon.refresh_from_db()
        result = kupon.derece
        return JsonResponse({'result':result})
    pass

def profil_detay(request, pk):
    kullanici = get_object_or_404(User, pk=pk)
    profil = get_object_or_404(Kullanici, pk=pk)
    bookmarked = Maddeler.objects.filter(bookmarked=kullanici.id)
    kbookmarked = Kuponlar.objects.filter(bookmarked=kullanici.id)
    kelepirler = Maddeler.objects.filter(paylasan=kullanici.id)
    instagram = 'http://www.instagram.com/'
    insta_handle = urllib.parse.urljoin(instagram, profil.insta)
    comments = Comment.objects.filter(user_id=kullanici)

    context = {'profil':profil, 'kullanici':kullanici, 'kelepirler':kelepirler, 'bookmarked':bookmarked,
    'comments':comments, 'kbookmarked':kbookmarked,'insta_handle':insta_handle}
    return render(request, 'registration/profil_gor.html', context)

def madde_detay(request, pk):
    madde = get_object_or_404(Maddeler, pk=pk)
    comments = Comment.objects.filter(content_type_id=9, object_id=madde.id)
    #top_comments = Comment.objects.filter_comments_by_object(madde).order_by('-reaction__likes')
    top_comments = Comment.objects.all_comments_by_object(madde).order_by('-reaction__likes').first()
    pdiff = 0
    if madde.orjinalFiyat != None:
        pchange = madde.fiyat - madde.orjinalFiyat
        pdiff = round((pchange / madde.orjinalFiyat) * 100, 0)
        pdiff = abs(pdiff)

    #top_Comments = django_comment_flags.objects.filter(flag=="I like it").filter(flag.count>=1)
    ### Bookmarks
    bookmarked = False
    if madde.bookmarked.filter(id=request.user.id).exists():
        bookmarked = True
    else:
        bookmarked = False

    context = {'madde':madde,'bookmarked':bookmarked, 'pdiff':pdiff, 'comments':comments, 'top_comments':top_comments}
    return render(request, 'madde/maddeler_detail.html', context)

def kupon_detay(request, pk):
    kupon = get_object_or_404(Kuponlar, pk=pk)
    comments = Comment.objects.filter(content_type_id=24, object_id=kupon.id)
    top_comments = Comment.objects.all_comments_by_object(kupon).order_by('-reaction__likes').first()
    ### Bookmarks
    bookmarked = False
    if kupon.bookmarked.filter(id=request.user.id).exists():
        bookmarked = True
    else:
        bookmarked = False

    context = {'kupon':kupon,'bookmarked':bookmarked, 'comments':comments, 'top_comments':top_comments}
    return render(request, 'madde/kuponlar_detail.html', context)

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
    kuponlar = Kuponlar.objects.filter(paylasan=kullanici.id)
    #comments = XtdComment.objects.filter(user_id=kullanici.id)
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
        'kuponlar':kuponlar,
        'insta_handle':insta_handle,
    }
    return render(request, 'registration/edit_profile.html', context)

@login_required
def madde_guncelle(request, pk):
    madde = Maddeler.objects.get(id=pk)

    if request.method == 'POST':
        edit_form = DealEditForm(data=request.POST or None, instance=madde, files=request.FILES)
        #profile_form = ProfileEditForm(data=request.POST or None, instance=request.user.kullanici, files=request.FILES)

        if edit_form.is_valid():
            edit_form.save()
            return redirect('madde_detay', pk=madde.id)
    else:
        edit_form = DealEditForm(instance=madde)
    context = {
        'edit_form': edit_form,
        'madde':madde,
    }
    return render(request, 'madde/deal_edit.html', context)

@login_required
def kupon_guncelle(request, pk):
    kupon = Kuponlar.objects.get(id=pk)

    if request.method == 'POST':
        edit_form = KuponEditForm(data=request.POST or None, instance=kupon, files=request.FILES)
        #profile_form = ProfileEditForm(data=request.POST or None, instance=request.user.kullanici, files=request.FILES)

        if edit_form.is_valid():
            edit_form.save()
            return redirect('kupon_detay', pk=kupon.id)
    else:
        edit_form = KuponEditForm(instance=kupon)
    context = {
        'edit_form': edit_form,
        'kupon':kupon,
    }
    return render(request, 'madde/coupon_edit.html', context)


@login_required(login_url="login/")
def submitdeal(request):
    form = DealForm()

    if request.method == 'POST':
        form = DealForm(request.POST, request.FILES)

        if form.is_valid():
            submission = form.save(commit=False) # Dont save just yet
            submission.paylasan = request.user
            submission.save()
            return redirect('index')
        else:
            form = DealForm()
    return render(request, 'madde/paylasforma.html', {'form':form})


@login_required(login_url="login/")
def submitkupon(request):
    form = KuponForm()

    if request.method == 'POST':
        form = KuponForm(request.POST, request.FILES)

        if form.is_valid():
            submission = form.save(commit=False) # Dont save just yet
            submission.paylasan = request.user
            submission.save()
            return redirect('kuponlarindeksi')
        else:
            form = KuponForm()
    return render(request, 'madde/kuponforma.html', {'form':form})


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
def bookmarkInListView(request,id):
    madde = get_object_or_404(Maddeler, id=id)
    if madde.bookmarked.filter(id=request.user.id).exists():
        madde.bookmarked.remove(request.user)
    else:
        madde.bookmarked.add(request.user)
    return render(request, 'madde/partials/madde.html', {'kelepir': madde})

@login_required
def bookmark(request,id):
    madde = get_object_or_404(Maddeler, id=id)
    if madde.bookmarked.filter(id=request.user.id).exists():
        madde.bookmarked.remove(request.user)
    else:
        madde.bookmarked.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
'''
def bookmark(request):
    if request.POST.get('action') == 'postbookmark':
        # get information from request about what item id it is
        id = int(request.POST.get('maddeid'))
        # And also which button was pressed
        #button = request.POST.get('button')
        madde = Maddeler.objects.get(id=id)
        #madde = get_object_or_404(Maddeler, id=id)

        if not madde.bookmarked.filter(id=request.user.id).exists():
            madde.bookmarked.add(request.user)
            madde.save()
        else:
            madde.bookmarked.remove(request.user)
            madde.save()

        madde.refresh_from_db()
        result = madde.bookmarked
        return JsonResponse({'result':result})
    pass
    '''

@login_required
def kbookmark(request,id):
    kupon = get_object_or_404(Kuponlar, id=id)
    if kupon.bookmarked.filter(id=request.user.id).exists():
        kupon.bookmarked.remove(request.user)
    else:
        kupon.bookmarked.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def expire(request,id):
    if request.method == 'POST':
        madde = get_object_or_404(Maddeler, id=id)
        if not madde.tukenmiscagiri.filter(id=request.user.id).exists():
            madde.tukenmiscagiri.add(request.user)
            madde.tukenmisSayi += 1
            if madde.tukenmisSayi >= 5:
                madde.aktif = False
            madde.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def expirek(request,id):
    if request.method == 'POST':
        kupon = get_object_or_404(Kuponlar, id=id)
        if not kupon.tukenmiscagiri.filter(id=request.user.id).exists():
            kupon.tukenmiscagiri.add(request.user)
            kupon.tukenmisSayi += 1
            if kupon.tukenmisSayi >= 5:
                kupon.aktif = False
            kupon.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
