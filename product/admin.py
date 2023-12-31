from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from product.models import Category, Comment, Product, Images

class ProductImagesInline(admin.TabularInline):
    model = Images
    extra = 5
    readonly_fields = ('image_tag',)
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']
    # fields = ['status']
    prepopulated_fields = {"slug": ("title",)}  #! new

class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',) #! Alt başlıklar.
    prepopulated_fields = {'slug': ('title',)} #! Kategori adı yazılırken alt kısımdaki slug kısmını otomatik oluşturan kod.

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'

# admin.site.register(Category,MPTTModelAdmin)
admin.site.register(Category,CategoryAdmin2)

class ProductAdmin(admin.ModelAdmin):
    # fields = ['title', 'status'] == 
    list_display = ['title', 'category','image_tag']
    list_filter = ['status','category']
    readonly_fields = ('image_tag',) 
    inlines = [ProductImagesInline]
admin.site.register(Product, ProductAdmin)

class ImagesAdmin(admin.ModelAdmin):
    # fields = ['title', 'status']
    list_display = ['title','product', 'image_tag']
admin.site.register(Images, ImagesAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject','comment', 'status','create_at']
    list_filter = ['status']
    readonly_fields = ('subject','comment','ip','user','product','rate','id')

admin.site.register(Comment, CommentAdmin)