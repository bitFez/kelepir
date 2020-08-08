from urllib.parse import quote_plus
from django.shortcuts import render, get_object_or_404, redirect
from .models import Maddeler, Votes, Kuponlar, Katagoriler, Comment
from hesaplar.models import Kullanici
# list view adds a queryset for us and looks up all records in the DB.
# Detailview only looks up 1 id!
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from . forms import CreateUserForm, DealForm, KuponForm, CommentForm, UserEditForm, ProfileEditForm

from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST

def index(request):
    kelepirler = Maddeler.objects
    katagoriler = Katagoriler.objects
    yorumlar = Comment.objects.filter(active=True)
    h1 = 'Günün Kelepirleri'
    #comment_c = request.build_absolute_uri

    context = {'yorumlar': yorumlar,'kelepirler':kelepirler, 'katagoriler':katagoriler, 'h1':h1}
    return render(request, 'madde/index.html', context)

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
def upvote(request,madde_id):
    if request.method == 'POST':
        try:
            vote = Votes.objects.get_object_or_404(madde=madde_id, kullanici=request.user)
        except Vote.DoesNotExist:
            vote = None

        if vote is None:
            # find madde by id and increment
            kelepir = Maddeler.objects.get_object_or_404(id=madde_id)
            vote = Votes(kelepir=kelepir, user=request.user)
            kelepir.votes_total += 1
            kelepir.derece +=2

            vote.save()
            kelepir.save()

@login_required()
def downvote(request,madde_id):
    if request.method == 'POST':
        try:
            vote = Votes.objects.get_object_or_404(madde=madde_id, kullanici=request.user)
        except Vote.DoesNotExist:
            vote = None

        if vote is None:
            # find madde by id and increment
            kelepir = Maddeler.objects.get_object_or_404(id=madde_id)
            vote = Votes(kelepir=kelepir, user=request.user)
            kelepir.votes_total += 1
            kelepir.derece -=2

            vote.save()
            kelepir.save()

def madde_detay(request, pk):
    template_name = 'madde/maddeler_detail.html'
    madde = get_object_or_404(Maddeler, pk=pk)
    yorumlar = madde.comments.filter(active=True)
    #share_string = quote_plus(madde.content)
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

    context = {'madde':madde, 'yorumlar': yorumlar, 'new_comment': new_comment,
    'comment_form': comment_form}
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
    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST or None, instance=request.user)
        profile_form = ProfileEditForm(data=request.POST or None, instance=request.user.kullanici, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.kullanici)
    context = {
        'user_form': user_form,
        'profile_form':profile_form,

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
    if request.method == 'POST':
        yorum = get_object_or_404(Comment, id=request.POST.get('comment_id'))

        yorum.likes.add(request.user)
        return HttpResponseRedirect(yorum.get_absolute_url())
