"""
URL configuration for SoftDesk_API project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework import routers
from rest_framework_nested import routers as nested_routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# from SoftDesk_API.views import api_root
from Users.views import (AdminUserViewSet, UserViewSet)
from Projects.views import (ProjectViewSet, AdminProjectViewSet, IssueViewSet, CommentViewSet)

# ---- ROUTER DE L'API ----
router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('projects', ProjectViewSet, basename='project')

# Router imbriqué pour les issues d'un projet
projects_router = nested_routers.NestedSimpleRouter(router,
                                                    'projects',
                                                    lookup='project')
projects_router.register('issues', IssueViewSet, basename='project-issues')

# Router imbriqué pour les commentaires d'une issue
issues_router = nested_routers.NestedSimpleRouter(projects_router,
                                                  'issues',
                                                  lookup='issue')
issues_router.register('comments', CommentViewSet,
                       basename='issue-comments')


# ----------- ADMIN ROUTERS -----------
router.register('admin/users',
                AdminUserViewSet,
                basename='admin-user')
router.register('admin/projects',
                AdminProjectViewSet,
                basename='admin-project')



# TODO: Ajouter les router admin/user, admin/project, admin/project/users, admin/project/issues, admin/project/comments,etc.. !!! A REFLECHIR

urlpatterns = [
    path('', RedirectView.as_view(url='/api/', permanent=False), name='root'),
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    # path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
    path('api/', include(projects_router.urls)),
    path('api/', include(issues_router.urls)),

]
