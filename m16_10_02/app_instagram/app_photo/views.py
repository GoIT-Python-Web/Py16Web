from pathlib import Path

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .forms import PictureForm
from .models import Picture


# Create your views here.

def index(request):
    return render(request, 'app_photo/index.html', context={"msg": "Hello world!"})


@login_required
def pictures(request):
    pics = Picture.objects.filter(user=request.user).all()
    return render(request, 'app_photo/pictures.html', context={"pics": pics})


@login_required
def upload(request):
    form = PictureForm(instance=Picture())
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES, instance=Picture())
        if form.is_valid():
            pic = form.save(commit=False)
            pic.user = request.user
            pic.save()
            return redirect(to="app_photo:pictures")
    return render(request, 'app_photo/upload.html', context={"form": form})


@login_required
def edit(request, pic_id):
    if request.method == 'POST':
        desc = request.POST.get('description')
        Picture.objects.filter(pk=pic_id, user=request.user).update(description=desc)
        return redirect(to="app_photo:pictures")
    pic = Picture.objects.filter(pk=pic_id, user=request.user).first()
    return render(request, 'app_photo/edit_desc.html', context={"pic": pic})


@login_required
def remove(request, pic_id):
    pic = Picture.objects.filter(pk=pic_id, user=request.user)
    file_path: Path = settings.MEDIA_ROOT / str(pic.first().path)
    if file_path.exists():
        file_path.unlink()
        pic.delete()
        print('Removed file')
    else:
        print('File ont removed')

    return redirect(to="app_photo:pictures")
