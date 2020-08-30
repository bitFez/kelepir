from urllib.parse import quote_plus
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Maddeler, Votes, Kuponlar, Katagoriler
from hesaplar.models import Kullanici
# list view adds a queryset for us and looks up all records in the DB.
# Detailview only looks up 1 id!
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.db.models import Q, F
from . forms import CreateUserForm, DealForm, KuponForm, UserEditForm, ProfileEditForm
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
from django_comments_xtd.models import XtdComment

def index(request):
    kelepirler = Maddeler.objects
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
    context = {'kelepirler':kelepirler, 'katagoriler':katagoriler, 'h1':h1}
    return render(request, 'madde/index.html', context)

def hottestdeals(request):
    kelepirler = Maddeler.objects.order_by('-derece')
    katagoriler = Katagoriler.objects
    #yorumlar = Comment.objects.filter(active=True)
    h1 = 'Kaynayan Kelepirler'
    context = {'kelepirler':kelepirler, 'katagoriler':katagoriler, 'h1':h1}
    return render(request, 'madde/index.html', context)

def kuponlarindeksi(request):
    kuponlar = Kuponlar.objects

    context = {'kuponlar':kuponlar}
    return render(request, 'madde/kuponlarindeksi.html', context)

'''@login_required()
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

        return JsonResponse({'result':result})'''

@login_required
def product_vote(request):
    if request.POST.get('action') == 'vote_id':
        # get information from request about what item id it is
        id = int(request.POST.get('maddeid'))
        # And also which button was pressed
        button = request.POST.get('button')
        madde = Maddeler.objects.get(id=id)
        #madde = get_object_or_404(Maddeler, id=id)

        #get the users current vote on a product
        '''if madde.oyveren.filter(id=request.user.id).exists():
            q = Votes.objects.get(Q(madde=id) & Q(kullanici=request.user.id))
            existingVote = q.oy
            # change appearance of button if there is already a vote
            if existingVote == True:
                return JsonResponse({'existingVote'})

            pass

            if existingVote == False:
                return JsonResponse({'existingVote'})

        else:'''

        if button == 'downvote_button':
            if not madde.oyveren.filter(id=request.user.id).exists():
                madde.oyveren.add(request.user)
                madde.oylar +=1
                madde.derece -=2
                madde.save()

                '''print(f'user {request.user} \n user id {request.user.id} \n {madde}')
                existingVote = Votes(kullanici=request.user, madde=id, oy=False)
                existingVote.save()'''

        elif button == 'upvote_button':
            if not madde.oyveren.filter(id=request.user.id).exists():
                madde.oyveren.add(request.user)
                madde.oylar +=1
                madde.derece +=2
                madde.save()
                '''existingVote = Votes(kullanici=request.user, madde=id, oy=True)
                existingVote.save()'''

        # return result
        madde.refresh_from_db()
        result = madde.derece
        return JsonResponse({'result':result}) #, 'existingVote':existingVote
    pass


'''@login_required()
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
'''





def profil_detay(request, pk):
    kullanici = get_object_or_404(User, pk=pk)
    profil = get_object_or_404(Kullanici, pk=pk)
    bookmarked = Maddeler.objects.filter(bookmarked=kullanici.id)
    kelepirler = Maddeler.objects.filter(paylasan=kullanici.id)
    instagram = 'http://www.instagram.com/'
    insta_handle = urllib.parse.urljoin(instagram, profil.insta)
    comments = XtdComment.objects.filter(user_id=kullanici.id)
    context = {'profil':profil, 'kullanici':kullanici, 'kelepirler':kelepirler, 'bookmarked':bookmarked,
    'insta_handle':insta_handle, 'comments':comments}
    return render(request, 'registration/profil_gor.html', context)

def madde_detay(request, pk):
    madde = get_object_or_404(Maddeler, pk=pk)
    comments = XtdComment.objects.filter(object_pk=madde.id)
    pdiff = 0
    pchange = madde.fiyat - madde.orjinalFiyat
    pdiff = round((pchange / madde.orjinalFiyat) * 100, 0)
    print(pdiff)
    #top_Comments = django_comment_flags.objects.filter(flag=="I like it").filter(flag.count>=1)
    ### Bookmarks
    bookmarked = False
    if madde.bookmarked.filter(id=request.user.id).exists():
        bookmarked = True
    else:
        bookmarked = False

    context = {'madde':madde,'bookmarked':bookmarked, 'comments':comments, 'pdiff':pdiff}
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
    comments = XtdComment.objects.filter(user_id=kullanici.id)
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
            #kullanici = Kullanici.objects.get(id=request.user.id)
            madde = Maddeler.objects.create(
                paylasan = request.user,
                bas_tarih = form.cleaned_data.get("bas_tarih"),
                son_tarih = form.cleaned_data.get("son_tarih"),
                diyar = form.cleaned_data.get("diyar"),
                url = form.cleaned_data.get("url"),
                satici = form.cleaned_data.get("satici"),
                fiyat = form.cleaned_data.get("fiyat"),
                orjinalFiyat = form.cleaned_data.get("orjinalFiyat"),
                kargo = form.cleaned_data.get("kargo"),
                kupon = form.cleaned_data.get("kupon"),
                baslik = form.cleaned_data.get("baslik"),
                ayrintilar = form.cleaned_data.get("ayrintilar"),
                goruntu = form.cleaned_data.get("goruntu"),
                #katagori = form.cleaned_data.get("katagori"),
                online = form.cleaned_data.get("online"),
                w3w = form.cleaned_data.get("w3w")
            )

            #madde.save(commit=False) # dont save juts yet!
            #madde.paylasan = request.user.id # attach author to the instance of the deal
            madde.katagori = form.cleaned_data.get("katagori")
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
