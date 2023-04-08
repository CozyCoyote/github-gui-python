import wx
import wx.svg
import consts
import settings
import resources

from api import Api


class GithubUiFrame(wx.Frame):
    token = None
    mainPannel = None
    settingsPannel = None
    prContainer = None
    api = Api()

    def __init__(self, *args, **kw):
        super(GithubUiFrame, self).__init__(
            *args, **kw, size=consts.WINDOWS_SIZE)

        pnl = wx.Panel(self)
        self.mainPannel = pnl
        container = wx.BoxSizer(wx.VERTICAL)

        connectButton = wx.Button(pnl)
        connectButton.LabelText = "Connect"
        container.Add(connectButton, consts.LEFT_TOP_PADDING)

        self.ProjectsTabs(pnl=pnl, container=container)

        self.prContainer = wx.BoxSizer(wx.VERTICAL)
        container.Add(self.prContainer, consts.LEFT_TOP_PADDING)



        pnl.SetSizer(container)

        self.makeMenuBar()

        self.Bind(wx.EVT_BUTTON, self.ConnectApi, connectButton)

        self.CreateSettingPannel()

    def makeMenuBar(self):
        settingsMenu = wx.Menu()
        settingsItem = settingsMenu.Append(-1, "&Settings")

        menuBar = wx.MenuBar()
        menuBar.Append(settingsMenu, "&File")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OpenSettings, settingsItem)

    def OpenSettings(self, event):
        # self.settingsPannel.SetPosition((200,50))
        self.mainPannel.Hide()
        self.settingsPannel.Raise()
        self.settingsPannel.Show()

    def CloseSettings(self, event):
        self.mainPannel.Show()
        self.settingsPannel.Hide()

    def CreateSettingPannel(self):
        pnl = wx.Panel(self)

        self.settingsPannel = pnl
        container = wx.BoxSizer(wx.VERTICAL)

        configLabel = wx.StaticText(pnl, label="Configuration")
        container.Add(configLabel, consts.LEFT_TOP_PADDING)

        btn = wx.Button(pnl, label="close[x]")
        btn.ForegroundColour = (255, 0, 0)
        btn.Bind(wx.EVT_BUTTON, self.CloseSettings)
        container.Add(btn, consts.LEFT_TOP_PADDING)

        credentialsRow = wx.BoxSizer(wx.HORIZONTAL)

        self.token = wx.TextCtrl(pnl, size=(300, 24))
        self.token.Hint = "Github token"
        self.token.SetValue(settings.token())
        credentialsRow.Add(self.token)

        saveBtn = wx.Button(pnl)
        saveBtn.LabelText = "Save"
        self.Bind(wx.EVT_BUTTON, self.SaveToken, saveBtn)
        credentialsRow.Add(saveBtn, consts.LEFT_PADDING)

        container.Add(credentialsRow, consts.LEFT_TOP_PADDING)
        pnl.SetSizerAndFit(container)
        pnl.Hide()
        pnl.Raise()
        pnl.CenterOnParent()

    def ProjectsTabs(self, pnl, container):
        if (settings.token != ""):
            self.api.connect()
            favoritesRow = wx.BoxSizer(wx.HORIZONTAL)
            for project in self.api.listRepos():
                print(project)
                favButton = wx.Button(pnl)
                favButton.LabelText = project.name
                favoritesRow.Add(favButton)
                self.Bind(wx.EVT_BUTTON, self.PickFavorite, favButton)
            container.Add(favoritesRow, consts.LEFT_TOP_PADDING)

    def SaveToken(self, event):
        settings.saveToken(self.token.GetLineText(0))

    def ConnectApi(self, event):
        self.api.connect()

    def PickFavorite(self, event):
        sender = event.GetEventObject()
        print(sender.LabelText)
        # self.prContainer.Clear()
        for pr in self.api.listPullRequests("PyGithub/PyGithub"):
            print(pr.title)
            prSizer = wx.BoxSizer(wx.HORIZONTAL)
            prSizer.Add(wx.StaticBitmap(self.mainPannel, bitmap=resources.loadSvg('ic-bug')))
            name = wx.StaticText(self.mainPannel, label=pr.title)
            prSizer.Add(name)
            self.prContainer.Add(prSizer)