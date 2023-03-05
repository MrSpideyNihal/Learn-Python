"""Simulates a simple shape renderer using the factory pattern."""
import abc
class Shape(abc.ABC):
    @abc.abstractmethod
    def render(self):
        pass

class Circle(Shape):
    def render(self):
        return "Drawing a circle."\n
class Square(Shape):
    def render(self):
        return "Drawing a square."\n\nFactory = abc_ABC()

def ShapeRenderer(factory):
    """Create and render shapes using the factory pattern."""
    class Factory:
        @abc.abstractmethod
        def create_shape(self, shape_type):
            pass
    
    def render(self, shape):
        return shape.render()
    
    def create_rectangle(self):
        return Square()
    
    def create_circle(self):
        return Circle()
\nif __name__ == "__main__":
    factory = Factory()
    renderer = ShapeRenderer(factory)
    print(renderer.create_rectangle().render())
    print(renderer.create_circle().render())
