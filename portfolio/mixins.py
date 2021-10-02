from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer


class AdminOnlyBrowsableAPIMixin:
    """
    Mixin to allow `BrowseableAPIRenderer` to admin only.
    """

    def get_renderers(self):
        rends = [JSONRenderer]
        if self.request.user and self.request.user.is_superuser:
            rends.append(BrowsableAPIRenderer)
        return [renderer() for renderer in rends]
