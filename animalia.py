class Animalia:
    def __init__(self,Kingdom,Phylum,Class,Family, Order,Genus,Species):
        self.Kingdom = Kingdom
        self.Phylum = Phylum
        self.Class= Class
        self. Family= Family
        self.Order = Order 
        self.Genus= Genus
        self.Species= Species
    def getKingdom(self):
        return self.Kingdom
    def getPhylum(self):
        return self.Phylum
    def getClass(self):
        return self.Class  
    def getFamily(self):
        return self.Family
    def getOrder(self):
        return self.Order
    def getGenus(self):
        return self.Genus
    def getSpecies(self):
        return self.Species 
        #Animals 
print("animals available for study: Lion, Human,Leopard,Octopus,HoneyBee")


Lion = Animalia ("Animalia","Chordata","Mammalia","Carnivora","Felidae","Panthera"," Panthera Leo")
print(Lion.getKingdom())
print(Lion.getPhylum())
print(Lion.getClass())
print(Lion.getFamily())
print(Lion.getOrder())
print(Lion.getGenus())
print(Lion.getSpecies())

Human = Animalia ("Animalia","Chordata","Mammalia","Primata","Hominidae","Homo","Sapien")
print(Lion.getKingdom())
print(Human.getPhylum())
print(Human.getClass())
print(Human.getFamily())
print(Human.getOrder())
print(Human.getGenus())
print(Human.getSpecies())

Leopard = Animalia ("Animalia","Chordata","Mammalia","Carnivora","Felidae","Panthera","Panthera Unci")
print(Leopard.getKingdom())
print(Leopard.getPhylum())
print(Leopard.getClass())
print(Leopard.getFamily())
print(Leopard.getOrder())
print(Leopard.getGenus())
print(Leopard.getSpecies())

Octupus = Animalia ("Animalia","Mollusca","Cephalopoda","Octopoda","Octopodidae","Octopus","Octopus Vulgaris")
print(Octupus.getKingdom())
print(Octupus.getPhylum())
print(Octupus.getClass())
print(Octupus.getFamily())
print(Octupus.getOrder())
print(Octupus.getGenus())
print(Octupus.getSpecies())

HoneyBee = Animalia ("Animalia","Athropoda","Insecta","Hymenoptera","Apidae","Apis","Apis Mellifera")
print(HoneyBee.getKingdom())
print(HoneyBee.getPhylum())
print(HoneyBee.getClass())
print(HoneyBee.getFamily())
print(HoneyBee.getOrder())
print(HoneyBee.getGenus())
print(HoneyBee.getSpecies())
