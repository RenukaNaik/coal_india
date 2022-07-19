from django.shortcuts import render
from .models import CoalForm#, ProjectDetails,
from django.shortcuts import redirect
from .forms import Coalform
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.db.models import Count
from django.http import HttpResponse
import csv

# Create your views here.
def single(request,id):
    s=CoalForm.objects.get(id=id)
    # print(s)
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['id','Project name', 'Sector', 'State', 'District','Latitude','Longitude','FY','Project Status','Implementing Agency','Implementing Agency Name','Requested Amount','Approved Amount','Compendium','Picture'])
    # s.id == this will fetch id of each project--- helps in downloading excel sheet of only single project
    for project in CoalForm.objects.filter(id=s.id).values_list('id','project_name', 'sector', 'inputState', 'inputDistrict','lat','lng','fy','Projectstatus','agencytype','organisation_name','request_amount','approved_amount','commpendium','picture','submission_date'):
        if(CoalForm.objects.filter(project_name=s).latest('id')):
            writer.writerow(project)

    response['Content-Disposition'] = 'attachment; filename="project_info.csv"'

    return response
    
    # print(s)
    # return render(request,'home/download.html')
def edit(request): 
    
    data =CoalForm.objects.all() 
    # data = CoalForm.objects.get(id=id)
    # docdata  = doctor.objects.get(id=id)  
    # print(data.name)
   
    context = {
        'data':data
    }
    # return render(request,'edit.html', {'data':data}) 
    return render(request,'home/edit.html',context) 

def export(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Project name', 'Sector', 'State', 'District','Latitude','Longitude','FY','Project Status','Implementing Agency','Implementing Agency Name','Requested Amount','Approved Amount','Compendium','Picture'])

    for project in CoalForm.objects.all().values_list('project_name', 'sector', 'inputState', 'inputDistrict','lat','lng','fy','Projectstatus','agencytype','organisation_name','request_amount','approved_amount','commpendium','picture'):
        writer.writerow(project)

    response['Content-Disposition'] = 'attachment; filename="archive.csv"'

    return response

def coalIndia(request):
    # coal = ProjectDetails.objects.all()
    coalform=CoalForm.objects.all()
    s1=CoalForm.objects.filter(sector='education')
    s2=CoalForm.objects.filter(sector='healthcare')

    # print(coalform)
    # print(s1)
    
    # duplicates = CoalForm.objects.values(
    # 'inputDistrict').annotate(Count('inputDistrict')).filter(lat__gt=1)
    # print(duplicates)   #queryset
    # records = CoalForm.objects.filter(lat__in=[item['inputDistrict'] for item in duplicates])
    # print(records)
    # print([item[inputDistrict] for item in records])
    # for r in duplicates:
    #     district=r['inputDistrict']
    #     dist_count=r['inputDistrict__count']
    #     # print(r['inputDistrict'],r['inputDistrict__count'])
    #     print(district,dist_count)
# course_qs = <whatever query gave you the queryset>
# for course in course_qs:
#     print(course['course_code'])

#     dupes = Literal.objects.values('name')
#                        .annotate(Count('id'))
#                        .order_by()
#                        .filter(id__count__gt=1)
# Literal.objects.filter(name__in=[item['name'] for item in dupes])
    context = {'coal':coal,'coalform':coalform,
    
    's1':s1,'s2':s2}
    # context = {'wells': wells, 'mylist':mylist}
    return render(request, 'home/viewVatikas.html', context )


def search(request):
    # coal = ProjectDetails.objects.all()
    coalform=CoalForm.objects.all()
    s1=CoalForm.objects.filter(sector='education')
    s2=CoalForm.objects.filter(sector='healthcare')
    fy=CoalForm.objects.values_list('fy').distinct()
    date=CoalForm.objects.latest('submission_date')
    # print(date)
    # print(coalform)
    # print(s1)
    # print(fy)
    
    # duplicates = CoalForm.objects.values(
    # 'inputDistrict').annotate(Count('inputDistrict')).filter(lat__gt=1)
    # print(duplicates)   #queryset
    # records = CoalForm.objects.filter(lat__in=[item['inputDistrict'] for item in duplicates])
    # print(records)
    # print([item[inputDistrict] for item in records])
    # for r in duplicates:
    #     district=r['inputDistrict']
    #     dist_count=r['inputDistrict__count']
    #     # print(r['inputDistrict'],r['inputDistrict__count'])
    #     print(district,dist_count)
# course_qs = <whatever query gave you the queryset>
# for course in course_qs:
#     print(course['course_code'])

#     dupes = Literal.objects.values('name')
#                        .annotate(Count('id'))
#                        .order_by()
#                        .filter(id__count__gt=1)
# Literal.objects.filter(name__in=[item['name'] for item in dupes])
    context = {'coal':coal,'coalform':coalform,
    
    's1':s1,'s2':s2}
    # context = {'wells': wells, 'mylist':mylist}
    return render(request, 'home/search.html', context )



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
