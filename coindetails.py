# This will be my first attempt to create a class with currency. 6/7/22

if __name__ == '__main__':
    pass

class Currency:
    
    def __init__(self, denomination, value, composition, weight, diameter, thickness):
        self.denomination = denomination
        self.value = value + 'cents'
        self.composition = composition
        self.weight = weight + 'g'
        self.diameter = diameter + 'mm'
        self.thickness = thickness + 'mm'
        
    def coin_details(self):
        return 'Denomination: {}\nValue:        {}\nComposition:  {}\nWeight:       {}\nDiamete:      {}\nThickness:    {}\n'.format(self.denomination, self.value, self.composition, self.weight, self.diameter, self.thickness)
    
    def coin_comp(self):
        return self.composition
    def coin_weight(self):
        return self.weight
    def coin_diameter(self):
        return self.diameter
    def coin_thick(self):
        return self.thickness
    
quarter = Currency('Quarter', '0.25', 'Cupro-Nickel',       '5.670', '24.26', '1.75')
dime =    Currency('Dime',    '0.10', 'Cupro-Nickel',       '2.268', '17.91', '1.35')
nickel =  Currency('Nickel',  '0.05', 'Cupro-Nickel',       '5.000', '21.21', '1.95')
penny =   Currency('Penny',   '0.01', 'Copper Plated Zinc', '2.500', '19.5',  '1.52')

print(Currency.coin_details(quarter))
print(dime.coin_details())
print(nickel.coin_details())
print(penny.coin_details())