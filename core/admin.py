from django.contrib import admin

from .models.bamazon import Author, Tag, Book



class AuthorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [
                            'first_name',
                            'last_name',
                            'middle_name',
                            'birth_date',
                            'death_date',
                            'image',
                            'bio',
                ]}
        ),
    ]
    search_fields = ['last_name', 'desc']

admin.site.register(Author, AuthorAdmin)


class TagAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [
                            'title',
                            'desc',
                ]}
        ),
    ]
    search_fields = ['title']

admin.site.register(Tag, TagAdmin)


class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [
                            'authors',
                            'tags',
                            'title',
                            'desc',
                            'price',
                            'pub_date',
                ]}
        ),
    ]
    list_filter = ['pub_date']
    search_fields = ['authors', 'tags', 'title', 'desc', 'pub_date']

admin.site.register(Book, BookAdmin)
