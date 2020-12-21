import json
import time
import re

# Do we have a valid tuner (short) RX command
#
def isValidTunerRxCommand(shortCommand):
  if (shortCommand in ['A', 'B', 'D', 'F', 'L', 'M', 'O', 'Q', 'S', 'T', 'V', 'W', 'X', 'Z']):
    return True
  else:
    return False


# Do we have a valid board (short) RX command?
#
def isValidBoardRxCommand(boardCommand):
  if (boardCommand in ['BLO', 'BLB', 'BHB', 'BPB']):
    return True
  else:
    return False


# Converts board RX command to dictionary index
#
def convertBoardRxShortCommand(shortCommand):
  switcher = {
    'BLO' : 'localOscillatorMHz',
    'BLB' : 'bandEdgeLowMHz',
    'BHB' : 'bandEdgeHighMHz',
    'BPB' : 'preAmpOffsetDb'
  }
  return switcher.get(shortCommand, '')


# Converts short 1-letter command to dictionary index
#
def convertTunerRxShortCommand(shortCommand):
  switcher = {
    'A' : 'mutingMode',
    'B' : 'bandWidthMode',
    'D' : 'rdsStatus',
    'F' : 'Frequency',
    'L' : 'Volume',
    'M' : 'stereoStatus',
    'O' : 'tuneStatus',
    'Q' : 'squelshStatus',
    'S' : 'signalLevel',
    'T' : 'rdsName',
    'V' : 'deviationOverload',
    'W' : 'bandWidthKHz',
    'X' : 'muteStatus',
    'Z' : 'stereoMode'
  }
  return switcher.get(shortCommand, '')


# TunerBoard class
#
class tunerBoard:
  def __init__(self):
    self.tuners = {}
    self.tuners['uuid'] = '34e756f4-3ae9-11eb-8d59-c31c5c810982'
    self.tuners['timeStamp'] = str(time.time())
    self.tuners['localOscillatorMHz'] = 0
    self.tuners['bandEdgeLowMHz'] = 0
    self.tuners['bandEdgeHighMHz'] = 0
    self.tuners['preAmpOffsetDb'] = ""
    self.tuners['tuners'] = {}

    # Build dictionary for 4 tuners
    for x in range(1, 5):
      self.tuners['tuners'][x] = {}
      self.tuners['tuners'][x]['Frequency'] = ""
      self.tuners['tuners'][x]['bandWidthKHz'] = 0
      self.tuners['tuners'][x]['bandWidthMode'] = 0
      self.tuners['tuners'][x]['rdsStatus'] = 0
      self.tuners['tuners'][x]['rdsName'] = ""
      self.tuners['tuners'][x]['tuneStatus'] = 0
      self.tuners['tuners'][x]['stereoStatus'] = 0
      self.tuners['tuners'][x]['stereoMode'] = 0
      self.tuners['tuners'][x]['squelshStatus'] = 0
      self.tuners['tuners'][x]['mutingMode'] = 0
      self.tuners['tuners'][x]['Volume'] = 0
      self.tuners['tuners'][x]['signalLevel'] = 0
      self.tuners['tuners'][x]['deviationOverload'] = 0
      self.tuners['tuners'][x]['muteStatus'] = 0

  # Update timestamp
  #
  def updateTimeStamp(self):
    self.tuners['timeStamp'] = str(time.time())

  # Check for valid tuner commands and set dictionary values accordingly
  #
  def parseRXtuners(self, data):
    pattern=re.compile(r'\<T([\d])([\w])([\w\s\.,\-]+)\>')
    for c in re.finditer(pattern, data):

      # Do we have valid data in the buffer?
      if (c):
        tunerid=int(c.group(1))
        command=c.group(2)
        value=c.group(3)

        if (isValidTunerRxCommand):
          self.tuners['tuners'][tunerid][convertTunerRxShortCommand(command)] = value
          #print ("Short:",command, "Long:", convertTunerRxShortCommand(command), "Value:", value)


  # Check for valid board commands and set dictionary values accordingly
  #
  def parseRXboard(self, data):
    pattern=re.compile(r'\<(B[\w]{2})([\w\s]+)\>')
    for c in re.finditer(pattern, data):

      # Do we have valid data?
      if (c):
        command=c.group(1)
        value=c.group(2)
        if (isValidBoardRxCommand(command)):
          self.tuners[convertBoardRxShortCommand(command)] = value
          #print ("Data:", convertBoardRxShortCommand(command), "Value:", value)


  # Check for valid timer message (<TIMR>)
  #
  def parseTIMER(self, data):
    c=re.search(r'\<(TIMR)\>', data)

    # Do we have valid data?
    if (c):
      return True
    else:
      return False
