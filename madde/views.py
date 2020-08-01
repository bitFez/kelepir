from django.shortcuts import render, get_object_or_404, redirect
from .models import Maddeler
from django.views import generic
# Create your views here.
def index(request):
    kelepirler = Maddeler.objects

    context = {'kelepirler':kelepirler}
    return render(request, 'madde/index.html', context)


@login_required
def upvote(request,madde_id):
    try:
        vote = Vote.objects.get(madde=madde_id, kullanici=request.user)
      except Vote.DoesNotExist:
        vote = None

      if vote is None:
        # find madde by id and increment
        kelepir = Maddeler.objects.get(id=madde)
        vote = Vote(kelepir=kelepir, user=request.user)
        kelepir.votes_total += 1
        kelepir.derece +=2

        vote.save()
        kelepir.save()

@login_required
def downvote(request,madde_id):
    try:
        vote = Vote.objects.get(madde=madde_id, kullanici=request.user)
      except Vote.DoesNotExist:
        vote = None

      if vote is None:
        # find madde by id and increment
        kelepir = Maddeler.objects.get(id=madde)
        vote = Vote(kelepir=kelepir, user=request.user)
        kelepir.votes_total += 1
        kelepir.derece -=2

        vote.save()
        kelepir.save()



class MaddeDetailView(generic.DetailView):
    model = Maddeler
