import urlparse


def _validate_next_redirect_parameter(request, next_redirect):
    """
    Validate the next_redirect url and return the path if ok, else None
    """
    parsed = urlparse.urlparse(next_redirect)
    if parsed and parsed.path:
        return parsed.path
    return None


def get_next_redirect(request):
    """
    Find the next_redirect url to redirect
    """
    next_redirect = getattr(request, 'POST', {}).get('nr',
                        getattr(request, 'GET', {}).get('nr',
                            getattr(request, 'META', {}).get('HTTP_REFERER', None)))
    if next_redirect:
        next_redirect = _validate_next_redirect_parameter(request,
                                                          next_redirect)
    if not next_redirect:
        next_redirect = getattr(request, 'path', None)
    return next_redirect
