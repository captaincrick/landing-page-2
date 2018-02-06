from django.conf.urls import url
from . import views

app_name = 'signup_cn'

urlpatterns = [

    url(r'^$',views.SignUpView.as_view(),name='signup'),
    url(r'^success/$',views.SuccessView.as_view(),name='success'),

]
