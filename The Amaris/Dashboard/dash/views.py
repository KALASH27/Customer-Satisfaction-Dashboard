from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import logout as dj_logout
from .models import Cus_Res
from django.contrib import messages

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'dash.html')
    else:
        return redirect('login')


def logout(request):
    dj_logout(request)
    return redirect('login')


def entry(request):
    if request.user.is_authenticated:
        return render(request,'entry.html')
    else:
        return redirect('login')


def add(request):
    if request.user.is_authenticated:
        try:
            cus_name=request.POST['cus_name']
            checkin=request.POST['checkin']
            checkout=request.POST['checkout']
            eoob=request.POST['eoob']
            ws=request.POST['ws']
            fd=request.POST['fd']
            das=request.POST['das']
            inout=request.POST['inout']
            clean=request.POST['clean']
            os=request.POST['os']
            sat=request.POST['sat']
            n=10000+len(Cus_Res.objects.all())
            if(checkin<checkout):
                res=Cus_Res(id=n+1, Cus_name=cus_name, Checkin=checkin, Checkout=checkout, Easeofonlinebooking=eoob, wifi_Service=ws, FoodDrinks=fd, DepartureArrivalConvinience=das, Checkinoutservice=inout, Cleanliness=clean, OtherServices=os, Satisfication=sat)
                res.save()
                messages.success(request,"Your entry successfully saved")
            else:
                messages.error(request,"Check-in date must be before checkout date bla bla bla")
        except Exception as e:
            messages.error(request,str(e))
        finally:
            return render(request,'entry.html')
    else:
        return redirect('login')


def data(request):
    if request.user.is_authenticated:
        res=Cus_Res.objects.all()
        data={'Res':res}
        return render(request,'datatable.html',data)
    else:
        return redirect('login')



def viewres(request,myid):
    if request.user.is_authenticated:
        try:
            res=Cus_Res.objects.get(id=myid)
            response={'res':res}
            return render(request,"viewres.html",response)
        except Exception as e:            
            messages.error(request,str(e))
            return redirect('table')
            
    else:
        return redirect('login')


def deldata(request):
    if request.user.is_authenticated:
        res=Cus_Res.objects.all()
        k=0
        for i in range(1,len(res)+1):
            st="ch"+str(10000+i)
            if((request.GET.get(st,'off')) == 'on'):
                print('hello')
                delres=Cus_Res.objects.filter(id=i+10000)
                delres.delete()
                k=k+1
                if k==1:
                    messages.success(request,"Data successfully deleted")
        print(request.GET.get(st,"OFF"), st)
        return redirect('table')
    else:
        return redirect('login')


def charts(request):
    if request.user.is_authenticated:
        res=Cus_Res.objects.all()
        n=len(res)
        sat=0
        dis=0
        neu=0
        hs=0
        hd=0
        eob=0
        ws=0
        fd=0
        dac=0
        cio=0
        cl=0
        os=0
        for i in range(10001,10001+n):
            cus=Cus_Res.objects.filter(id=i).values()
            for resp in cus:
                eob=eob+resp['Easeofonlinebooking']
                ws=ws+resp['wifi_Service']
                fd=fd+resp['FoodDrinks']
                dac=dac+resp['DepartureArrivalConvinience']
                cio=cio+resp['Checkinoutservice']
                cl=cl+resp['Cleanliness']
                os=os+resp['OtherServices']
                if(resp['Satisfication']=='Satisfied'):
                    sat=sat+1
                elif(resp['Satisfication']=='Dissatisfied'):
                    dis=dis+1
                elif(resp['Satisfication']=='Neutral'):
                    neu=neu+1
                elif(resp['Satisfication']=='Highly satisfied'):
                    hs=hs+1
                else:
                    hd=hd+1
        eobp=eob/15000*100
        dacp=dac/15000*100
        ciop=cio/15000*100
        wsp=ws/15000*100
        fdp=fd/15000*100
        clp=cl/15000*100
        osp=os/15000*100
        satis={'sat':sat,'dis':dis,'neu':neu,'hs':hs,'hd':hd,'eobp':eobp,'wsp':wsp,'fdp':fdp,'dacp':dacp,'ciop':ciop,'clp':clp,'osp':osp}
        return render(request,'charts.html',satis)
    else:
        return redirect('login')
