from django.shortcuts import get_object_or_404, render
from .forms import AddVideoForm
from .models import Video
from django.contrib.auth import logout


def index(request):
    all_videos = Video.objects.all().order_by('-pk')

    context = {'all_videos': all_videos
               }

    return render(request, 'index.html', context)

def add(request):
    if request.method == 'POST':
        form = AddVideoForm(request.POST)
        if form.is_valid():
            saved_form = form.save(commit=False)
            saved_form.save()
            video_record = get_object_or_404(Video, pk=saved_form.id)
            message = "Record saved!"
            context = {'video_record': video_record,
                       'message': message
                }
            return render(request, 'detail.html', context)
        else:
            form_errors = form.errors
            context = {'form': form,
                       'form_errors': form_errors
                       }
            return render(request, 'add.html', context)
    else:
        form = AddVideoForm()
        context = {'form': form}
        return render(request, 'add.html', context)


def edit(request, video_id):
    video_to_edit = get_object_or_404(Video, pk=video_id)
    if request.method == 'POST':
        form = AddVideoForm(request.POST, request.FILES or None, instance=video_to_edit)
        if form.is_valid():
            saved_form = form.save(commit=False)
            saved_form.save()
            video_record = get_object_or_404(Video, pk=saved_form.id)
            message = "Record saved!"
            context = {'video_record': video_record,
                       'message': message
                }
            return render(request, 'detail.html', context)
        else:
            form_errors = form.errors
            context = {'form': form,
                       'form_errors': form_errors
                       }
            return render(request, 'add.html', context)
    else:
        form = AddVideoForm(instance=video_to_edit)
        context = {'form': form}
        return render(request, 'edit.html', context)

def logout_view(request):
    logout(request)
    all_videos = Video.objects.all().order_by('-pk')

    context = {'all_videos': all_videos
               }

    return render(request, 'index.html', context)
