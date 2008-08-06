#! /usr/bin/env python
# -*- Python -*-
###########################################################################

#                        --------------------                             #

#  copyright            : Giuseppe "denever" Martino                      #
#  email                : denever@users.sf.net                            #
###########################################################################
###########################################################################
#                                                                         #
#   This program is free software; you can redistribute it and/or modify  #
#   it under the terms of the GNU General Public License as published by  #
#   the Free Software Foundation; either version 2 of the License, or     #
#   (at your option) any later version.                                   #
#                                                                         #
#  This program is distributed in the hope that it will be useful,        #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of         #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
#  GNU General Public License for more details.                           #
#                                                                         #
#  You should have received a copy of the GNU General Public License      #
#  along with this program; if not, write to the Free Software            #
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,             #
#  MA 02110-1301 USA                                                      #
#                                                                         #
###########################################################################

import pygtk

pygtk.require('2.0')

import gtk

from gtk import *
from gtk import glade

gdk.threads_init()

class Gui:
    def __init__(self):
        self.wtree = glade.XML('glade/mainwindow.glade')
        self.wtree.get_widget('main_window').connect("destroy", main_quit)
    	self.wtree.get_widget('main_window').show()        
 	dict = {}
	for key in dir(self.__class__):
	    dict[key] = getattr(self, key)
	self.wtree.signal_autoconnect(dict)

    def on_mit_exit_activate(self, widget):
        gtk.main_quit()

    def on_mit_new_activate(self, widget):
        print 'new'

    def on_mit_setdim_activate(self, widget):
        self.wtree.get_widget('dlg_setdim').show()
        
    def on_mit_setstep_activate(self, widget):
        self.wtree.get_widget('dlg_setstep').show()

    def on_mit_setseed_activate(self, widget):
        self.wtree.get_widget('dlg_setseed').show()

    def on_mit_addnode_activate(self, widget):
        print 'addnode'

    def on_mit_addnodegroup_activate(self, widget):
        print 'addnodegroup'

    def on_btn_setdim_canc_clicked(self, widget):
        self.wtree.get_widget('dlg_setdim').hide()

    def on_btn_setdim_apply_clicked(self, widget):
        print self.wtree.get_widget('hsl_dimx').get_value()
        self.wtree.get_widget('dlg_setdim').hide()

    def on_btn_setstep_canc_clicked(self, widget):
        self.wtree.get_widget('dlg_setstep').hide()

    def on_btn_setstep_apply_clicked(self, widget):
        print self.wtree.get_widget('hsl_step').get_value()
        self.wtree.get_widget('dlg_setstep').hide()

    def on_btn_setseed_canc_clicked(self, widget):
        self.wtree.get_widget('dlg_setseed').hide()

    def on_btn_setseed_apply_clicked(self, widget):
        print self.wtree.get_widget('hsl_seed').get_value()
        self.wtree.get_widget('dlg_setseed').hide()

if __name__ == "__main__":
    gui = Gui()
    main()
