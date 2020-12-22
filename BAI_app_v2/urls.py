from django.urls import path
from BAI_app_v2 import views

app_name = 'BAI_app_v2'

urlpatterns = [
    path('signup/',views.signup,name = 'signup'),
    path('user_login/',views.user_login,name="user_login"),
    path('logout/',views.participant_logout,name="logout"),
    path('form1/',views.form1,name="form1"),
    path('form2/',views.form2,name="form2"),
    path('form3/',views.form3,name="form3"),
    path('form0/',views.form0,name="form0"),
    path('user_landing/',views.user_landing,name="user_landing"),
    path('user_profile/',views.user_profile,name="user_profile"),
]