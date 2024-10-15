SOLID Principles
Single Responsibility Principle (SRP): Each class has one responsibility.

Users Class: Handles all database interactions, including user registration.
Email Class: Responsible for sending emails, such as registration confirmation.
Logger Class: Manages error logging.
UserRegistration Class: Orchestrates the registration process, calling other classes to handle specific tasks.
Open/Closed Principle (OCP): The system is open for extension but closed for modification.

New functionalities, such as additional notification methods (like SMS), can be added by creating new classes without modifying existing code.
Liskov Substitution Principle (LSP): Derived classes can be substituted for their base classes without affecting the program's functionality.

If we were to create different types of user notification classes (like SMS or push notifications), they could replace the Email class in UserRegistration without changing its behavior.
Interface Segregation Principle (ISP): Clients should not be forced to depend on interfaces they do not use.

Each class focuses on a specific interface, ensuring that classes only implement methods relevant to their responsibility.
Dependency Inversion Principle (DIP): High-level modules should not depend on low-level modules but rather on abstractions.

The UserRegistration class depends on abstractions (Email, Logger, and Users classes) rather than concrete implementations.
