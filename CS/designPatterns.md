# Introduction
## Description
* Best Practices for OOP devs to solve general problem types
# Notes
* Gang of Four (GOF) == Authors of "Design Patterns - Elements of Reusable Object-Oriented Software"
* Philosophy:
    * Program to Interface, not implementation
    * Favour Object Composition over inheritance
## Use of Design Patterns
* Common Platform for Devs: Standard of language to communicate with other devs ideas
* Best Practices: An agreed upon standard so all can learn faster and catch up better
## Pattern Types (By Category)
* Traditionally, there are 3 -- this [site](https://www.tutorialspoint.com/design_pattern/design_pattern_quick_guide.htm) adds J2EE patterns
### Creational Patterns
* Create objects w/o logic and flexibility to create based on use case
#### Factory Patterns
*Description*
* Create Object when requested for by client, w/o logic being given to client (They merely request and are given the finished object)
* Ex: ShapeFactory class will be passed a string, and will return the corresponding object -- therefore creates object, but doesn't show the logic
#### Abstract Factory Pattern
*Description*
* "Factory of Factories"

### Structural Patterns
* Classes and objects -- inheritance to help create objects and functions
### Behavioral Patterns
* Communication between objects
### J2EE
* Presentation layer objects; by Sun Java Center
