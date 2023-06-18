from django.shortcuts import get_object_or_404, render
from .models import Proposal

def index(request):
    latest_proposal_list = Proposal.objects.order_by("-modification_date")[:5]
    context = {"latest_proposal_list": latest_proposal_list}
    return render(request, "proposals/index.html", context)    

def detail(request, id):
    question = get_object_or_404(Proposal, pk = id)
    context = {"question": question}
    return render(request, "proposals/detail.html", context)