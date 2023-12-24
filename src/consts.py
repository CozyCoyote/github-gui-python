import wx

WINDOWS_SIZE = (800,400)

PADDING = 16

LEFT_PADDING = wx.SizerFlags().Border(wx.LEFT, PADDING)
RIGHT_PADDING = wx.SizerFlags().Border(wx.RIGHT, PADDING)
TOP_PADDING = wx.SizerFlags().Border(wx.TOP, PADDING)
LEFT_TOP_PADDING = wx.SizerFlags().Border(wx.TOP|wx.LEFT, PADDING)
