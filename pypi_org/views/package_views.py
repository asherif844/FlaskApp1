import flask 
import sys
sys.path.append('pypi_org/services')
from services import package_services

blueprint = flask.Blueprint('packages', __name__, template_folder = 'templates')

@blueprint.route("/project/<package_name>")
def package_details(package_name: str):
    return "Package details for {}".format(package_name)

@blueprint.route("/<int:rank>")
def popular(rank: int):
    print(type(rank), rank)
    return "The details for {}th most popular package".format(rank)