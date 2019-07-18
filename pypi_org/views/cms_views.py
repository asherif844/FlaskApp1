import sys

import flask

from services import cms_service as cms_service

sys.path.append('pypi_org/services')

blueprint = flask.Blueprint('cms', __name__, template_folder = 'templates')

@blueprint.route('/<path:full_url>')
def cms_page(full_url: str):
    print('Getting CMS page for {}'.format(full_url))

    page = cms_service.get_page(full_url)
    if not page:
        return flask.abort(404)
    # return page
    return flask.render_template('cms/about.html', packages=page)
