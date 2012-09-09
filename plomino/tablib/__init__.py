from tablib import Databook, Dataset, detect, import_set, import_book, InvalidDatasetType, InvalidDimensions, UnsupportedFormat

from Products.PythonScripts.Utility import allow_module 
allow_module('plomino.tablib')

class PlominoTablib:
    module = 'plomino.tablib'
    methods = ['Databook', 'Dataset', 'detect', 'import_set',
            'import_book', 'InvalidDatasetType', 'InvalidDimensions',
            'UnsupportedFormat', ]

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
