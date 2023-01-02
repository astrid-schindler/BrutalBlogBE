from django.contrib import admin

# Register your models here.
from BrutalBlogAdmin.models import Blogpost


@admin.register(Blogpost)
class ProfileAdmin(admin.ModelAdmin):
    model = Blogpost
    date_hierarchy = "publish_date"
    save_on_top = True

    list_display = (
        "id_post",
        "title",
        "slug",
        "publish_date",
        "published",
        "author",
    )



