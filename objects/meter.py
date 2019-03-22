import mcpi.minecraft as minecraft
import mcpi.block as block

class meter:

    #build connection with minecraft
    mc = minecraft.Minecraft.create()

    def __init__(self, name, posX, posY, posZ, sizeX, sizeY, sizeZ):
        self.name = name
        #size -1 (0 to 2) = 3
        self.sizeX = sizeX -1
        self.sizeY = sizeY -1
        self.sizeZ = sizeZ -1
        playerPos = self.mc.player.getPos()
        self.posX = playerPos.x  + posX
        self.posY = playerPos.y + posY
        self.posZ = playerPos.z + posZ
        self.value = 0

    def name_update(self, name):
        self.name = name
    
    def size_update(self, x, y, z):
        #size -1 (0 to 2) = 3
        self.sizeX = x -1
        self.sizeY = y -1
        self.sizeZ = z -1

    def pos_update(self, x, y, z):
        playerPos = self.mc.player.getPos()
        self.posX = playerPos.x + x
        self.posY = playerPos.y + y
        self.posZ = playerPos.z + z

    def build_meter(self):
        #build meter
        self.mc.setBlocks(self.posX, self.posY, self.posZ,
                          self.posX + self.sizeX, self.posY + self.sizeY, self.posZ + self.sizeZ,
                          block.GLASS.id)
        #build base
        self.mc.setBlocks(self.posX, self.posY - 1, self.posZ,
                          self.posX + self.sizeX, self.posY - 1, self.posZ + self.sizeZ,
                          block.STONE.id)
        
        #clear middle
        self.mc.setBlocks(self.posX + 1, self.posY, self.posZ + 1,
                          self.posX + self.sizeX - 1, self.posY + self.sizeY, self.posZ + self.sizeZ - 1,
                          block.AIR.id)
        #set base value
        self.mc.setBlocks(self.posX + 1, self.posY, self.posZ + 1,
                          self.posX + self.sizeX - 1, self.posY + 1, self.posZ + self.sizeZ - 1,
                          block.LAVA.id)
        
        self.postToChat("%s created" %self.name)

    #post string to chat
    def postToChat(self, string):
        self.mc.postToChat("%s: %s " %(self.name, string))

    #update meter scale
    def meter_update(self, r):
        if 0 < r < self.sizeY:
            if r != self.value:
                self.value = r
                self.postToChat("value now : %s" %r)
                self.mc.setBlocks(self.posX + 1, self.posY, self.posZ + 1,
                                  self.posX + self.sizeX - 1, self.posY + r, self.posZ + self.sizeZ - 1,
                                  block.LAVA.id)
                self.mc.setBlocks(self.posX + 1, self.posY + r + 1, self.posZ + 1,
                                  self.posX + self.sizeX - 1, self.posY + self.sizeY, self.posZ + self.sizeZ - 1,
                                  block.AIR.id)
        elif r >= self.sizeY:
            self.postToChat("value higher than %d!" %self.sizeY)
        elif r <= 0:
            self.postToChat("value lower than 0!")

    #delete previous meter
    def meter_delete(self):
        #delete meter
        self.mc.setBlocks(self.posX, self.posY, self.posZ,
                          self.posX + self.sizeX, self.posY + self.sizeY, self.posZ + self.sizeZ,
                          block.AIR.id)
        #delete base
        self.mc.setBlocks(self.posX, self.posY - 1, self.posZ,
                          self.posX + self.sizeX, self.posY - 1, self.posZ + self.sizeZ,
                          block.AIR.id)

#END
