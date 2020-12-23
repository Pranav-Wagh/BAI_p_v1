from django.urls import path
from BAI_app_v2 import views
from django.contrib.auth import views as auth_views

app_name = 'BAI_app_v2'

urlpatterns = [
    path('signup/',views.signup,name = 'signup'),
    path('user_login/',views.user_login,name="user_login"),
    path('login/',views.user_login,name="login"),
    path('',views.participant_logout,name="participant_logout"),
    path('form1/',views.form1,name="form1"),
    path('form2/',views.form2,name="form2"),
    path('form3/',views.form3,name="form3"),
    path('form0/',views.form0,name="form0"),
    path('user_landing/',views.user_landing,name="user_landing"),
    path('user_profile/',views.user_profile,name="user_profile"),
    path('change_pass/',views.change_pass,name='change_pass'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='BAI_app_v2/PasswordReset.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='BAI_app_v2/PasswordResetDone.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='BAI_app_v2/PasswordResetConfirm.html'),name='password_reset_comfirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='BAI_app_v2/PasswordResetComplete.html'),name='password_reset_complete'),
]