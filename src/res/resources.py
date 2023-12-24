import wx.svg

RESOURCE_FOLDER = 'resources'
USER_DATA_FOLDER = 'local-data'

def loadSvg(name, scale, width = 24, height = 24):
        icon = wx.svg.SVGimage.CreateFromFile(f'{RESOURCE_FOLDER}/{name}.svg')
        return icon.ConvertToBitmap(scale=scale, width=width, height=height)
