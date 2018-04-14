# -*- coding: utf-8 -*-
"""pyahp.errors

This module contains the errors which are raised by this package.
"""


class AHPModelError(Exception):
    """Base class for exceptions in this module."""
    pass


class AHPFieldEmptyError(AHPModelError):
    def __init__(self, var):
        self.var = var

    def __str__(self):
        return 'Field {} should not be empty'.format(self.var)


class AHPTypeMismatchError(AHPModelError):
    def __init__(self, var, expected, actual, list_elements=False):
        self.var = var
        self.expected = expected
        self.actual = actual
        self.list_elements = list_elements

    def __str__(self):
        if self.list_elements:
            return 'Expected {} list to have <{}> elements, got <{}>'.format(self.var, self.expected, self.actual)
        else:
            return 'Expected {} to be of type <{}>, got <{}>'.format(self.var, self.expected, self.actual)


class AHPContainsDuplicateError(AHPModelError):
    def __init__(self, var):
        self.var = var

    def __str__(self):
        return 'Field {} contains duplicates'.format(self.var)


class AHPNonSquarePreferenceMatrixError(AHPModelError):
    def __init__(self, kind, name, side, actual_width, actual_height):
        self.kind = kind
        self.name = name
        self.side = side
        self.actual_width = actual_width
        self.actual_height = actual_height

    def __str__(self):
        return 'Expecting {0}:{1} preference matrix to be {2}x{2} got {3}x{4}'.format(self.kind, self.name, self.side,
                                                                                      self.actual_width,
                                                                                      self.actual_height)


class AHPMissingPreferenceMatrixError(AHPModelError):
    def __init__(self, kind, name):
        self.kind = kind
        self.name = name

    def __str__(self):
        return 'Missing {} preference matrix for {}'.format(self.kind, self.name)
