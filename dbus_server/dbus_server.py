#!/usr/bin/env python3

#########################################################
#            AGILE DBus Protocol Server                 #
#                                                       #
#    Description: Runs the AGILE DBus Protocol defined  #
#       in the AGILE API for the XBee 802.15.4 and XBee #
#       ZigBee protocols.                               #
#    Author: David Palomares <d.palomares@libelium.com> #
#    Version: 0.1                                       #
#    Date: June 2016                                    #
#########################################################

# --- Imports -----------
import sys
from gi.repository import GLib
import dbus
import dbus.service
import dbus.mainloop.glib
from dbus_protocols import dbus_protocol as dbP
from dbus_protocols import dbus_xbee_802_15_4 as xb_802
from dbus_protocols import dbus_xbee_zigbee as xb_zb
# -----------------------


# --- Variables ---------
mainloop = GLib.MainLoop()

# ZigBee
setup_params = {
   "baudrate": 38400,
   "apiMode2": False,
   "NJ": "FF",
   "ZS": "00",
   "EE": "01",
   "SC": "0020"  # set bit 5 only, which means only the 5th channel, starting from 11, i.e. channel 16 (shown as ATCH=0x10)
}
# -----------------------


# --- Classes -----------
class DBusExit(dbus.service.Object):
    
   def __init__(self):
      super().__init__(dbus.SessionBus(), dbP.OBJ_PATH) 
    
   @dbus.service.method(dbP.BUS_NAME, in_signature="", out_signature="")
   def Exit(self):
      mainloop.quit() 
# -----------------------


# --- Functions ---------
def dbusService():
   dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
   dbe = DBusExit()
   xb1 = xb_802.XBee_802_15_4()
   xb2 = xb_zb.XBee_ZigBee()

   # Setup ZB
   xb2._objS0.Setup(dbus.Dictionary(setup_params, signature="sv"))
   xb2._objS0.Connect()

   print("Running DBus service.")
   try:
      mainloop.run()
   except KeyboardInterrupt:
      mainloop.quit()
      print()
      endProgram(0)
   
def endProgram(status):
   print("DBus service stopped.")
   sys.exit(status)
# -----------------------
   

# --- Main program ------
if __name__ == "__main__":
   dbusService()   
   endProgram(0)
# -----------------------

