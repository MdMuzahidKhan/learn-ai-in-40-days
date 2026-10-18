# Day 11 Design Pattern Notes

## Repository Pattern
The Repository pattern separates data access from the API routes.  
This makes the code easier to test and allows the data source to be changed later without changing the endpoint logic.

## Factory Pattern
The Factory pattern creates the correct type of book based on the input `book_type`.  
This keeps object creation logic in one place instead of spreading it across the API.

## Strategy Pattern
Strategy could be used if we later want different search or validation rules for different book types.  
For example, physical books and ebooks may have different filtering or processing behavior.

## Singleton Pattern
Singleton could be used for a shared configuration object or one shared database connection manager.  
It would be useful if we want only one common instance used throughout the application.