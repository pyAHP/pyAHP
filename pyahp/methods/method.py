# -*- coding: utf-8 -*-
"""pyahp.methods.method

This module contains the abstract Method class used as a base class for other methods.
"""

from abc import ABC, abstractmethod


class Method(ABC):
    """Method

    Abstract class to provide a common interface for various methods.
    """

    @abstractmethod
    def estimate(self, preference_matrix):
        """Estimate the priority from the provided preference matrix

        Args:
            preference_matrix (np.array): A two (nxn) dimensional reciprocal array.

        Returns:
            nx1 np.array of priorities
        """
        pass

    @staticmethod
    def _check_matrix(matrix):
        width, height = matrix.shape

        assert width == height, "Preference Matrix should be a square matrix"
        assert width >= 2, "Preference Matrix too small or empty"

        for i in range(width):
            for j in range(height):
                if i == j:
                    assert matrix[i, j] == 1, "Preference should be 1 on the diagonal"
                else:
                    assert abs(1 - matrix[i, j]*matrix[j, i]) <= 0.011, "Failed consistency check for Reciprocal Matrix"
