import mcpi.minecraft as minecraft
import mcpi.block as block

class thermometer:
    #set thermometer size (0 to 2 = 3)  
    sizeX = 3 -1
    sizeY = 50 -1
    sizeZ = 3 -1

    posX = 0
    posY = 0
    posZ = 0
    temp = 0
    
    #build connection with minecraft
    mc = minecraft.Minecraft.create()

    def __init__(self,name, x, y, z):
        self.name = name
        playerPos = self.mc.player.getPos()
        self.posX = playerPos.x - self.sizeX//2 + x
        self.posY = playerPos.y - self.sizeY//2 + y
        self.posZ = playerPos.z + z

    def name_update(self, name):
        self.name = name

    def pos_update(self, x, y, z):
        playerPos = self.mc.player.getPos()
        self.posX = playerPos.x - self.sizeX//2 + x
        self.posY = playerPos.y - self.sizeY//2 + y
        self.posZ = playerPos.z + z

    def build_ther(self):
        #build thermometer
        self.mc.setBlocks(self.posX, self.posY, self.posZ,
                          self.posX + self.sizeX, self.posY + self.sizeY, self.posZ + self.sizeZ, block.GLASS.id)
        
        #reset ther_pos to ther_pos_mid
        self.posX = self.posX + 1
        self.posZ = self.posZ + 1
        self.mc.setBlocks(self.posX - self.sizeX, self.posY - self.sizeZ, self.posZ - self.sizeZ ,
                          self.posX + self.sizeX, self.posY + self.sizeZ, self.posZ + self.sizeZ, block.GLASS.id)
        self.mc.setBlocks(self.posX - self.sizeX +1, self.posY - self.sizeZ +1, self.posZ - self.sizeZ +1,
                          self.posX + self.sizeX -1, self.posY + self.sizeZ -1, self.posZ + self.sizeZ -1, block.LAVA.id)

        self.postToChat("Thermometer created")
    
    def postToChat(self, string):
        self.mc.postToChat(string)

    #update meter scale
    def temp_update(self, r):
        if 0 < r < self.sizeY:
            if r != self.temp:
                temp = r
                self.mc.postToChat("temperature now : %s" %r)
            self.mc.setBlocks(self.posX, self.posY, self.posZ,
                              self.posX , self.posY + r, self.posZ, block.LAVA.id)
            self.mc.setBlocks(self.posX, self.posY + r + 1, self.posZ,
                              self.posX , self.posY + self.sizeY, self.posZ, block.AIR.id)
        elif r >= sizeY:
            mc.postToChat("temp higher than 50!")
        elif r <= 0:
            mc.postToChat("temp lower than 0!")

    #delete previous meter
    def ther_delete(self):
        #delete thermometer
        self.mc.setBlocks(self.posX - self.sizeX, self.posY - self.sizeZ, self.posZ - self.sizeZ ,
                          self.posX + self.sizeX, self.posY + self.sizeY, self.posZ + self.sizeZ, block.AIR.id)
        self.mc.setBlocks(self.posX - 1, self.posY, self.posZ - 1 ,
                          self.posX + 1, self.posY + self.sizeY, self.posZ + 1, block.AIR.id)
        
        
