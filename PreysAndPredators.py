import numpy as np

class PreysAndPredators:
    """docstring for PreysAndPredators"""
    def __init__(self, r, a, b, m, init_preys, init_predators, h, max_length):
        self.r = r
        self.a = a
        self.b = b
        self.m = m 
        self.init_preys = init_preys 
        self.init_predators = init_predators
        self.h = h
        self.max_length = max_length
    

    def preys_population(self, previous_preys, previous_predators, h):
        result = previous_preys + h * self.preys_derivative(previous_preys, previous_predators)
        return result

    def predators_population(self, previous_preys, previous_predators, h):
        result = previous_predators + h * self.predators_derivative(previous_preys, previous_predators)
        return result

    def preys_derivative(self, prev_preys, prev_predators):
        result = self.r * prev_preys - self.a * prev_preys * prev_predators
        return result

    def predators_derivative(self, prev_preys, prev_predators):
        result = self.b * prev_preys * prev_predators - self.m * prev_predators
        return result

    def evolution_species(self, h, max_length):
        previous_preys = self.init_preys
        previous_predators = self.init_predators
        print(0)
        print(previous_preys)
        print(previous_predators)
        print("-------------------")

        for t in np.arange(h, max_length, h):
            previous_preys = self.preys_population(previous_preys, previous_predators, h)
            previous_predators = self.predators_population(previous_preys, previous_predators, h)
            
            print(t)
            print(previous_preys)
            print(previous_predators)
            print("-------------------")
            
            t = t + h

def main():
   papr_ex = PreysAndPredators(3,2,1,2,2,2,0.01,100)
   papr_ex.evolution_species(papr_ex.h, papr_ex.max_length)

if __name__ == '__main__':
    main()