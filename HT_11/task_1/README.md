# Class Calc
## Task text

Create a Calc class that will have the __last_result__ attribute and 4 methods. 
Methods must perform mathematical operations with 2 numbers, namely:
addition, subtraction, multiplication, division.

* If the __last_result__ attribute is called when instantiating a class, it should return an empty value.
* If you use one of the methods - __last_result__ must return the result of the PREVIOUS method.


```
    Example:

     last_result --> None
     1 + 1
     last_result --> None
     2 * 3
     last_result --> 2
     3 * 4
     last_result --> 6
     ...
```

___

## Installation
Usually, a Git repository is obtained in one of two ways:
1. Take a local directory that is not currently under version control and turn it into a Git repository, or
2. Clone an existing Git repository from where. 
Either way, you get a ready-to-use Git repository on your local machine.

For Windows

```
$ cd /c/user/my_project
```

For Mac 
```
$ cd /Users/user/my_project
```

## Example usage

### Code example 
```
# Test
obj = Calc()
print(obj.last_result)

obj.add(1, 1)
print(obj.last_result)

obj.multiplication(2, 3)
print(obj.last_result)

obj.multiplication(3, 4)
print(obj.last_result)
```

### Results
```None
None
2
6
```