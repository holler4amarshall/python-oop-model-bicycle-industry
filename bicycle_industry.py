# modelling the bicycle industry

class Bicycle: 
    
    def __init__(self, name, weight, cost):
        '''Initialise Bicycles with attributes for name, weight and cost'''
        self.name = name 
        self.weight = weight
        self.cost = cost
        
class Customer: 
    
	def __init__(self, name, budget):
	    '''Initialise Customers with attributes for name, budget and list of affordable bicycles'''
	    self.name = name
	    self.budget = budget
	    self.affordable_bicycles = []

        
class Bicycle_store: 
    def __init__(self, name):
        '''Initialise Bicycle Stores with attributes for store name, 
        store markup, store retail price list, store inventory list'''
        self.name = name
        self.markup = 0
        self.retail_price = {}
        self.inventory = {}
        
    def get_markup(self):
        '''return the store markup'''
        return self.markup
    
    def set_retail_price(self, Bicycle):
        '''in a dictionary, note each bicycle and its retail price.
        calculate retail price based on bicycle cost + shop markup'''
        retail = Bicycle.cost + (Bicycle.cost * (self.get_markup() / 100.0))
        self.retail_price[Bicycle.name] = retail
        return self.retail_price
        
    def get_retail_price(self, bicycle):
        return self.retail_price[bicycle]
        
    def create_suggestion_list(self, Bicycle, Customer):
        '''create a list of bicycles for each customer based on bicycles within their budget'''
        if Customer.budget * 100.0 > self.retail_price[Bicycle.name]:
            Customer.affordable_bicycles.append(Bicycle.name)
        return str(Customer.affordable_bicycles)
        
    def make_suggestions(self, Customer):
        '''using the customer suggestion list, create a suggestion string to recommend bicycles within customer budget'''
        if len(Customer.affordable_bicycles) > 0: 
            suggestion_as_string = ", ".join(Customer.affordable_bicycles )
            print Customer.name + ' with a budget of: $' + str(Customer.budget) + ', you may wish to consider: ' \
            + suggestion_as_string + '.'
        else:
            print Customer.name + ', unfortunately we cannot offer any bikes within your budget.'
        
    def current_inventory(self): 
        '''print and return the current inventory for the store'''
        current_inventory = ', '.join("{!s}={!r}".format(key,val) for (key,val) in self.inventory.items())
        print 'The current inventory at ' + self.name + ' is: ' + current_inventory
        return current_inventory
		
		
