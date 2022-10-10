from django.shortcuts import render,redirect
from .models import review
from .forms import ReviewForm

# Create your views here.


def index(request):

    review_title = "TEST"
    movie_title = "DATA"
    content = "입니다."


    return render(request,'app/index.html')

def create(request):
    
    if request.method == 'POST':
        # DB에 저장하는 로직
        Review_form = ReviewForm(request.POST)
        if Review_form.is_valid():
            Review_form.save()
            return redirect('app:index')
    else: 
        Review_form = ReviewForm()
    context = {
        'Review_form': Review_form
    }
    return render(request, 'app/new.html', context=context)


def detail(request):

    reviews = review.objects.order_by('-pk')
    # Template에 전달한다. 
    context = {
        'reviews': reviews
    }
    
    return render(request, 'app/review.html', context)

def delete(request,pk):

    reviews = review.objects.get(pk=pk)
    reviews.delete()
    
    return redirect('app:review')


def update(request,pk):
    review_to_edit = review.objects.get(pk=pk)
    if request.method == 'POST':
        # POST : input 값 가져와서, 검증하고, DB에 저장
        review_form = ReviewForm(request.POST, instance=review_to_edit)
        if review_form.is_valid():
            # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
            review_form.save()
            return redirect('app:review')
        # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 article_form을 랜더링
    else:
        # GET : Form을 제공
        review_form = ReviewForm(instance=review_to_edit)
    context = {
        'review_form': review_form,
        'pk':pk
    }
    return render(request, 'app/update.html', context)
    


   
   