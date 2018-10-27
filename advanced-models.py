# covers aspects of advanced model use cases in django

###------xporting django models to a csv file---##
# pip install django-import-export
# inside installed apps setting, add 'import_export',
# inside the admin.py
from django.contrib import admin
from .models import View
from import_export.admin import ImportExportModelAdmin
from .models import Book

admin.site.register(View)
#or @admin.resgister(View)
#b = Book.objects.get(id=50)
#b.title, b.author, etc

class ViewAdmin(ImportExportModelAdmin):
    pass
# go over to the admin site and under the model you will see an 'export' button

website = models.URLField() !!!
email = models.EmailField()
publication_date = models.DateField()

# accessing foreign key values
to get a list of books for a given publisher,
>>p = Publisher.objects.get(name='apress publishing')
>>p.book_set.all()

book_set is just a QuerySet and it can be filtered and sliced like any other QuerySet.
>>p = Publisher.objects.get(name='Apress Publishing')
>>p.book_set.filter(title__icontains='django')

The attribute name 'book_set' is generated by appending lower case model name to _set.

# accessing many to many values
Many to many values work like foreign key values, except we use QuerySetvalues instead of model instances.
b = Books.objects.get(id=50)
b.authors.all()     # fetch the queryset first
b.authors.filter(first_name='adam')

This also works in reverse. To view all the books for an author:
a = Author.objects.get(first_name='adrian')
a.book_set.all()
b.authors.filter(first_name='adam')









































