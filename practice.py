class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."


cat_1 = Cat("Blue", 3)

print(cat_1)
print(Cat.__class__)


#############################################

class_name = 'Mouse'
super_class = ()


def __init__(self, name, age):
    self.name = name
    self.age = age


def __str__(self):
    return f"{self.name} is {self.age} years old."


mouse_dict = {'__init__': __init__, '__str__': __str__, '__module__': '__main__'}
Mouse = type(class_name, super_class, mouse_dict)

mouse_1 = Mouse("Mickey", 90)
print(mouse_1)
print(Mouse.__class__)


#############################################


def cat_meta(class_name, super_class, class_dict):
    if '__str__' not in class_dict:
        def __str__(self):
            return class_name
        class_dict['__str__'] = __str__
    return type(class_name, super_class, class_dict)


class Dog(metaclass=cat_meta):
    def __init__(self, name, age):
        self.name = name
        self.age = age


dog_1 = Dog("Rex", 5)
print(dog_1)


#############################################


class CountMeta(type):

    def __init__(cls, name, super_class, cls_dict):
        cls.count = 0
        prev_init = cls.__init__

        def __init__(*args, **kwargs):
            cls.count += 1
            return prev_init(*args, **kwargs)
        cls.__init__ = __init__

        type.__init__(cls, name, super_class, cls_dict)


class Cat(metaclass=CountMeta):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."


cat_1 = Cat("Blue", 3)
cat_2 = Cat("Kitty", 2)
cat_3 = Cat("Fluffy", 5)
print(Cat.count)


#############################################


class ToStr:
    def __str__(self):
        result = f'{self.__class__.__name__}: '
        for key in self.__dict__.keys():
            result += f'{key}={self.__dict__[key]} '
        return result


class MetaStr(type):
    def __new__(cls, name, super_class, cls_dict):
        super_class = (ToStr,)
        return type.__new__(cls, name, super_class, cls_dict)


class Cat(metaclass=MetaStr):
    def __init__(self, name, age):
        self.name = name
        self.age = age


cat_1 = Cat("Blue", 3)
print(cat_1)


#############################################


class AbstractValidator(ABC):

    @abstractmethod
    def validate(self, value):
        ''


class FalseValidator(AbstractValidator):

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

    def validate(self, value):
        ...


a = FalseValidator('Hello world!')
print(a)


