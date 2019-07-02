from django.shortcuts import render, get_object_or_404
from .models import ReviewPost
from .forms import ReviewForm


def reviews(request):
    reviews = ReviewPost.objects.all()
    context = {'reviews':reviews}
    return render(request, 'reviews/reviews.html', context)

def review_create(request):
    form = ReviewForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        form = ReviewForm()
    context = {'form':form}
    return render(request, 'reviews/create.html', context)

def review_detail(request, review_id):
    reviewdetail = get_object_or_404(ReviewPost, pk=review_id)
    return render(request, 'reviews/detail.html', {'review':reviewdetail})

def review_update(request, review_id):
    reviewdetail = get_object_or_404(ReviewPost, pk=review_id)
    context = {'review':reviewdetail, 'form': None}
    return render(request, 'reviews/update.html', context)


def review_delete(request, review_id):
    reviewdetail = get_object_or_404(ReviewPost, pk=review_id)
    context = {'review':reviewdetail}
    return render(request, 'reviews/delete.html', context)
