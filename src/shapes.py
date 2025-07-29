"""
Example module nested in a subdirectory.
"""

from dataclasses import dataclass


@dataclass
class Rectangle:
    """An example dataclass representing a rectangle."""

    a: float
    b: float

    def area(self) -> float:
        """Calculate the area of the rectangle."""
        return self.a * self.b

    def perimeter(self) -> float:
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.a + self.b)
