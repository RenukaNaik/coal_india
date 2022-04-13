from django.shortcuts import render
from .models import CoalForm#, ProjectDetails,
from django.shortcuts import redirect
from .forms import Coalform
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

# Create your views here.
def edit(request, id):  
    data = CoalForm.objects.get(id=id)
    # docdata  = doctor.objects.get(id=id)  
    # print(data.name)
   
    context = {
        'data':data
    }
    # return render(request,'edit.html', {'data':data}) 
    return render(request,'home/edit.html',context) 

def coalIndia(request):
    # coal = ProjectDetails.objects.all()
    coalform=CoalForm.objects.all()
    context = {'coal':coal,'coalform':coalform}
    # context = {'wells': wells, 'mylist':mylist}
    return render(request, 'home/viewVatikas.html', context )

def coal(request):
    # form = Coalform()
    if request.method == 'POST':
        form = Coalform(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            instance.user = request.user
            instance.save()
            print("data is saved.")
            return redirect('/coal')
    else:
        form = Coalform()
    return render(request,"home/coal.html",{'form': form})


# def coal(request):
#     form = Coalform()
#     if request.method == 'POST':
#         form = Coalform(request.POST, request.FILES)
#         # if form.is_valid():
#         #     form.save()
#         # name = request.POST.get('name')
#         # form = CoalForm(request.POST, request.FILES)
#         project_name = request.POST.get('project_name')
#         inputState=request.POST.get('inputState')
#         inputDistrict=request.POST.get('inputDistrict')
#         fy=request.POST.get('fy')
#         Projectstatus=request.POST.get('Projectstatus')
#         agencytype=request.POST.get('agencytype')
#         organisation_name=request.POST.get('organisation_name')
#         tender_receipt=request.POST.get('tender_receipt')
#         sector=request.POST.get('sector')
#         request_amount=request.POST.get('request_amount')
#         approved_amount=request.POST.get('approved_amount')
#         # security_completion=request.POST.get('security_completion')
#         # submission=request.POST.get('submission')
#         # receipt=request.POST.get('receipt')
#         # agenda_completion=request.POST.get('agenda_completion')
#         # committee_review=request.POST.get('committee_review')
#         # gm_csr_sign_off=request.POST.get('gm_csr_sign_off')
#         # legal_security=request.POST.get('legal_security')
#         # office_orfder_creation=request.POST.get('office_orfder_creation')
#         # finance=request.POST.get('finance')
#         # fund_disbursal=request.POST.get('fund_disbursal')
#         # first_release_ack=request.POST.get('first_release_ack')
#         # final_release_ack=request.POST.get('final_release_ack')
#         # vetting_by_dp=request.POST.get('vetting_by_dp')
#         # vetting_by_df=request.POST.get('vetting_by_df')
#         # chairman_approval=request.POST.get('chairman_approval')
#         # csr_sd_committee_review=request.POST.get('csr_sd_committee_review')
#         # cil_board_review=request.POST.get('cil_board_review')
#         # fcbc_completion=request.POST.get('fcbc_completion')
#         # mou_finalisation=request.POST.get('mou_finalisation')
#         lat=request.POST.get('lat')
#         lng=request.POST.get('lng')
#         picture=request.POST.get('picture')
#         coal = CoalForm.objects.create(project_name = project_name,inputState=inputState,inputDistrict=inputDistrict,
#         fy=fy,Projectstatus=Projectstatus,agencytype=agencytype,organisation_name=organisation_name,lat=lat,lng=lng,
#         tender_receipt=tender_receipt, sector=sector,request_amount=request_amount,approved_amount=approved_amount,picture=picture)
#         # security_completion=security_completion,submission=submission,receipt=receipt,agenda_completion=agenda_completion,
#         # committee_review=committee_review,gm_csr_sign_off=gm_csr_sign_off,legal_security=legal_security,office_orfder_creation=office_orfder_creation,
#         # finance=finance,fund_disbursal=fund_disbursal,first_release_ack=first_release_ack,final_release_ack=final_release_ack,
#         # vetting_by_dp=vetting_by_dp,vetting_by_df=vetting_by_df,chairman_approval=chairman_approval,csr_sd_committee_review=csr_sd_committee_review,
#         # cil_board_review=cil_board_review,fcbc_completion=fcbc_completion,mou_finalisation=mou_finalisation)
#         coal.save()
#         messages.info(request, _(u'Your data is submitted successfully!'))
#         # return HttpResponseRedirect(request.path_info)
#         return redirect('/coal')
           
#     else:
#         form = CoalForm()
#     return render(request,'home/coal.html',{})
