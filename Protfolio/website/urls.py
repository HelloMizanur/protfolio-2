from django.urls import path, include
from website import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name = 'index'),
    # path('about/', views.about, name='about'),
    # path('resume/', views.resume, name='resume'),
    # path('protfolio/', views.protfolio, name='protfolio'),
    # path('blog/', views.blog, name='blog'),
    # path('contuct/', views.contuct, name='contuct'),
    # path('blogPost/', views.blogPost, name='blogPost'),
    # path('prtofoliodetail/', views.prtofolioDetail, name='prtofolioDetail'),
]
