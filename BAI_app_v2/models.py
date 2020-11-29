from django.db import models
from django.contrib.auth.models import User

# Create your models here.
yes_no=[("on","yes"),("off","no")]
ratings_1_10=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10')]
category_1_9=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9')]


class ParticipantInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)

    ph_no = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    other_membership = models.TextField(blank=True)
    company_nm = models.CharField(max_length=50)
    applicant_desig = models.CharField(max_length=25)

    #applicant_img = models.ImageField(upload_to='images',blank=True)

    def __str__(self):
        return self.user.username

class Speed(models.Model):
    users_name = models.CharField(max_length=20, blank=True)
    tender = models.CharField(choices=yes_no,max_length=4,blank=False)
    ProTimeFrame = models.TextField(max_length=100,blank=True)

    tracked = models.CharField(choices=yes_no,max_length=4,blank=False)
    PMCappointed = models.CharField(choices=yes_no,max_length=4,blank=False)
    TimeReduc = models.CharField(choices=yes_no,max_length=4,blank=False)
    trackPro = models.CharField(choices=yes_no,max_length=4,blank=False)

    expectPeriod = models.TextField(max_length=100,blank=False)
    periodComplete = models.TextField(max_length=100,blank=False)
    
    difficulty = models.CharField(choices=yes_no,max_length=4,blank=False)
    timeLost = models.TextField(max_length=100,blank=True)

    mechanization = models.TextField(max_length=100,blank=True)
    contribImprov = models.TextField(max_length=100,blank=True)
    tenderPay = models.CharField(choices=yes_no,max_length=4,blank=False)
    suggest = models.TextField(max_length=100,blank=False)
    SpeedScale = models.TextField(max_length=100,blank=False)

    def __str__(self):
        return self.users_name

class SafetynWellfare(models.Model):
    users_name = models.CharField(max_length=20,blank=True)
    monitered = models.CharField(choices=yes_no,max_length=10,blank=False)
    bywhom = models.TextField(max_length=200,blank=False)
    measures =models.TextField(max_length=200,blank=True)
    medical_aid = models.CharField(choices=yes_no,max_length=10,blank=False)
    incidents = models.CharField(choices=yes_no,max_length=10,blank=False)
    safety_audits = models.FileField(upload_to='uploads/',blank=True)

    def __str__(self):
        return self.users_name

class Others(models.Model):
    users_name = models.CharField(max_length=20, blank=True)
    accomodation= models.ImageField(upload_to='uploads/',blank=False)#
    sanitary = models.ImageField(upload_to='uploads/', blank=False)#
    school = models.ImageField(upload_to='uploads/', blank=True)
    polution_measures = models.ImageField(upload_to='uploads/', blank=False)#
    ISO_accreditation = models.CharField(choices=yes_no,max_length=4,blank=True)
    conseravation_A = models.TextField(max_length=200,blank=False)
    conseravation_B = models.TextField(max_length=200,blank=False)
    renewable_energy_text = models.TextField(max_length=200,blank=True)
    renewable_energy_pic = models.FileField(upload_to='uploads/', blank=True)
    green_building = models.TextField(max_length=2000,blank=True)
    debris_management = models.TextField(max_length=2000, blank=True)
    seminars = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return self.users_name

class Economy(models.Model):
    users_name = models.CharField(max_length=20, blank=True)
    project_cost=models.FloatField(blank=False)
    who_determined=models.TextField(blank=False,max_length=255)
    cost_reduction=models.CharField(choices=yes_no,max_length=4,blank=False)
    tracked_e=models.CharField(choices=yes_no,max_length=4,blank=True)
    who_tracked=models.TextField(blank=True,max_length=255)
    PMC_appointed=models.CharField(choices=yes_no,max_length=4,blank=True)
    expected_cost=models.FloatField(blank=False)
    actual_cost=models.FloatField(blank=False)
    difficulty_e=models.CharField(choices=yes_no,max_length=4,blank=True)
    escalated=models.TextField(blank=True,max_length=255)
    costsaving_measures=models.TextField(blank=False,max_length=255)
    suggestions=models.TextField(blank=True,max_length=255)
    cost_per_sft=models.FloatField(blank=False)
    cost_per_room=models.FloatField(blank=False)
    cost_per_bed=models.FloatField(blank=False)
    cost_per_workstation=models.FloatField(blank=False)
    cost_per_similar=models.FloatField(blank=False)
    economy_ratings=models.TextField(blank=False,max_length=100)

    def __str__(self):
        return self.users_name


