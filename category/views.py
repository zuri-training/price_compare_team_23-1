from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from .models import Product
from .forms import CommentForm
from .scraper.jumia import get_jumia_product
from .scraper import jumia, scraper, konga, asos
from django.db.models import Q
from django.views.generic import ListView
import random
from .product import populatedB, get_konga_product
import time
# import schedule

#  ************product views*****************

#  takes into consideration:
#   @ Details about the product
#   @ Products Listing when potential customers make a search
#   @ Results of the search made by the customers

def faq_view(request):
    
    return render(request, 'category/faq.html')

def index_view(request):
    products = Product.objects.all()[12:18]
    top = Product.objects.all()[0:1]
    context = {
        'products': products,
        'top': top
    }
    return render(request, 'category/index.html',context)

def contact_page(request):
    return render(request, 'category/contact.html')

def product_detail(request, id, product):
    product = get_object_or_404(
        Product,
        slug=product,
        id=id,
    )

    comments = product.comments.filter(active=True)
    new_comment = None
    prd = {
        "name": product.name,
        "brand": product.brand,
        "category": product.category,
    }
    platforms = []
    platforms.append(get_jumia_product(prd))
    #platforms.append(get_konga_product(prd))
    # print(platform)

    if request.method == "POST":
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.product = product
            new_comment.username = request.user.username
            new_comment.save()
            return HttpResponseRedirect(
                f"{product.slug}",
                {
                    "product": product,
                    "comments": comments,
                    "platforms": platforms,
                    "new_comment": new_comment,
                    "comment_form": comment_form,
                },
            )
    else:
        comment_form = CommentForm()

    return render(
        request,
        "product/detail.html",
        {
            "product": product,
            "comments": comments,
            "platforms": platforms,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )


class ProductListView(ListView):
    model = Product
    #populatedB()
    context_object_name = "products"
    template_name = "product/list.html"


class SearchResultView(ListView):
    model = Product
    template_name = "product/search_result.html"
    context_object_name = "products"

    def get_queryset(self):
        query = self.request.GET.get("search")
        list = Product.objects.filter(
            Q(name__icontains=query) | Q(category__icontains=query)
        )
        return list


def user_search(request):
    if request.GET.get("search"):
        q = request.GET.get("search")
        products = []
        #products.extend(asos.asos_scraper_bot(q))
        products.extend(scraper.jumia_scraper_bot(q))
        # products.extend(jumia.jumia_scraper_bot(q))
        # products.extend(konga.konga_scraper_bot(q))
        # products.extend(payporte.payporte_scraper_bot(q))
        # random.shuffle(products)
        for i in range(len(products)):

            objects = Product.objects.create(
                brand=products[i]["brand"],
                price=products[i]["price"],
                # vendor=products[i]["from"],
                image_src=products[i]["image"],
                name=products[i]["name"],
                category=products[i]["category"],
            )
            objects.save()
        return render(request, "product/user_search.html", {"products": products})

    else:
        products = Product.objects.all()

        return render(request, "product/user_search.html", {"products": products})