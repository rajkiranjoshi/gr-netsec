#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2017 NetSec-Grp.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import pmt
from gnuradio import gr


class string_to_pmt(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """[NetSec] A simple block that takes in a string and converts it to a pmt object. Also adds a static LLC header."""

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='String to PMT',   # will show up in GRC
            in_sig=None,
            out_sig=None
        )
        # fixed static llc header
        self.llc_str = "\xaa\xaa\x03\x00\x00\x00\x00\x00" # 8 bytes - last 2 bytes usually indicate ipv4 type i.e. 0x0800

        self.message_port_register_out(pmt.intern('pmt'))
        self.message_port_register_in(pmt.intern('string'))
        self.set_msg_handler(pmt.intern('string'),self.handle_msg)

    def handle_msg(self, msg):
        msg_str = str(msg)
        final_msg = self.llc_str + msg_str
        self.message_port_pub(pmt.intern('pmt'),pmt.intern(final_msg))
