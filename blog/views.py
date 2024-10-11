from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm



def post_list(request):
    posts = Post.objects.all().order_by('-created_on')
    paginator = Paginator(posts, 6)  # Show 6 posts per page
    
    page = request.GET.get('page', 1)  # Get the page number from the request
    try:
        posts = paginator.page(page)  # Get the posts for the page
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, deliver the last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post_list.html', {'posts': posts})



@login_required
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all().order_by('-created_on')
    comment_count = comments.count()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', slug=post.slug)
        else:
            messages.error(request, 'Error submitting comment')
    else:
        form = CommentForm()

    return render(
        request,
        'blog/post_detail.html',
        {
            'post': post,
            'comments': comments,
            'comment_count': comment_count,
            'form': form
        }
    )

@login_required
def comment_edit(request, slug, comment_id):
    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid() and comment.author == request.user:
            form.save()
            messages.success(request, 'Comment updated!')
        else:
            messages.error(request, 'Error updating comment.')
        return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm(instance=comment)
    
    return render(
        request,
        'blog/comment_edit.html',
        {
            'form': form,
            'post': post,
            'comment': comment
        }
    )

@login_required
def comment_delete(request, slug, comment_id):
    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted.')
    else:
        messages.error(request, 'You can only delete your own comments.')
    
    return redirect('post_detail', slug=post.slug)


