import mcpi.minecraft as minecraft
import mcpi.block as block

class block_light:

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
        #state of block -> what skin to be shown
        self.state = 0

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

    def build_block(self):
        #build block
        self.mc.setBlocks(self.posX, self.posY, self.posZ,
                          self.posX + self.sizeX, self.posY + self.sizeY, self.posZ + self.sizeZ,
                          block.FURNACE_INACTIVE.id)
        self.state = 0 # reset state everytime destroyed
        self.postToChat("%s created" %self.name)

    #post string to chat
    def postToChat(self, string):
        self.mc.postToChat("%s: %s " %(self.name, string))

    #update meter scale
    def change_state(self):
        if self.state == 0:
            #build state 1 block
            self.mc.setBlocks(self.posX, self.posY, self.posZ,
                              self.posX + self.sizeX, self.posY + self.sizeY, self.posZ + self.sizeZ,
                              block.FURNACE_ACTIVE.id)
            self.state = 1
            self.postToChat("turn on")
        elif self.state == 1:
            #build state 1 block
            self.mc.setBlocks(self.posX, self.posY, self.posZ,
                              self.posX + self.sizeX, self.posY + self.sizeY, self.posZ + self.sizeZ,
                              block.FURNACE_INACTIVE.id)
            self.postToChat("turn off")
            self.state = 0
        
    #delete previous block
    def block_delete(self):
        #delete block
        self.mc.setBlocks(self.posX, self.posY, self.posZ,
                          self.posX + self.sizeX, self.posY + self.sizeY, self.posZ + self.sizeZ,
                          block.AIR.id)

#END
