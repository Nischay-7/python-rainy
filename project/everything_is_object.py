# TODO: Stage 2 - Everything is an Object!
# 
# In Python, everything is an object! This stage will help you understand:
# - Objects and their identity (id())
# - Aliasing and how it works
# - Dynamic typing in Python
# - Classes as blueprints for objects
# - How to inspect object properties
#
# Instructions:
# Complete all the functions below. Read the docstrings carefully and implement
# the logic using concepts you've learned about objects, ids, types, and aliasing.


def check_same_object(obj1, obj2):
    """
    Use id() to determine if two variables reference the same object.
    
    Args:
        obj1: First object
        obj2: Second object
    
    Returns:
        True if obj1 and obj2 reference the same object (have same id), False otherwise
    
    Hint: Use the id() function to get the identity of each object and compare them.
    """
    # TODO: Implement this function
    if id(obj1) == id(obj2):
        return True
    return False


def create_alias(original):
    """
    Create an alias by assigning a second name to the existing object,
    and verify it points to the same object.
    
    Args:
        original: The original object
    
    Returns:
        A tuple (alias, is_same_object) where:
        - alias is a new name that references the same object as original
        - is_same_object is True if alias and original reference the same object
    
    Hint: Create a new variable that references the same object, then use
          check_same_object() or id() to verify they're the same.
    """
    # TODO: Implement this function
    # Step 1: Create an alias (a new variable pointing to the same object)
    # Step 2: Verify they reference the same object using check_same_object or id()
    alias = original
    return alias, check_same_object(alias, original)


def break_alias(value):
    """
    Show how reassigning breaks aliases.
    
    Args:
        value: An initial value (int or float)
    
    Returns:
        A tuple (original_id, alias_id_before, alias_id_after) where:
        - original_id: id of the original object
        - alias_id_before: id of the alias before reassignment
        - alias_id_after: id of the alias after reassignment (should be different)
    
    Hint: 
    1. Create an alias to value
    2. Get the id of both before reassignment
    3. Reassign the alias to a new value (like value + 1)
    4. Get the id of the alias after reassignment
    5. Return all three ids
    """
    # TODO: Implement this function
    # Step 1: Create an alias
    # Step 2: Store ids before reassignment
    # Step 3: Reassign alias to a new object (e.g., value + 1)
    # Step 4: Get id after reassignment
    alias = value
    original_id = id(value)
    alias_id_before = id(alias)
    alias = value+1
    alias_id_after = id(alias)
    return (original_id, alias_id_before, alias_id_after)


def get_object_type(obj):
    """
    Return the type of an object using type().
    
    Args:
        obj: Any Python object
    
    Returns:
        The type object of obj
    
    Hint: Use the type() built-in function.
    """
    # TODO: Implement this function
    return type(obj)


def demonstrate_dynamic_typing():
    """
    Demonstrate dynamic typing by reassigning a variable from int → float → string.
    
    Returns:
        A tuple (type_after_int, type_after_float, type_after_string) showing
        the type of the variable after each reassignment.
    
    Hint:
    1. Create a variable and assign it an integer
    2. Store its type
    3. Reassign it to a float
    4. Store its type
    5. Reassign it to a string
    6. Store its type
    7. Return all three types
    """
    # TODO: Implement this function
    # Step 1: Assign an integer to a variable, get its type
    # Step 2: Reassign to a float, get its type
    # Step 3: Reassign to a string, get its type
    x = 7
    type_after_int = type(x)
    x = 5.5
    type_after_float = type(x)
    x = "meow"
    type_after_string = type(x)
    return type_after_int, type_after_float, type_after_string


def check_if_none(identifier):
    """
    Check if an identifier refers to None.
    
    Args:
        identifier: A variable that may or may not be None
    
    Returns:
        True if identifier refers to None, False otherwise
    
    Hint: Use the 'is' operator to check for None (not ==).
          In Python, we use 'is None' or 'is not None' to check for None.
    """
    # TODO: Implement this function
    return identifier is None


def explore_integer_class():
    """
    Show that numbers are instances of int class.
    
    Returns:
        A tuple (number_object, is_int_instance, int_class) where:
        - number_object: An integer object (e.g., 42)
        - is_int_instance: True if the number is an instance of int
        - int_class: The int class itself
    
    Hint:
    1. Create an integer object
    2. Use isinstance() to check if it's an instance of int
    3. Return the integer, the result of isinstance(), and the int class
    """
    # TODO: Implement this function
    x = 7
    return x, isinstance(x), int


def explore_string_class():
    """
    Show that strings are instances of str class.
    
    Returns:
        A tuple (string_object, is_str_instance, str_class) where:
        - string_object: A string object (e.g., "hello")
        - is_str_instance: True if the string is an instance of str
        - str_class: The str class itself
    
    Hint:
    1. Create a string object
    2. Use isinstance() to check if it's an instance of str
    3. Return the string, the result of isinstance(), and the str class
    """
    # TODO: Implement this function
    x = "meow"
    return x, isinstance(x), str


def get_class_blueprint(obj):
    """
    Use type() or .__class__ to get an object's class.
    
    Args:
        obj: Any Python object
    
    Returns:
        The class object that obj is an instance of
    
    Hint: You can use either type(obj) or obj.__class__ - both work!
          Try using obj.__class__ for this one.
    """
    # TODO: Implement this function
    # Hint: Use obj.__class__ to get the class
    return obj.__class__


def check_class_relationship(obj, class_type):
    """
    Verify an object is instance of its class using isinstance().
    
    Args:
        obj: Any Python object
        class_type: A class type (e.g., int, str, float)
    
    Returns:
        True if obj is an instance of class_type, False otherwise
    
    Hint: Use isinstance(obj, class_type)
    """
    # TODO: Implement this function
    return isinstance(obj, class_type)


def get_object_info(obj):
    """
    Return object's id, type, and value.
    
    Args:
        obj: Any Python object
    
    Returns:
        A tuple (object_id, object_type, object_value) containing:
        - object_id: The id of the object (using id())
        - object_type: The type of the object (using type())
        - object_value: The value of the object (just obj itself)
    
    Hint: Use id(), type(), and return obj as the value.
    """
    # TODO: Implement this function
    return id(obj), type(obj), obj

