from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from team.models import Team
from banner.models import Banner
from slider.models import Slider
from blogs.models import Blogs
from testimonial.models import Testimonial
from mainblog.models import MainBlog
from savecontact.models import saveContact
from indexpurifier.models import indexPurifier
from indexcamera.models import indexCamera

def  index(request):
    purifierData  = indexPurifier.objects.all()[0:6]
    cameraData  = indexCamera.objects.all()[0:6]
    bannerData = Banner.objects.all()
    sliderData = Slider.objects.all()
    testimonialData = Testimonial.objects.all()
    data = {
        'bannerData': bannerData,
        'sliderData': sliderData,
        'testimonialData':testimonialData,
        'purifierData': purifierData,
        'cameraData': cameraData,
    }
    return render(request,'index.html',data)



def  base(request):
    bannerData = Banner.objects.all()
    data = {
        'bannerData': bannerData,
    }
    return render(request,'base.html',data)

def contact(request):
        return render(request, 'contact.html')

def savecontact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        message=request.POST.get('message')

        saved = saveContact(s_name=name,s_contact=contact,s_email=email,s_message=message)
        saved.save()
        show = 'data inserted'


    return render (request,'contact.html',{'success':True})


def blog_three_columns(request):
    blogData = Blogs.objects.all()
    mainblogData = MainBlog.objects.all()
    data={
        'blogData':blogData,
        'mainblogData':mainblogData,
    }
    return render(request, 'blog.html',data)

def aboutus(request):
    return render(request, 'aboutus.html')

def testimonials(request):
    testimonialData = Testimonial.objects.all()
    data={
        'testimonialData':testimonialData,
    }
    return render(request, 'testimonials.html',data)

def products(request):
    return render(request, 'products.html')

def team(request):

    teamData = Team.objects.all().order_by('team_name')[0:4]
    data = {
        'teamData': teamData,
    }

    return render(request, 'team.html',data)