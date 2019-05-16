class Person:
    def __init__(self, name,age):
        self._name=name
        self._age=age

    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age

    @name.setter
    def name(self,name):
        self._name=name

    def play(self):
        if self._age<=16:
            print("%s playing game" %self._name)
        else:
            print("%s is playing "%self._name)
    
def main():
    person=Person("wang da chui",12)
    person.play()
    person.name="gebilaowang"
    person.play()

if __name__ == "__main__":
    main()