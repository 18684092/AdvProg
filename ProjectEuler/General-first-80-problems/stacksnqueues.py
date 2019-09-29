""" Stack and Queue Objects """

"""
This module contains classes for stacks and queues
written by Andy Perrett 2018

Stack is a LIFO store
LIFO is an alias (Child) of Stack
FILO is an alias (Child) of Stack

"""

class Stack():
  """ A Stack is a Last in First out store """

  def __init__(self, startingList = []):
    if len(startingList) == 0:
      self.stack = []
    else:
      self.stack = startingList
    self.old = []

  def push(self, value):
    """ Adds a new item to the top of the stack """
    self.value = value 
    self.stack.append(value)
    
  def pop(self):
    """
    Pops the last entry. Returns last item and deletes
    that item. 
    """
    l = self.stack[-1]
    del self.stack[-1]
    return(l)
  
  def last(self):
    return(self.stack[-1])
  
  def top(self):
    return(self.last())
  
  def clear(self):
    """ Empties stack """
    self.stack = []
    
  def count(self):
    """ Returns the number of items in stack """
    return(len(self.stack))
  
  def getItem(self, value):
    """ Returns the item at index "value" """ 
    return(self.stack[value])
  
  def getItems(self):
    """ Yields and interable version of the stack """
    for i in self.stack:
      yield i
      
      
  def __repr__(self):
    """ Is called when "print(object)" is called """
    s = "["
    for i, value in enumerate(self.stack):
      s += str(value)
      if i < len(self.stack) - 1:
        s += ", "
    s += "]"
    return(s)

  def __iter__(self):
    """ Number conversion is iterable """
    for i in self.stack:
      yield i
  
  def store(self):
    """ Save a copy of the stack at this point in time """
    self.old = self.stack[:]
    
  def restore(self):
    """ Restore stack to the previous stored version """
    self.stack = self.old[:]
    
class LIFO(Stack):
  pass
  
class FILO(Stack):
  pass
