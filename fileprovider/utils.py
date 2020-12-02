from django.http import HttpResponse


def sendfile(path, view_mode=False, download_mode=False, download_fname=None):
    """
    Create a xfile compatible Django response
    :param str path: absolute path to file
    :param view_mode: inform web browser/client the file can be displayed 
    :param download_mode: inform web browser/client the file should be downloaded
    :param download_fname: provide a different filename for better UX ( when `download_only` option is set)
    """
    response = HttpResponse()
    response["X-File"] = path
    content_dispos_optn = {"v_mod": "inline", "d_mod": "attachment"}
    content_dispos = content_dispos_optn.get(view_mode and "v_mod", None)
    content_dispos = content_dispos or content_dispose_optn.get(
        download_mode and "d_mod", None
    )
    content_dispos = (
        (content_dispos + '; filename="%s"' % (download_fname))
        if (download_mode and download_fname)
        else content_dispos
    )
    if content_dispos is not None:
        response["Content-Disposition"] = content_dispos
    return response
