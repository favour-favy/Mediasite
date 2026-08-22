from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import MediaItem, Category, Comment
from .forms import MediaItemForm, CommentForm

def gallery_view(request):
    query = request.GET.get('q', '')
    items = MediaItem.objects.all()

    if query:
        items = items.filter(title__icontains=query)

    paginator = Paginator(items, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()
    return render(request, 'gallery/gallery.html', {'page_obj': page_obj, 'categories': categories, 'query': query})

def add_media(request):
    if request.method == 'POST':
        form = MediaItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = MediaItemForm()
    return render(request, 'gallery/media_form.html', {'form': form, 'action': 'Add'})

def edit_media(request, pk):
    item = get_object_or_404(MediaItem, pk=pk)
    if request.method == 'POST':
        form = MediaItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = MediaItemForm(instance=item)
    return render(request, 'gallery/media_form.html', {'form': form, 'action': 'Edit'})

def delete_media(request, pk):
    item = get_object_or_404(MediaItem, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('gallery')
    return render(request, 'gallery/media_confirm_delete.html', {'item': item})

def media_detail(request, pk):
    item = get_object_or_404(MediaItem, pk=pk)
    comments = item.comments.all().order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.media_item = item
            comment.save()
            return redirect('media_detail', pk=item.pk)
    else:
        form = CommentForm()

    return render(request, 'gallery/media_detail.html', {'item': item, 'comments': comments, 'form': form})