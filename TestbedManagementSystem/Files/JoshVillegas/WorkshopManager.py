from Workshop import Workshop
from WorkshopGroup import WorkshopGroup
from WorkshopUnit import WorkshopUnit
from lib2to3.pgen2.tokenize import group

class WorkshopManager:
    def __init__(self):
        print("Workshop Manager created")
        self.__workshopSet = set() #a set of all workshop instances
        self.__groupSet = set() #not sure if used yet
        self.__unitSet = set() #not sure if used yet
        
    def __getWorkshop(self, workshopName):
        for workshop in self.__workshopSet:
            if workshopName == workshop.getName():
                return workshop
            return None
        
    def __getGroup(self, groupName):
        for group in self.__groupSet:
            if groupName == WorkshopGroup.getName():
                return WorkshopGroup
            return None
        
    def __getUnit(self, unitName):
        for unit in self.__unitSet:
            if unitName == WorkshopUnit.getName():
                return WorkshopUnit
            return None
        
    
    def getReferenceMaterial(self, workshopName):
         workshop = self.__getWorkshop(workshopName)
         return (workshop.getReferenceMaterial())
     
    def getWorkshopStatus(self, workshopName):
        
    def getAvailableWorkshops(self):
    
    def getUnitConnectionString(self, unitName):
        unit = self.__getUnit(unitName)
        return (unit.getConnectionString())
    