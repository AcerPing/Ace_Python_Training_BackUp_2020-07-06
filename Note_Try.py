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
## Class Main_Frame
###########################################################################

class Main_Frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 967,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.Main_Frame_menubar_File = wx.MenuBar( 0 )
		self.menu_selection_File = wx.Menu()
		self.menuItem_Name_Build = wx.MenuItem( self.menu_selection_File, wx.ID_ANY, u"建立檔案(清空) 消します", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_selection_File.Append( self.menuItem_Name_Build )

		self.menuItem_Name_OpenFile = wx.MenuItem( self.menu_selection_File, wx.ID_ANY, u"開啟檔案　ファイルを開けます", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_selection_File.Append( self.menuItem_Name_OpenFile )

		self.menuItem_Name_SaveFile = wx.MenuItem( self.menu_selection_File, wx.ID_ANY, u"儲存檔案　ファイルを貯める", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_selection_File.Append( self.menuItem_Name_SaveFile )

		self.menuItem_Name_Exit = wx.MenuItem( self.menu_selection_File, wx.ID_ANY, u"關閉程式　閉じる", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_selection_File.Append( self.menuItem_Name_Exit )

		self.Main_Frame_menubar_File.Append( self.menu_selection_File, u"檔案　ファイル" )

		self.Main_Frame_menu_Author = wx.Menu()
		self.menuItem_Name_Author = wx.MenuItem( self.Main_Frame_menu_Author, wx.ID_ANY, u"作者介紹　作者に関する", wx.EmptyString, wx.ITEM_NORMAL )
		self.Main_Frame_menu_Author.Append( self.menuItem_Name_Author )

		self.Main_Frame_menubar_File.Append( self.Main_Frame_menu_Author, u"關於 関する" )

		self.SetMenuBar( self.Main_Frame_menubar_File )

		Main_Frame_Layout = wx.FlexGridSizer( 0, 2, 0, 0 )
		Main_Frame_Layout.SetFlexibleDirection( wx.BOTH )
		Main_Frame_Layout.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 967,600 ), wx.TE_MULTILINE|wx.TE_PROCESS_ENTER )
		Main_Frame_Layout.Add( self.textCtrl, 1, wx.ALL|wx.EXPAND, 5 )

		self.Main_Frame_Scrolled = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.Main_Frame_Scrolled.SetScrollRate( 5, 5 )
		Main_Frame_Layout.Add( self.Main_Frame_Scrolled, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( Main_Frame_Layout )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.menu_Function_Build, id = self.menuItem_Name_Build.GetId() )
		self.Bind( wx.EVT_MENU, self.menuItem_Function_OpenFile, id = self.menuItem_Name_OpenFile.GetId() )
		self.Bind( wx.EVT_MENU, self.menuItem_Function_SaveFile, id = self.menuItem_Name_SaveFile.GetId() )
		self.Bind( wx.EVT_MENU, self.menuItem_Function_Exit, id = self.menuItem_Name_Exit.GetId() )
		self.Bind( wx.EVT_MENU, self.menuItem_Functione_Author, id = self.menuItem_Name_Author.GetId() )
		self.textCtrl.Bind( wx.EVT_SIZE, self.FrameSize )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def menu_Function_Build( self, event ):
		event.Skip()

	def menuItem_Function_OpenFile( self, event ):
		event.Skip()

	def menuItem_Function_SaveFile( self, event ):
		event.Skip()

	def menuItem_Function_Exit( self, event ):
		event.Skip()

	def menuItem_Functione_Author( self, event ):
		event.Skip()

	def FrameSize( self, event ):
		event.Skip()


###########################################################################
## Class Frame_Author
###########################################################################

class Frame_Author ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 966,404 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		Frame_Author_Layout = wx.BoxSizer( wx.VERTICAL )

		self.staticText_Enter_1 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Enter_1.Wrap( -1 )

		Frame_Author_Layout.Add( self.staticText_Enter_1, 0, wx.ALL, 5 )

		self.staticText_Name_CH = wx.StaticText( self, wx.ID_ANY, u"作者：何哲平", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Name_CH.Wrap( -1 )

		self.staticText_Name_CH.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" ) )

		Frame_Author_Layout.Add( self.staticText_Name_CH, 0, wx.ALL, 5 )

		self.staticText_Email_CH = wx.StaticText( self, wx.ID_ANY, u"信箱：acerping0805@gmail.com", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Email_CH.Wrap( -1 )

		self.staticText_Email_CH.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "微軟正黑體" ) )

		Frame_Author_Layout.Add( self.staticText_Email_CH, 0, wx.ALL, 5 )

		self.staticText_Enter_2 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Enter_2.Wrap( -1 )

		Frame_Author_Layout.Add( self.staticText_Enter_2, 0, wx.ALL, 5 )

		self.staticText_Name_JP = wx.StaticText( self, wx.ID_ANY, u"私は何哲平と申します", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Name_JP.Wrap( -1 )

		self.staticText_Name_JP.SetFont( wx.Font( 24, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "新細明體" ) )

		Frame_Author_Layout.Add( self.staticText_Name_JP, 0, wx.ALL, 5 )

		self.staticText_Email_JP = wx.StaticText( self, wx.ID_ANY, u"メールアドレス：acerping0805@gmail.com", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Email_JP.Wrap( -1 )

		self.staticText_Email_JP.SetFont( wx.Font( 24, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "新細明體" ) )

		Frame_Author_Layout.Add( self.staticText_Email_JP, 0, wx.ALL, 5 )

		self.staticText_Enter_3 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Enter_3.Wrap( -1 )

		Frame_Author_Layout.Add( self.staticText_Enter_3, 0, wx.ALL, 5 )

		self.staticText_Last = wx.StaticText( self, wx.ID_ANY, u"どうぞよろしくお願いいたします。", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Last.Wrap( -1 )

		self.staticText_Last.SetFont( wx.Font( 24, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "新細明體" ) )

		Frame_Author_Layout.Add( self.staticText_Last, 0, wx.ALL, 5 )


		self.SetSizer( Frame_Author_Layout )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


