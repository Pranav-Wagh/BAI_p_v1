from django.urls import path
from BAI_app_v2 import views
from django.contrib.auth import views as auth_views

app_name = 'BAI_app_v2'

urlpatterns = [
    path('signup/',views.signup,name = 'signup'),
    path('user_login/',views.user_login,name="user_login"),
    path('login/',views.user_login,name="login"),
    path('',views.participant_logout,name="participant_logout"),
    path('form1_1/',views.form1_1,name="form1_1"),
    path('form1_2/',views.form1_2,name="form1_2"),
    path('form1_3/',views.form1_3,name="form1_3"),
    path('form1_4/',views.form1_4,name="form1_4"),
    path('form2_1/',views.form2_1,name="form2_1"),
    path('form2_2/',views.form2_2,name="form2_2"),
    path('form2_3/',views.form2_3,name="form2_3"),
    path('form3/',views.form3,name="form3"),
    path('form0/',views.form0,name="form0"),
    path('user_landing/',views.user_landing,name="user_landing"),
    path('user_profile/',views.user_profile,name="user_profile"),
    path('change_pass/',views.change_pass,name='change_pass'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='BAI_app_v2/PasswordReset.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='BAI_app_v2/PasswordResetDone.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='BAI_app_v2/PasswordResetConfirm.html'),name='password_reset_comfirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='BAI_app_v2/PasswordResetComplete.html'),name='password_reset_complete'),
    path('activate/<uidb64>/<token>/',views.activate,name="activate"),
    path('adminBAI/',views.adminBAI,name="adminBAI"),
    path('admin_home/',views.admin_home,name="admin_home"),
    path('add_jury/',views.add_jury,name="add_jury"),
    path('admin_verified/',views.admin_verified,name="admin_verified"),
    path('admin_notverified/',views.admin_notverified,name="admin_notverified"),
    path('view_jury/',views.view_jury,name="view_jury"),

    path('viewForm1_1/<user>/<int:cat_id>',views.viewForm1_1,name="viewForm1_1"),
    # path('viewForm1_2/<user>/<cat>',views.viewForm1_2,name="viewForm1_2"),
    # path('viewForm1_3/<user>/<cat>',views.viewForm1_3,name="viewForm1_3"),
    # path('viewForm1_4/<user>/<cat>',views.viewForm1_4,name="viewForm1_4"),
    # path('viewForm2_1/<user>/<cat>',views.viewForm2_1,name="viewForm2_1"),
    # path('viewForm2_2/<user>/<cat>',views.viewForm2_2,name="viewForm2_2"),
    # path('viewForm2_3/<user>/<cat>',views.viewForm2_3,name="viewForm2_3"),
    # path('viewForm3/<user>/<cat>',views.viewForm3,name="viewForm3"),

    path('AcceptForm/<user>/<int:cat_id>',views.AcceptForm,name="AcceptForm"),
    path('RejectForm/<user>/<int:cat_id>',views.RejectForm,name="RejectForm"),
]