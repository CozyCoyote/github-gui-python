import wx.svg

RESOURCE_FOLDER = 'resources'
USER_DATA_FOLDER = 'local-data'

def loadSvg(name):
        icon = wx.svg.SVGimage.CreateFromFile(f'{RESOURCE_FOLDER}/{name}.svg')
        return icon.ConvertToBitmap(scale=0.035, width=24, height=24)
