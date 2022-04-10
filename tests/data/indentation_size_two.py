class MyClass:
    """ Multiline
    class docstring
    """

    def method(self):
        """Multiline
        method docstring
        """
        a = 1
        return a


def foo():
    """This is a docstring with
    some lines of text here
    """
    return


def poit():
    """
    Lorem ipsum dolor sit amet.

    Consectetur adipiscing elit:
     - sed do eiusmod tempor incididunt ut labore
     - dolore magna aliqua
       - enim ad minim veniam
       - quis nostrud exercitation ullamco laboris nisi
     - aliquip ex ea commodo consequat
    """
    pass

# output

class MyClass:
  """Multiline
  class docstring
  """

  def method(self):
    """Multiline
    method docstring
    """
    a = 1
    return a


def foo():
  """This is a docstring with
  some lines of text here
  """
  return


def poit():
  """
  Lorem ipsum dolor sit amet.

  Consectetur adipiscing elit:
   - sed do eiusmod tempor incididunt ut labore
   - dolore magna aliqua
     - enim ad minim veniam
     - quis nostrud exercitation ullamco laboris nisi
   - aliquip ex ea commodo consequat
  """
  pass