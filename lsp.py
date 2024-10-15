class Bird:
    def fly(self):
        return "Flying..."

class Sparrow(Bird):
    def fly(self):
        return "Sparrow flying high!"

class Ostrich(Bird):
    # Ostrich cannot fly, so this violates LSP
    def fly(self):
        raise NotImplementedError("Ostrich can't fly!")

def make_bird_fly(bird: Bird):
    return bird.fly()

# Main program block
sparrow = Sparrow()
print(make_bird_fly(sparrow))  # Works as expected

ostrich = Ostrich()
try:
    print(make_bird_fly(ostrich))  # Raises an error, violating LSP
except NotImplementedError as e:
    print(e)

# Fix the violation by refactoring

class NonFlyingBird(Bird):
    def fly(self):
        return "I can't fly but can run!"

class Ostrich(NonFlyingBird):
    def fly(self):
        return "Ostrich running fast!"

# Now Ostrich properly adheres to the LSP
ostrich_fixed = Ostrich()
print(make_bird_fly(ostrich_fixed))  # No error, and LSP is followed.
