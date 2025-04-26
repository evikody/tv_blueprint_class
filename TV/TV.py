class TV:
    # Constructor
    def __init__self(self):
        self.channel = 1 # Start the TV Channel on channel 1
        self.volumeLevel = 1 # Start the TV volume level with level 1
        self.on = False # TV is initially turned off

def turn_on(self):
    # Method to turn the TV on
    self.on = True

def turn_off(self):
    # Method to turn the TV off
    self.on = False

def get_channel(self):
    # Method to get the current channel
    return self.channel()

def set_channel(self, channel):
    # Method to set the TV to a new channel
    if self.on and 1 <= channel <= 120: # Only set if the TV is on and the channel is between 1 to 120
        self.channel = channel

def get_volume(self):
    # Method to get the volume level
    return self.volumeLevel

def set_volume(self, volumeLevel):
    # Method to get set the TV to a new volume level
    if self.on and 1 <= volumeLevel <= 7: # Only set if the TV is on and the volume level is  between 1 to 7
        self.volumeLevel = volumeLevel

def channel_up(self):
    # Method to increase the channel by 1
    if self.on and self.channel < 120: # Only increase the channel if the TV is on and the channel is below 120
        self.channel += 1

def channel_down(self):
    # Method to decrease the channel by 1
    if self.on and self.channel > 1: # Only decrease the channel if the TV is on and the channel is greater than 1
        self.channel -= 1

def volume_up(self):
    if self.on and self.volumeLevel < 7:
        self.volumeLevel += 1

def volume_down(self):
    if self.on and self.volumeLevel > 1:
        self.volumeLevel -= 1