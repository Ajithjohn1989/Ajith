def greeting(**kwargs):
    print(kwargs)
    print("hello",kwargs.get('name'),"you are",kwargs.get('age'),"Years old","\ncourse is",kwargs.get('course'))
greeting(name="ajith",age=21,course="python")
greeting(name="akku",age=21)