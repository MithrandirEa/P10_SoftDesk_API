from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminAuthenticated(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and
                    request.user.is_authenticated and
                    request.user.is_superuser)


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj == request.user


class IsAuthorOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class IsProjectContributor(BasePermission):

    def has_object_permission(self, request, view, obj):
        # Détermine le projet parent selon le type d'objet
        project = None

        # 1. Si l'objet est un Projet (ProjectViewSet)
        # Note : adaptez selon le nom exact de votre modèle Project
        if hasattr(obj, 'contributor_set'):
            project = obj
        # 2. Si l'objet est une Issue (IssueViewSet -> project)
        elif hasattr(obj, 'project'):
            project = obj.project

        # 3. Si l'objet est un Commentaire (CommentViewSet -> issue -> project)
        elif hasattr(obj, 'issue'):
            project = obj.issue.project

        if project:
            # Vérifie l'existence dans la table intermédiaire
            return project.contributor_set.filter(user=request.user).exists()

        return False
