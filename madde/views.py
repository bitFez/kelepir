from django.shortcuts import render, get_object_or_404, redirect
from .models import Maddeler, Votes
from hesaplar.models import Kullanici
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from . forms import CreateUserForm, DealForm
# Create your views here.
def index(request):
    kelepirler = Maddeler.objects

    context = {'kelepirler':kelepirler}
    return render(request, 'madde/index.html', context)


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



class MaddeDetailView(DetailView):
    model = Maddeler
    template_name = 'madde/maddeler_detail.html'


def registration(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account created, now log in '+ username)
            return redirect('login')
        else:
            context = {'form':form}
            return render(request, 'registration/register.html', context)
    else:

        context = {'form':form}
        return render(request, 'registration/register.html', context)

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
