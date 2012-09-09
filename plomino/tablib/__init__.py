from zope import component
from Products.CMFPlomino import interfaces
from zope.interface import implements

# TODO: support more of these:
# from tablib import Databook, Dataset, detect, import_set, InvalidDatasetType, InvalidDimensions, UnsupportedFormat

from tablib import Dataset

from Products.PythonScripts.Utility import allow_module, allow_class

allow_module('plomino.tablib')
allow_class(Dataset)

def dataset(data, headers=None):
    dataset = Dataset()
    dataset.dict = data
    if headers:
        dataset.headers = headers
    return dataset

class PlominoTablibUtils:
    implements(interfaces.IPlominoUtils)

    module = 'plomino.tablib'
    methods = ['dataset']

component.provideUtility(PlominoTablibUtils, interfaces.IPlominoUtils)

def initialize(context):
    """Initializer called when used as a Zope 2 product."""

