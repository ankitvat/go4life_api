from rest_framework import routers
from leads import views as leads_views

router = routers.DefaultRouter()
router.register(r"leads", leads_views.LeadView)
