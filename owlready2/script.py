from owlready2 import *
onto_path.append("./repository")
onto = get_ontology("http://www.lesfleursdunormal.fr/static/_downloads/pizza_onto.owl")
onto.load()

with onto:
     class NonVegetarianPizza(onto.Pizza):
       equivalent_to = [
         onto.Pizza
       & ( onto.has_topping.some(onto.MeatTopping)
         | onto.has_topping.some(onto.FishTopping)
         ) ]
       def eat(self): print("Sou vegetariano!")

test_pizza = onto.Pizza("test_pizza")
test_pizza.has_topping = [ onto.CheeseTopping(),
                            onto.TomatoTopping(),
                            onto.MeatTopping  () ]

print(test_pizza.__class__)

sync_reasoner()

print(test_pizza.__class__)
test_pizza.eat()

onto.save()