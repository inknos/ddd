from django.shortcuts import render
from django.http import HttpResponse
from .models import Contributor, Institution, Action,Contribution
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    return render(request, 'database/database.html')

@login_required
def contributors(request):
    contributors_list = Contributor.objects.order_by('name')
    context = { "contributors_list": contributors_list }
    return render(request, 'database/contributors.html', context)

@login_required
def institutions(request):
    institutions_list = Institution.objects.order_by('name')
    context = { "institutions_list": institutions_list }
    return render(request, 'database/institutions.html', context)

@login_required
def actions(request):
    actions_list = Action.objects.order_by('name')
    context = { "actions_list": actions_list }
    return render(request, 'database/actions.html', context)

@login_required
def contributions(request):
    contributions_list = Contribution.objects.order_by('name_of_contributor')
    context = { "contributions_list": contributions_list }
    return render(request, 'database/contributions.html', context)

@login_required
def contributor(request, name):
    try:
        contributor = Contributor.objects.get(name=name)
    except:
        raise Http404("Contributor does not exist, create one!")
    contributions_list = Contribution.objects.filter(name_of_contributor__name=name)
    return render(
        request,
        'database/contributor.html',
        {
            "contributor" : contributor,
            "contributions_list" : contributions_list,
        }
    )

@login_required
def institution(request, name):
    try:
        institution = Institution.objects.get(name=name)
    except:
        raise Http404("Institution does not exist, create one!")
    contributions_list = Contribution.objects.filter(target_institution__name=name)
    contributors_list = Contributor.objects.filter(institution__name=name)
    return render(
        request,
        'database/institution.html',
        {
            "institution" : institution ,
            "contributions_list": contributions_list,
            "contributors_list" : contributors_list,
        }
    )

@login_required
def action(request, name):
    try:
        action = Action.objects.get(name=name)
    except:
        raise Http404("Action does not exist, create one!")
    contributions_list = Contribution.objects.filter(action_type__name=name)
    return render(
        request,
        'database/action.html',
        {
            "action" : action,
            "contributions_list" : contributions_list,
        }
    )

@login_required
def contribution(request, id):
    try:
        contribution = Contribution.objects.get(pk=id)
    except:
        raise Http404("Contribution does not exist, create one!")
    return render(
        request,
        'database/contribution.html',
        { "contribution" : contribution }
    )
