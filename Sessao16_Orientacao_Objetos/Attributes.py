# Is the object characteristics     (instance attributes)
# Declared in constructor method

"""
In Java:
public class LightBulb() {
    private int tension;
    private String color;
    private Boolean lightOn = false;

    public LightBulb(int tension, String color) {
        this.tension = tension;
        this.color = color;
    }
}
"""


class LightBulb:
    def __int__(self, tension, color):
        self.__tension = tension    # this two underlines are the 'private' in Java
        self.__color = color
        self.__lightOn = False


class BankAccount:
    def __init__(self, number, limit, balance):
        self.__number = number
        self.__limit = limit
        self.__balance = balance


class Product:
    def __init__(self, name, description, value):
        self.__name = name
        self.__description = description
        self.__value = value


class User:
    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password
