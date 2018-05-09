# -*- coding: utf-8 -*-
"""pyahp.errors

This module contains the errors which are raised by this package.
"""


class AHPModelError(Exception):
    """Base class for exceptions in this module."""
    pass


class AHPMethodUnsupportedError(AHPModelError):
    """Error for cases when the AHP model uses a method not implemented."""
    def __init__(self, expected, actual):
        self.expected = expected
        self.actual = actual

    def __str__(self):
        return 'Expected method to be one of [{}], got \'{}\''.format(self.expected, self.actual)


class AHPFieldEmptyError(AHPModelError):
    """Error for cases when the AHP model has an empty field."""
    def __init__(self, var):
        self.var = var

    def __str__(self):
        return 'Field \'{}\' should not be empty'.format(self.var)


class AHPTypeMismatchError(AHPModelError):
    """Error for cases when the properties in the AHP model don't match the expected type."""
    def __init__(self, var, expected, actual, list_elements=False):
        self.var = var
        self.expected = expected
        self.actual = actual
        self.list_elements = list_elements

    def __str__(self):
        if self.list_elements:
            return 'Expected \'{}\' list to have <{}> elements, got <{}>'.format(self.var, self.expected, self.actual)
        else:
            return 'Expected \'{}\' to be of type <{}>, got <{}>'.format(self.var, self.expected, self.actual)


class AHPContainsDuplicateError(AHPModelError):
    """Error for cases when the properties in the AHP model have duplicate entries."""
    def __init__(self, var):
        self.var = var

    def __str__(self):
        return 'Field \'{}\' contains duplicates'.format(self.var)


class AHPNonSquarePreferenceMatrixError(AHPModelError):
    """Error for cases when the preference matrix in the AHP model are not square matrices."""
    def __init__(self, kind, name, side, actual_width, actual_height):
        self.kind = kind
        self.name = name
        self.side = side
        self.actual_width = actual_width
        self.actual_height = actual_height

    def __str__(self):
        return 'Expecting \'{0}:{1}\' preference matrix to be {2}x{2} got {3}x{4}'.format(self.kind, self.name,
                                                                                          self.side,
                                                                                          self.actual_width,
                                                                                          self.actual_height)


class AHPMissingPreferenceMatrixError(AHPModelError):
    """Error for cases when a required preference matrix is missing in the AHP model."""
    def __init__(self, kind, name):
        self.kind = kind
        self.name = name

    def __str__(self):
        return 'Missing \'{}\' preference matrix for \'{}\''.format(self.kind, self.name)


class AHPPreferenceMatrixConversionError(AHPModelError):
    """Error for cases when it is unable to convert a matrix to a reciprocal one."""
    def __init__(self, pm, loc):
        self.pm = pm
        self.loc = loc

    def __str__(self):
        return 'Preference matrix {0} is unable to be convert a reciprocal one.\n \
        Give a valid value to the element at ({1[0]}, {1[1]}).'.format(self.pm, self.loc)