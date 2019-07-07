from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import ReviewPost
from .forms import ReviewForm


def reviews(request):
    reviews = ReviewPost.objects.all()
    context = {'reviews':reviews}
    return render(request, 'reviews/reviews.html', context)

# @login_required
@staff_member_required
def review_create(request):
    form = ReviewForm(request.POST or None, request.FILES)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = ReviewForm()
        return redirect("/reviews")
    context = {'form':form}
    return render(request, 'reviews/form.html', context)

def review_detail(request, review_id):
    reviewdetail = get_object_or_404(ReviewPost, pk=review_id)
    return render(request, 'reviews/detail.html', {'review':reviewdetail})

@staff_member_required
def review_update(request, review_id):
    obj = get_object_or_404(ReviewPost, pk=review_id)
    form = ReviewForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/reviews")
    context = {'form': form, "title": f"Update {obj.title}"}
    return render(request, 'reviews/form.html', context)

@staff_member_required
def review_delete(request, review_id):
    reviewdetail = get_object_or_404(ReviewPost, pk=review_id)
    if request.method == "POST":
        reviewdetail.delete()
        return redirect("/reviews")
    context = {'review':reviewdetail}
    return render(request, 'reviews/delete.html', context)
