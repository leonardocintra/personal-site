from django.contrib import admin
from .models import Site

class SiteModelAdmin(admin.ModelAdmin):
	search_fields = ('titulo', )

	class Meta:
		model = Site


admin.site.register(Site, SiteModelAdmin)