# First things, first. Import the wxPython package.
import wx
from main_frame import GithubUiFrame

# Next, create an application object.
app = wx.App()

# Then a frame.
frm = GithubUiFrame(None, title="Hello World")

# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()