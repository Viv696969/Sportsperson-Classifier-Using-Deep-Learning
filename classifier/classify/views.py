from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from classify import tools
import os
from .models import *
import random



def home(request):
    tools.load_objects()
    test_images=list(Test_Image.objects.all())
    image_list=[]
    for i in range(4):
            image_list.append(random.choice(test_images))
    
    context={'images':image_list}
    if request.method=='GET':
        context['new']=True
        return render(request,'home.html',context)
    else:
        imgurl=request.POST['imgurl']
    
        path=f"./{imgurl}"
        probablities,name=tools.classify_image(path)
        if name ==False:
            
            return render(request,'home.html',context)
    
        context['name']=name[0]
        
        probablity=tuple(zip(tools.classes.tolist(),probablities[0].tolist()))
       
        context['probablity']=probablity
        return render(request,'home.html',context)

def predict_by_user(request):
        tools.load_objects()
        if request.method=='POST':
            context={}
            img=request.FILES.get('user_upload_image')
            # create object of file system storage
            fs=FileSystemStorage()
            fs.save(img.name,img)
            path=f'./media/{img.name}'
            probablities,name=tools.classify_image(path)
            if name ==False:
                
                return render(request,'home.html',context)
        
            context['name']=name[0]
            
            probablity=tuple(zip(tools.classes.tolist(),probablities[0].tolist()))
         
            context['probablity']=probablity
            
            os.remove(path)
            
            return render(request,'userimage.html',context)
        else:
            context={'new':True}
            return render(request,'userimage.html',context)
        
    
