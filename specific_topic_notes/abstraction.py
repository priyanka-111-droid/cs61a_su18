'''
ABSTRACTION
Hiding specific details.


Where in real life?
Car-> Driver only sees steering wheel and gears,not the engine
Oven-> User only needs to know the buttons on the oven to heat food and not the actual heating
mechanism.


Where in programs?
Variable abstraction, functional abstraction, data abstraction


Data abstraction?
- Allows us to represent compound values in program.
- Compound values have multiple components(rational
number,latitude and longitude)
- Eg. Rational numbers 


Rational numbers example?
- can be implemented as abstract data type(ADT)
- Use constructors(create rat no) and selectors(select from rat no)
- Involve an abstraction barrier.
- Representation/Implementation Layer ->	[x, y], [0], [1]
- Data Abstraction 1 layer ->	make_rational, numerator, denominator
- Data Abstraction 2 layer -> mul_rational, add_rational
- User Programs -> Could be anything using the layer above

- Each layer would only need to use the layer above it, meaning that 
when users use the data abstractions, they do not need to care about how it is implemented.
- Assuming implementation of data type leads to abstraction violation.
