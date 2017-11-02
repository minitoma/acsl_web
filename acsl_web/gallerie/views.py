from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Photo

# Create your views here.

def gallerie_list(request):
    gallerie = Media.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'gallerie/gallerie_list.html', {'gallerie': gallerie})

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'gallerie/photo_detail.html', {'photo': photo})
