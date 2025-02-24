# python_projects

Learning progress overview:

_Week 1-2_: Learned about data types, data structures, conditional statements and loops. Learned how to manipulate the data structures with data
>> * Data Types/Variables: String, Integer, Float, Boolean 
>> * Data Structures: List/Array, Dictionary, Tuples, and Sets
>> * Overall pretty basic concepts. I took a python and database course in college so a lot of this was just a refresher for me. 

_Week 3-4_: Learned function arguments, namespace/scope, object-oriented programming (class structure) and unit testing 
>> * function arguments were really easy to grasp 
>> * namespace and scope took longer to wrap my head around it. This became easier and more straightforward after working with Classes more often 
>> * Object Oriented programming was also a bit difficult to grasp at first with the introduction of Classes. Encapsulation, Abstraction, Inheritance and Polymorphism made sense, in an of themselves, but I struggled to understand the application for each at times. 
>> * Classes felt really odd to use at first, but their value became more apparent the more I exposed myself to the syntax and completed a coding interview exercies that could easilt leverage the functions of a class and more modular code 
>> * Unit testing is difficult. Still struggle to grasp the concepts and throwing exceptions. In a production environment, when going over the PRDs with a product manager at the start of a sprint, I believe unit testing will make more sense in the scope of a project and the specific stop gap's extrapolated from the requirments of the code functionality. 

_Week 5: Worked on a code interview question focused on object oriented programming  
>> * Project was to read in a text file of Drivers with name, trip start time, end time, and miles driven as the given input. 
>> * The required output of the python script was driver name, total miles driven, and mph. 
>> * Nuance of the project was ensuring the script could handle multiple trips from the same driver or no trips at all. 
>> * Findings: I initially started to read the input data into a nested list, and begin creating one main function/method inside of the a trip class that would calculate all of the required output data. This proved to be limiting and my class structure was really poor at first. I then talked with one of my friends who is a senior developer and he gave me some tips and suggested that I make my code more modular and break down some of the trip calcuations into their own methods inside of the trips class. I then went back and created a driver class as well to modulate more of my code. By building out the class structure and creating more methods, I was able to abstract away the unneccessary data/calculations that were originally inside of my main trip function and encapsulate the data and their respective functions into a more logical approach.   


_Week 6-8: Worked on Advanced Python Learning Modules
>> * Linear Data Structures 
>> 	* Linked Lists, Doubley Linked Lists, Searching Arrays, Queues, Stacks
>>  	* Linked Lists were extremely cumbersom to set up and the application of them seems relatively niche (i.e. GPS functionality)
>>  	* Queues and Stacks were easy to grasp in concept (video game queues when servers are overloaded). They were a bit tricky to set-up, but it became easier with more practice. I understand the application of stacks for say a stack of weights at a gym, but struggle to grasp the variety of application in a software environment. My guess is certain algorithms make use of a stack data structure for the last in, first out approach. 
>> * Hash Maps
>> * Went over algorithmic concepts such as recursion and asymptotic notation (Big O Runtime) 
>> * Non-Linear Data Structures: Trees, Binary Search Trees, Heaps
