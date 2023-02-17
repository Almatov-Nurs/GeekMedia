from django.contrib import admin
from .models import Posts, Articles, Category, MultiMedia

admin.site.register(Posts)
admin.site.register(Articles)
admin.site.register(Category)
admin.site.register(MultiMedia)
