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


Open/Closed Principle (OCP)
Software entities (classes, modules, functions) should be open for extension but closed for modification. You should be able to extend the functionality without modifying existing code.

File: ocp.py

In this example, new logging mechanisms (e.g., writing to a file or a database) can be added without modifying the existing logging system.

python
Copy code
class Logger:
    # Base class for logging
    ...

class ErrorLogger(Logger):
    # New functionality (logging to file, database)
    ...
Liskov Substitution Principle (LSP)
Derived classes must be substitutable for their base classes without altering the correctness of the program. This means that subclasses should behave in a way that does not break the functionality of the base class.

File: lsp.py

Here, the Ostrich class initially violates LSP because it cannot fly, but the issue is resolved by creating a NonFlyingBird class to handle birds that do not fly.

python
Copy code
class Bird:
    def fly(self):
        return "Flying..."

class Sparrow(Bird):
    # Substitutable subclass
    ...

class Ostrich(NonFlyingBird):
    # Fix: Ostrich does not fly but can run
    ...
Interface Segregation Principle (ISP)
Clients should not be forced to depend on interfaces they do not use. This principle encourages creating smaller, more specific interfaces rather than large, general-purpose ones.

File: isp.py

In this example, the Workable and Eatable interfaces are separated, ensuring that the RobotWorker class does not need to implement unnecessary methods like eat().

python
Copy code
class Workable:
    # Interface for working
    ...

class Eatable:
    # Interface for eating
    ...

class HumanWorker(Workable, Eatable):
    # Implements both work and eat
    ...

class RobotWorker(Workable):
    # Implements only work
    ...
Dependency Inversion Principle (DIP)
High-level modules should not depend on low-level modules. Both should depend on abstractions. This principle decouples high-level logic from low-level implementation details.

File: dip.py

In this example, the NotificationService depends on an abstract Notifier class rather than concrete classes like EmailNotifier or SMSNotifier. This allows easy switching or adding new notification methods.

python
Copy code
class Notifier:
    # Abstract notifier class
    ...

class EmailNotifier(Notifier):
    # Low-level email notification
    ...

class SMSNotifier(Notifier):
    # Low-level SMS notification
    ...

class NotificationService:
    # High-level service depending on abstraction (Notifier)
    ...
How to Run
Clone this repository:
bash
Copy code
git clone https://github.com/yourusername/solid-principles-python
