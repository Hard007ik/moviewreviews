from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('email/',views.email,name='email'),
    path('detail/<int:movie_id>',views.detail,name='detail'),
    path('detail/<int:movie_id>/create/',views.createreview,name='createreview'),
    path('review/<int:review_id>',views.updatereview,name='updatereview'),
    path('review/<int:review_id>/delete/', views.deletereview, name='deletereview'),
]
