from django.shortcuts import render

# from catalog.models import Book, Category
# from django.db.models import Q, Value, DecimalField, F
#
# Book.objects.filter(price__lt=500)
# Book.objects.filter(stock=0)
#
# Book.objects.filter(
#     Q(title__icontains="django") | Q(author__icontains="django")
# )
#
# Book.objects.filter(
#     Q(price__gt=100) | Q(stock__lt=5)
# )
#
# Book.objects.annotate(
#     price_with_fee=F("price") + Value(
#         10,
#         output_field=DecimalField(max_digits=10, decimal_places=2),
#     )
# )