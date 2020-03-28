# Author murphy
# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"功能页", pos = wx.DefaultPosition, size = wx.Size( 300,250 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"添加", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"修改", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"查询", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button7 = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer1.Add(self.m_button7, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button3.Bind( wx.EVT_BUTTON, self.add )
		self.m_button4.Bind( wx.EVT_BUTTON, self.delete )
		self.m_button5.Bind( wx.EVT_BUTTON, self.update )
		self.m_button6.Bind( wx.EVT_BUTTON, self.select )
		self.m_button7.Bind(wx.EVT_BUTTON, self.exit)

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def add( self, event ):
		event.Skip()

	def delete( self, event ):
		event.Skip()

	def update( self, event ):
		event.Skip()

	def select( self, event ):
		event.Skip()

	def exit(self,event):
		event.Skip()

