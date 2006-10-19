#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
# generated by wxGlade 0.4cvs on Fri Oct  6 01:22:16 2006

import sys
import os
import wx
import mp3Info

TRACK_MODE = 1
ALBUM_MODE = 2
MANUAL_MODE = 3

class mainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: mainFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_2 = wx.Panel(self, -1)
        self.panel_1 = wx.Panel(self, -1)
        
        # Menu Bar
        self.mainMenu = wx.MenuBar()
        self.SetMenuBar(self.mainMenu)
        global ID_MENU_ADD_FILES; ID_MENU_ADD_FILES = wx.NewId()
        global ID_MENU_ADD_FOLDER; ID_MENU_ADD_FOLDER = wx.NewId()
        global ID_MENU_CLEAR_FILES; ID_MENU_CLEAR_FILES = wx.NewId()
        global ID_MENU_CLEAR_ALL; ID_MENU_CLEAR_ALL = wx.NewId()
        global ID_MENU_MODE_TRACK; ID_MENU_MODE_TRACK = wx.NewId()
        global ID_MENU_MODE_ALBUM; ID_MENU_MODE_ALBUM = wx.NewId()
        global ID_MENU_MODE_MANUAL; ID_MENU_MODE_MANUAL = wx.NewId()
        global ID_MENU_TRACK_ANALYSIS; ID_MENU_TRACK_ANALYSIS = wx.NewId()
        global ID_MENU_ALBUM_ANALYSIS; ID_MENU_ALBUM_ANALYSIS = wx.NewId()
        global ID_MENU_TRACK_GAIN; ID_MENU_TRACK_GAIN = wx.NewId()
        global ID_MENU_ALBUM_GAIN; ID_MENU_ALBUM_GAIN = wx.NewId()
        global ID_MENU_MANUAL_GAIN; ID_MENU_MANUAL_GAIN = wx.NewId()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(ID_MENU_ADD_FILES, "Add Files", "Add mp3 files to list", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(ID_MENU_ADD_FOLDER, "Add Folder", "Add all mp3 files in a folder", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(ID_MENU_CLEAR_FILES, "Clear files", "Remove selected files from list", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(ID_MENU_CLEAR_ALL, "Clear all files", "Remove all files from list", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(wx.ID_EXIT, "E&xit", "Quit this program", wx.ITEM_NORMAL)
        self.mainMenu.Append(wxglade_tmp_menu, "&File")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(ID_MENU_MODE_TRACK, "&Track", "\"Track\" analysis and gain", wx.ITEM_RADIO)
        wxglade_tmp_menu.Append(ID_MENU_MODE_ALBUM, "&Album", "\"Album\" analysis and gain", wx.ITEM_RADIO)
        wxglade_tmp_menu.Append(ID_MENU_MODE_MANUAL, "&Manual", "Manual gain change", wx.ITEM_RADIO)
        self.mainMenu.Append(wxglade_tmp_menu, "&Mode")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(ID_MENU_TRACK_ANALYSIS, "Track Analysis", "Calculate ReplayGain for each mp3 file", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(ID_MENU_ALBUM_ANALYSIS, "Album Analysis", "Calculate ReplayGain for each folder", wx.ITEM_NORMAL)
        self.mainMenu.Append(wxglade_tmp_menu, "Analysis")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(ID_MENU_TRACK_GAIN, "Track Gain", "Apply suggested Track gain to each file", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(ID_MENU_ALBUM_GAIN, "Album Gain", "Apply suggested Album gain to each folder", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(ID_MENU_MANUAL_GAIN, "Manual Gain", "Apply user-selected gain change to each file", wx.ITEM_NORMAL)
        self.mainMenu.Append(wxglade_tmp_menu, "Gain")
        # Menu Bar end
        self.mainStatusbar = self.CreateStatusBar(1, 0)
        
        # Tool Bar
        self.mainToolbar = wx.ToolBar(self, -1, style=wx.TB_HORIZONTAL|wx.TB_FLAT|wx.TB_TEXT)
        self.SetToolBar(self.mainToolbar)
        global ID_TOOL_ADD_FILES; ID_TOOL_ADD_FILES = wx.NewId()
        global ID_TOOL_ADD_FOLDER; ID_TOOL_ADD_FOLDER = wx.NewId()
        global ID_TOOL_ANALYZE; ID_TOOL_ANALYZE = wx.NewId()
        global ID_TOOL_GAIN; ID_TOOL_GAIN = wx.NewId()
        global ID_TOOL_CLEAR_FILES; ID_TOOL_CLEAR_FILES = wx.NewId()
        global ID_TOOL_CLEAR_ALL; ID_TOOL_CLEAR_ALL = wx.NewId()
        global ID_TOOL_CANCEL; ID_TOOL_CANCEL = wx.NewId()
        self.mainToolbar.AddLabelTool(ID_TOOL_ADD_FILES, "Add Files", wx.Bitmap("res/big_add_files.xpm", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Add mp3 files to list", "Add mp3 files to list")
        self.mainToolbar.AddLabelTool(ID_TOOL_ADD_FOLDER, "Add Folder", wx.Bitmap("res/big_add_folder.xpm", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Add all mp3 files in a folder", "Add all mp3 files in a folder")
        self.mainToolbar.AddSeparator()
        self.mainToolbar.AddLabelTool(ID_TOOL_ANALYZE, "Track Analysis", wx.Bitmap("res/big_scan_radio.xpm", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Do ReplayGain analysis on files", "Do ReplayGain analysis on files")
        self.mainToolbar.AddLabelTool(ID_TOOL_GAIN, "Track Gain", wx.Bitmap("res/big_adjust_radio.xpm", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Change volume of files", "Change volume of files")
        self.mainToolbar.AddSeparator()
        self.mainToolbar.AddLabelTool(ID_TOOL_CLEAR_FILES, "Clear Files", wx.Bitmap("res/big_remove_files.xpm", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Remove selected files from list", "Remove selected files from list")
        self.mainToolbar.AddLabelTool(ID_TOOL_CLEAR_ALL, "Clear All", wx.Bitmap("res/big_remove_all.xpm", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Remove all files from list", "Remove all files from list")
        self.mainToolbar.AddSeparator()
        self.mainToolbar.AddLabelTool(ID_TOOL_CANCEL, "Cancel", wx.Bitmap("res/big_stop.xpm", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Cancel current processing", "Cancel current processing")
        # Tool Bar end
        self.static_line_1 = wx.StaticLine(self, -1)
        self.targetLabel = wx.StaticText(self.panel_1, -1, "Target \"Normal\" Volume:")
        global ID_SLIDER_VOLUME; ID_SLIDER_VOLUME = wx.NewId()
        self.volumeSlider = wx.Slider(self.panel_1, ID_SLIDER_VOLUME, 890, 800, 1050)
        global ID_LABEL_VOLUME; ID_LABEL_VOLUME = wx.NewId()
        self.volumeLabel = wx.StaticText(self.panel_1, ID_LABEL_VOLUME, "100.0 dB")
        self.mainList = wx.ListCtrl(self, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.fileProgressLabel = wx.StaticText(self.panel_2, -1, "File Progress:")
        self.fileProgress = wx.Gauge(self.panel_2, -1, 100)
        self.totalProgressLabel = wx.StaticText(self.panel_2, -1, "Total Progress:")
        self.totalProgress = wx.Gauge(self.panel_2, -1, 100)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.OnAddFiles, id=ID_MENU_ADD_FILES)
        self.Bind(wx.EVT_MENU, self.OnAddFolder, id=ID_MENU_ADD_FOLDER)
        self.Bind(wx.EVT_MENU, self.OnClearFiles, id=ID_MENU_CLEAR_FILES)
        self.Bind(wx.EVT_MENU, self.OnClearAll, id=ID_MENU_CLEAR_ALL)
        self.Bind(wx.EVT_MENU, self.OnExit, id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.OnModeChange, id=ID_MENU_MODE_TRACK)
        self.Bind(wx.EVT_MENU, self.OnModeChange, id=ID_MENU_MODE_ALBUM)
        self.Bind(wx.EVT_MENU, self.OnModeChange, id=ID_MENU_MODE_MANUAL)
        self.Bind(wx.EVT_MENU, self.OnTrackAnalysis, id=ID_MENU_TRACK_ANALYSIS)
        self.Bind(wx.EVT_MENU, self.OnAlbumAnalysis, id=ID_MENU_ALBUM_ANALYSIS)
        self.Bind(wx.EVT_MENU, self.OnTrackGain, id=ID_MENU_TRACK_GAIN)
        self.Bind(wx.EVT_MENU, self.OnAlbumGain, id=ID_MENU_ALBUM_GAIN)
        self.Bind(wx.EVT_MENU, self.OnManualGain, id=ID_MENU_MANUAL_GAIN)
        self.Bind(wx.EVT_TOOL, self.OnAddFiles, id=ID_TOOL_ADD_FILES)
        self.Bind(wx.EVT_TOOL, self.OnAddFolder, id=ID_TOOL_ADD_FOLDER)
        self.Bind(wx.EVT_TOOL, self.OnAnalysisButton, id=ID_TOOL_ANALYZE)
        self.Bind(wx.EVT_TOOL, self.OnGainButton, id=ID_TOOL_GAIN)
        self.Bind(wx.EVT_TOOL, self.OnClearFiles, id=ID_TOOL_CLEAR_FILES)
        self.Bind(wx.EVT_TOOL, self.OnClearAll, id=ID_TOOL_CLEAR_ALL)
        self.Bind(wx.EVT_TOOL, self.OnCancel, id=ID_TOOL_CANCEL)
        self.Bind(wx.EVT_COMMAND_SCROLL, self.OnVolumeChange, id=ID_SLIDER_VOLUME)
        # end wxGlade

        self.mode = TRACK_MODE
        self.trackGainIcon = wx.Bitmap("res/big_adjust_radio.xpm", wx.BITMAP_TYPE_ANY)
        self.trackAnalysisIcon = wx.Bitmap("res/big_scan_radio.xpm", wx.BITMAP_TYPE_ANY)
        self.albumGainIcon = wx.Bitmap("res/big_adjust_album.xpm", wx.BITMAP_TYPE_ANY)
        self.albumAnalysisIcon = wx.Bitmap("res/big_scan_album.xpm", wx.BITMAP_TYPE_ANY)
        self.manualGainIcon = wx.Bitmap("res/big_adjust_constant.xpm", wx.BITMAP_TYPE_ANY)

    def __set_properties(self):
        # begin wxGlade: mainFrame.__set_properties
        self.SetTitle("MP3Gain")
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap("res/mp3gain.xpm", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetSize((629, 476))
        self.mainStatusbar.SetStatusWidths([-1])
        # statusbar fields
        mainStatusbar_fields = ["Ready"]
        for i in range(len(mainStatusbar_fields)):
            self.mainStatusbar.SetStatusText(mainStatusbar_fields[i], i)
        self.mainToolbar.SetToolBitmapSize((48, 48))
        self.mainToolbar.Realize()
        # end wxGlade

        self.mainList.InsertColumn(0,"Path/File")
        self.mainList.InsertColumn(1,"Volume")
        self.mainList.InsertColumn(2,"clipping")
        self.mainList.InsertColumn(3,"Track Gain")
        self.mainList.InsertColumn(4,"clip(Track)")
        self.mainList.InsertColumn(5,"Album Volume")
        self.mainList.InsertColumn(6,"Album Gain")
        self.mainList.InsertColumn(7,"clip(Album)")

        self.EnableStuff(True)
        self.mp3s = {}

    def __do_layout(self):
        # begin wxGlade: mainFrame.__do_layout
        mainSplit = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(2, 2, 0, 0)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        mainSplit.Add(self.static_line_1, 0, wx.EXPAND, 0)
        sizer_2.Add(self.targetLabel, 0, 0, 0)
        sizer_2.Add(self.volumeSlider, 1, wx.EXPAND, 0)
        sizer_2.Add(self.volumeLabel, 0, 0, 0)
        self.panel_1.SetAutoLayout(True)
        self.panel_1.SetSizer(sizer_2)
        sizer_2.Fit(self.panel_1)
        sizer_2.SetSizeHints(self.panel_1)
        mainSplit.Add(self.panel_1, 0, wx.EXPAND, 0)
        mainSplit.Add(self.mainList, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.fileProgressLabel, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.fileProgress, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.totalProgressLabel, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.totalProgress, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        self.panel_2.SetAutoLayout(True)
        self.panel_2.SetSizer(grid_sizer_1)
        grid_sizer_1.Fit(self.panel_2)
        grid_sizer_1.SetSizeHints(self.panel_2)
        grid_sizer_1.AddGrowableCol(1)
        mainSplit.Add(self.panel_2, 0, wx.EXPAND, 0)
        self.SetAutoLayout(True)
        self.SetSizer(mainSplit)
        self.Layout()
        # end wxGlade
        self.ChangeVolumeLabel()

    def NotImpYet(self, msg):
        d = wx.MessageDialog(self, "Event handler '"+msg+"' not implemented yet!", "Not implemented", wx.OK)
        d.ShowModal()
        d.Destroy()
        
    def OnAddFiles(self, event): # wxGlade: mainFrame.<event_handler>
        d = wx.FileDialog(self, "Choose mp3 files", "", "", "MP3 files (*.mp3)|*.mp3", wx.OPEN|wx.MULTIPLE|wx.CHANGE_DIR)
        if d.ShowModal() == wx.ID_CANCEL:
            return

        paths = d.GetPaths()
        for p in paths:
            self.AddFileToList(p)
        d.Destroy()
        
        self.EnableStuff(True)
        
            

    def OnAddFolder(self, event): # wxGlade: mainFrame.<event_handler>
        dirHome = wx.GetHomeDir()
        d = wx.DirDialog(self, "Choose an mp3 folder")

        if d.ShowModal() == wx.ID_OK:
            self.cancelProcessing = False
            self.EnableStuff(False)
            os.path.walk(d.GetPath(), self.AddFolder, None)
            self.EnableStuff(True)
            
        self.mainStatusbar.SetStatusText("")

    def OnClearFiles(self, event): # wxGlade: mainFrame.<event_handler>
        idx = self.mainList.GetFirstSelected()
        while idx != -1:
            del self.mp3s[self.mainList.GetItemText(idx)]
            self.mainList.DeleteItem(idx)
            idx = self.mainList.GetNextSelected(idx - 1)
            # need to check from idx - 1 in case the very next one in line
            # is selected-- thusly when the current idx is deleted, the next
            # one shifs up so that it's in the just-deleted one's idx spot

        self.EnableStuff(True)

    def OnClearAll(self, event): # wxGlade: mainFrame.<event_handler>
        self.mp3s = {}
        self.mainList.DeleteAllItems()
        self.EnableStuff(True)

    def OnExit(self, event): # wxGlade: mainFrame.<event_handler>
        self.cancelProcessing = True
        self.Close()

    def OnModeChange(self, event): # wxGlade: mainFrame.<event_handler>
        tb = self.mainToolbar
        
        tb.DeleteTool(ID_TOOL_ANALYZE)
        tb.DeleteTool(ID_TOOL_GAIN)

        id = event.GetId()
        if id == ID_MENU_MODE_TRACK:
            tb.InsertLabelTool(3,ID_TOOL_GAIN, "Track Gain", self.trackGainIcon, wx.NullBitmap, wx.ITEM_NORMAL, "Change volume of files", "Change volume of files")
            tb.InsertLabelTool(3,ID_TOOL_ANALYZE, "Track Analysis", self.trackAnalysisIcon, wx.NullBitmap, wx.ITEM_NORMAL, "Do ReplayGain analysis on files", "Do ReplayGain analysis on files")
            self.mode = TRACK_MODE
        elif id == ID_MENU_MODE_ALBUM:
            tb.InsertLabelTool(3,ID_TOOL_GAIN, "Album Gain", self.albumGainIcon, wx.NullBitmap, wx.ITEM_NORMAL, "Change volume of files", "Change volume of files")
            tb.InsertLabelTool(3,ID_TOOL_ANALYZE, "Album Analysis", self.albumAnalysisIcon, wx.NullBitmap, wx.ITEM_NORMAL, "Do ReplayGain analysis on files", "Do ReplayGain analysis on files")
            self.mode = ALBUM_MODE
        else:
            tb.InsertLabelTool(3,ID_TOOL_GAIN, "Manual Gain", self.manualGainIcon, wx.NullBitmap, wx.ITEM_NORMAL, "Change volume of files", "Change volume of files")
            self.mode = MANUAL_MODE
            
        tb.Realize()

        self.EnableStuff(True)


    def OnAnalysisButton(self, event): # wxGlade: mainFrame.<event_handler>
        if self.mode == TRACK_MODE:
            self.OnTrackAnalysis(event)
        else:
            self.OnAlbumAnalysis(event)

    def OnGainButton(self, event): # wxGlade: mainFrame.<event_handler>
        if self.mode == TRACK_MODE:
            self.OnTrackGain(event)
        elif self.mode == ALBUM_MODE:
            self.OnAlbumGain(event)
        else:
            self.OnManualGain(event)

    def OnTrackAnalysis(self, event): # wxGlade: mainFrame.<event_handler>
        print "Event handler `OnTrackAnalysis' not implemented!"
        event.Skip()

    def OnAlbumAnalysis(self, event): # wxGlade: mainFrame.<event_handler>
        print "Event handler `OnAlbumAnalysis' not implemented!"
        event.Skip()

    def OnTrackGain(self, event): # wxGlade: mainFrame.<event_handler>
        print "Event handler `OnTrackGain' not implemented!"
        event.Skip()

    def OnAlbumGain(self, event): # wxGlade: mainFrame.<event_handler>
        print "Event handler `OnAlbumGain' not implemented!"
        event.Skip()

    def OnManualGain(self, event): # wxGlade: mainFrame.<event_handler>
        print "Event handler `OnManualGain' not implemented!"
        event.Skip()

    def OnCancel(self, event): # wxGlade: mainFrame.<event_handler>
        self.cancelProcessing = True
        self.mainToolbar.EnableTool(ID_TOOL_CANCEL, False)
        self.mainStatusbar.SetStatusText("Cancelling...")

    def OnVolumeChange(self, event): # wxGlade: mainFrame.<event_handler>
        self.ChangeVolumeLabel()

    def ChangeVolumeLabel(self):
        targetVolume = self.volumeSlider.GetValue() / 10.0
        self.volumeLabel.SetLabel("%0.1f dB" % targetVolume)

    def AddFileToList(self, path):
        if not path.lower().endswith('.mp3'):
            return
        if path in self.mp3s:
            return
        
        self.mp3s[path] = mp3Info.mp3Info()
        
        idx = self.mainList.InsertStringItem(sys.maxint, path)
        self.mainList.SetStringItem(idx, 1, "88.2")
        self.mainList.SetStringItem(idx, 3, "1.5")
        self.mainList.SetStringItem(idx, 5, "101.3")
        self.mainList.SetStringItem(idx, 6, "-12.0")

    def AddFolder(self, ignore, dr, flst):
        if self.cancelProcessing:
            flst[:] = []
            return

        self.mainStatusbar.SetStatusText(dr)
        for f in flst:
            fullf = os.path.join(dr, f)
            if os.path.islink(fullf):
                break
            if os.path.isfile(fullf):
                self.AddFileToList(fullf)
            wx.Yield()
        
    def EnableStuff(self, enable):
        tb = self.mainToolbar
        mn = self.mainMenu

        tb.EnableTool(ID_TOOL_ADD_FILES, enable)
        tb.EnableTool(ID_TOOL_ADD_FOLDER, enable)
        tb.EnableTool(ID_TOOL_CANCEL, not enable)
        mn.Enable(ID_MENU_ADD_FILES, enable)
        mn.Enable(ID_MENU_ADD_FOLDER, enable)
        mn.Enable(ID_MENU_MODE_TRACK, enable)
        mn.Enable(ID_MENU_MODE_ALBUM, enable)
        mn.Enable(ID_MENU_MODE_MANUAL, enable)

        if self.mainList.GetItemCount() == 0:
            tb.EnableTool(ID_TOOL_ANALYZE, False)
            tb.EnableTool(ID_TOOL_GAIN, False)
            tb.EnableTool(ID_TOOL_CLEAR_FILES, False)
            tb.EnableTool(ID_TOOL_CLEAR_ALL, False)
            mn.Enable(ID_MENU_TRACK_ANALYSIS, False)
            mn.Enable(ID_MENU_ALBUM_ANALYSIS, False)
            mn.Enable(ID_MENU_TRACK_GAIN, False)
            mn.Enable(ID_MENU_ALBUM_GAIN, False)
            mn.Enable(ID_MENU_MANUAL_GAIN, False)
            mn.Enable(ID_MENU_CLEAR_FILES, False)
            mn.Enable(ID_MENU_CLEAR_ALL, False)
        else:
            tb.EnableTool(ID_TOOL_ANALYZE, enable)
            tb.EnableTool(ID_TOOL_GAIN, enable)
            tb.EnableTool(ID_TOOL_CLEAR_FILES, enable)
            tb.EnableTool(ID_TOOL_CLEAR_ALL, enable)
            mn.Enable(ID_MENU_TRACK_ANALYSIS, enable)
            mn.Enable(ID_MENU_ALBUM_ANALYSIS, enable)
            mn.Enable(ID_MENU_TRACK_GAIN, enable)
            mn.Enable(ID_MENU_ALBUM_GAIN, enable)
            mn.Enable(ID_MENU_MANUAL_GAIN, enable)
            mn.Enable(ID_MENU_CLEAR_FILES, enable)
            mn.Enable(ID_MENU_CLEAR_ALL, enable)
            
# end of class mainFrame


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = mainFrame(None, -1, "Woot!")
    frame.Show(1)
    app.MainLoop()
    app.Destroy()
