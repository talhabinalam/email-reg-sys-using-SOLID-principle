# SOLID Principles in Python

This repository contains Python examples that demonstrate the application of the SOLID principles, which are foundational guidelines for object-oriented programming and design. Each principle helps to create code that is easier to maintain, scale, and adapt over time.

## Table of Contents
- [SOLID Principles Overview](#solid-principles-overview)
- [Single Responsibility Principle (SRP)](#single-responsibility-principle-srp)
- [Open/Closed Principle (OCP)](#openclosed-principle-ocp)
- [Liskov Substitution Principle (LSP)](#liskov-substitution-principle-lsp)
- [Interface Segregation Principle (ISP)](#interface-segregation-principle-isp)
- [Dependency Inversion Principle (DIP)](#dependency-inversion-principle-dip)
- [How to Run](#how-to-run)

## SOLID Principles Overview

The **SOLID** principles are a set of best practices that help developers design maintainable and scalable object-oriented systems. These principles are:
- **S**ingle Responsibility Principle (SRP)
- **O**pen/Closed Principle (OCP)
- **L**iskov Substitution Principle (LSP)
- **I**nterface Segregation Principle (ISP)
- **D**ependency Inversion Principle (DIP)

Each principle is explained below with examples implemented in Python.

---

## Single Responsibility Principle (SRP)

A class should have only one reason to change, meaning it should have only one responsibility or job.

**File:** `srp.py`

In this example, the `Users`, `Logger`, and `Email` classes each have a single responsibility: managing users, logging errors, and sending emails, respectively. This separation of concerns ensures that changes in one aspect of the system do not affect others.

```python
class Users:
    # Responsibility: Database management for user registration
    ...

class Logger:
    # Responsibility: Logging system messages
    ...

class Email:
    # Responsibility: Sending emails
    ...


---

## Open/Closed Principle (OCP)

Software entities (classes, modules, functions) should be open for extension but closed for modification. This principle encourages building systems that can be extended without modifying existing code.

**File:** `ocp.py`

In this example, the `Logger` class is extended by the `ErrorLogger` class to add new logging mechanisms without altering the base `Logger` class. You can extend the system by adding new functionality, such as logging to a file or a database, without modifying the core behavior.

```python
class Logger:
    # Base class for logging
    def write_log_to_system(self, message):
        print(f"Log to system: {message}")

class ErrorLogger(Logger):
    # Extends functionality for logging to file and database
    def write_log_to_file(self, message):
        with open('log.txt', 'a') as writer:
            writer.write(message + '\n')
            
    def write_log_to_db(self, message):
        con = sqlite3.connect('sqldb.db')
        con.execute("INSERT INTO ErrorLog (Message) VALUES (?)", (message,))
        con.commit()
        con.close()


## Liskov Substitution Principle (LSP)

Derived classes must be substitutable for their base classes without altering the correctness of the program. This means that subclasses should behave in ways that respect the expectations of the base class.

### Example

In this example, the `Ostrich` class originally violates the LSP because it does not fly, even though it inherits from `Bird`. The solution is to create a new `NonFlyingBird` class for birds that don't fly, maintaining the substitutability.

**File:** `lsp.py`

```python
class Bird:
    def fly(self):
        return "Flying..."

class Sparrow(Bird):
    # Sparrow can fly, so it is substitutable for Bird
    def fly(self):
        return "Sparrow flying high!"

class NonFlyingBird(Bird):
    # Subclass for birds that do not fly
    def fly(self):
        return "Cannot fly, but can run..."

class Ostrich(NonFlyingBird):
    # Ostrich is a non-flying bird
    def run(self):
        return "Ostrich running fast!"

# Example usage
def make_bird_fly(bird: Bird):
    print(bird.fly())

# This works correctly
sparrow = Sparrow()
make_bird_fly(sparrow)

# This also works correctly, even though the Ostrich cannot fly
ostrich = Ostrich()
make_bird_fly(ostrich)  # It will not throw an error but will provide a valid response



## Interface Segregation Principle (ISP)

Clients should not be forced to depend on interfaces they do not use. This principle encourages creating smaller, more specific interfaces rather than large, general-purpose ones.

### Example

In this example, `Workable` and `Eatable` are two separate interfaces, ensuring that classes like `RobotWorker` only need to implement the methods relevant to them.

**File:** `isp.py`

```python
class Workable:
    # Interface for work-related functionality
    def work(self):
        pass

class Eatable:
    # Interface for eat-related functionality
    def eat(self):
        pass

class HumanWorker(Workable, Eatable):
    # Human can work and eat
    def work(self):
        print("Working...")
    
    def eat(self):
        print("Eating...")

class RobotWorker(Workable):
    # Robot only works, does not eat
    def work(self):
        print("Working...")



## Dependency Inversion Principle (DIP)

High-level modules should not depend on low-level modules. Both should depend on abstractions. This principle decouples high-level logic from low-level implementation details.

### Example

In this example, `NotificationService` depends on the abstract `Notifier` class, rather than concrete implementations like `EmailNotifier` or `SMSNotifier`. This allows for easy substitution of notifiers without changing the service.

**File:** `dip.py`

```python
class Notifier:
    # Abstract class for notification behavior
    def notify(self, message):
        pass

class EmailNotifier(Notifier):
    # Concrete implementation for email notifications
    def notify(self, message):
        print(f"Sending email notification: {message}")

class SMSNotifier(Notifier):
    # Concrete implementation for SMS notifications
    def notify(self, message):
        print(f"Sending SMS notification: {message}")

class NotificationService:
    def __init__(self, notifier: Notifier):
        # High-level module depending on the abstraction
        self.notifier = notifier

    def send_notification(self, message):
        self.notifier.notify(message)

# Example usage:
email_notifier = EmailNotifier()
sms_notifier = SMSNotifier()

service = NotificationService(email_notifier)
service.send_notification("Email message")

service = NotificationService(sms_notifier)
service.send_notification("SMS message")
