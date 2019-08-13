from django.urls import path, include

from . import views

urlpatterns = [
    # ex: /database/
    path('', views.index, name='index'),
    # ex: /database/contributors
    path('contributors/', views.contributors, name='contributors'),
    # ex: /database/institutions
    path('institutions/', views.institutions, name='institutions'),
    # ex: /database/actions
    path('actions/', views.actions, name='actions'),
    # ex: /database/contributions
    path('contributions/', views.contributions, name='contributions'),
    # ex: /database/contributor/Name
    path('contributor/<str:name>', views.contributor, name="contributor"),
    # ex: /database/institution/Name
    path('institution/<str:name>', views.institution, name="institution"),
    # ex: /database/action/Name
    path('action/<str:name>', views.action, name="action"),
    # ex: /database/contribution/Name
    path('contribution/<int:id>', views.contribution, name="contribution"),

    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]