class Project_info(models.Model):
    users_name = models.CharField(max_length=20, blank=True)
    project_name = models.TextField(max_length=200,blank=False)
    project_address=models.TextField(max_length=200,blank=False)
    site_map=models.FileField(upload_to="uploads/",blank=True)
    client_name=models.TextField(max_length=200,blank=False)
    project_cost=models.IntegerField(blank=False)
    applicant_role=models.TextField(max_length=200,blank=False)
    applicant_scope=models.TextField(max_length=200,blank=False)
    applicantWork_cost=models.IntegerField(blank=False)
    #time_limit=models.DateTimeField(blank=True)
    commencement_date=models.DateTimeField(blank=False)
    sched_completion_date=models.DateTimeField(blank=False)
    act_completion_date=models.DateTimeField(blank=False)
    proj_cost_tilldate=models.IntegerField(blank=False)
    Architect_name=models.CharField(max_length=200,blank=True)
    Structural_Consultant_name = models.CharField(max_length=200, blank=True)
    Plumbing_Consultant_name = models.CharField(max_length=200,blank=True)
    Fire_Consultant_name = models.CharField(max_length=200,blank=True)
    Landscaping_Consultant_name = models.CharField(max_length=200, blank=True)
    HVAC_Consultant_name = models.CharField(max_length=200,blank=True)
    Electrical_Consultant_name = models.CharField(max_length=200, blank=True)
    Interior_Designer_name = models.CharField(max_length=200, blank=True)
    Project_Management_Consultant_name = models.CharField(max_length=200, blank=True)
    MoEF_Consultant_name = models.CharField(max_length=200, blank=True)

    req_docs=models.FileField(upload_to="uploads/",blank=True)

    green_proj=models.CharField(max_length=1000, choices=yes_no,blank=True)
    green_project_details=models.FileField(upload_to="uploads/",blank=True)

    def __str__(self):
        return self.users_name

class Quality(models.Model):
    users_name = models.CharField(max_length=20, blank=True)
    any_system_for_coordinating_of_all_drawings=models.CharField(max_length=1000, choices=yes_no,blank=True)
    drawing_coordinating_system=models.TextField(max_length=1000, blank=True)
    PMC=models.CharField(max_length=1000, choices=yes_no,blank=True)
    drawing_specification_assessment=models.CharField(max_length=1000, choices=yes_no,blank=False)
    consultant_visit_frequency=models.IntegerField(blank=True)
    Decision_recorded=models.CharField(max_length=1000, choices=yes_no,blank=False)
    meeting_instruction_book_minute=models.FileField(upload_to="uploads/",blank=True)
    quality_standard_tender=models.CharField(max_length=1000, choices=yes_no,blank=False)
    name_of_quality_standard_approver=models.CharField(max_length=1000,blank=True)
    in_house_team_quality_control=models.CharField(max_length=1000, choices=yes_no,blank=True)
    external_team_to_control_quality=models.CharField(max_length=1000, choices=yes_no,blank=True)
    list_quality_assurance_tests_OnSite=models.TextField(max_length=100,blank=False)
    list_quality_assurance_tests_Off_Site = models.TextField(max_length=100,blank=False)
    sample_Checklist_followed=models.FileField(upload_to="uploads/",blank=True)
    sample_test_reports=models.FileField(upload_to="uploads/",blank=True)
    any_special_training_programs=models.CharField(max_length=1000, choices=yes_no,blank=True)
    If_Yes_Provide_details= models.TextField(max_length=100,blank=True)
    any_special_training_programs_workers=models.CharField(max_length=1000, choices=yes_no,blank=True)
    If_Yes_Provide_details_workers= models.TextField(max_length=100,blank=True)
    any_Supervision_from_Client_side=models.CharField(max_length=1000, choices=yes_no,blank=False)
    Any_other_system_method_mechanism_adopted=models.CharField(max_length=1000, choices=yes_no,blank=True)
    system_method_mechanism_adopted=models.TextField(max_length=100,blank=True)
    rate_your_project_in_terms_of_quality=models.IntegerField(blank=False)

    def __str__(self):
        return self.users_name

class Category(models.Model):
    users_name = models.CharField(max_length=20, blank=True)
    app_form_cat = models.CharField(choices=category_1_9,max_length=4,blank=True)

    def __str__(self):
        return self.users_name

# class CategoryChoices(models.Model):
#     app_form_cat = models.ForeignKey("Category",related_name="choices",on_delete=models.CASCADE)
#     choice = models.CharField("category_1_9", max_length=100)

#     class Meta:
#         unique_together = [
#             ("app_form_cat","choice"),
#         ]

#     def __str__(self):
#         return self.choice

# class Category(models.Model):
#     users_name = models.CharField(max_length=20, blank=True)
#     cat1 = models.CharField(max_length=100,default="off",unique=True, blank=True)
#     cat2 = models.CharField(max_length=100,default="off",unique=True, blank=True)
#     cat3 = models.CharField(max_length=100,default="off",unique=True, blank=True)
#     cat4 = models.CharField(max_length=100,default="off",unique=True, blank=True)
#     cat5 = models.CharField(max_length=100,default="off",unique=True, blank=True)
#     cat6 = models.CharField(max_length=100,default="off",unique=True, blank=True)
#     cat7 = models.CharField(max_length=100,default="off",unique=True, blank=True)
#     cat8 = models.CharField(max_length=100,default="off",unique=True, blank=True)
#     cat9 = models.CharField(max_length=100,default="off",unique=True, blank=True)

#     def __str__(self):
#         return self.users_name

class PaymentDetails(models.Model):
    users_name = models.CharField(max_length=20, blank=True)
    pay_method = models.CharField(max_length=50,blank=False)
    trans_date = models.CharField(max_length=20,blank=False)
    trans_id = models.CharField(max_length=30,blank=False)
    bank = models.CharField(max_length=50,blank=False)

    def __str__(self):
        return self.users_name





