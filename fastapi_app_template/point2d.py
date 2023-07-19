from pydantic import BaseModel


class Point2D(BaseModel):
    x: float
    y: float

    def __str__(self):
        return f"({self.x}, {self.y})"
