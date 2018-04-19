import wx
import chatbot as bot
import wx.grid
import utils

class BotFrame(wx.Frame):

    def __init__(self, *args, **kw):

        super(BotFrame, self).__init__(*args, **kw)

        self.pnl = wx.Panel(self)
        st = wx.StaticText(self.pnl, label="Mayuri BOT", pos=(25,25))
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        self.makeMenuBar()
        self.make_buttons()

        self.CreateStatusBar()
        self.SetStatusText("Aguardando...")
        self.Centre()


    def change_status(self, msg):
        if msg != '':
            self.SetStatusText(msg)

    def ini_bot(self):
        self.change_status("Iniciando Bot...")
        bot.bot = bot.bot_boot()
        msg = bot.start_msg()
        bot.lendo()
        self.change_status(msg)

    def make_buttons(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        btn_refresh = wx.Button(self.pnl, -1, 'Log')
        vbox.Add(btn_refresh, 0, wx.ALIGN_LEFT)
        self.Bind(wx.EVT_BUTTON, self.on_btn_refresh_click, btn_refresh)

    def on_btn_refresh_click(self, event):
        data = utils.load_file()[-10:]
        # Create a wxGrid object
        fm = wx.Frame(self, -1, title='Log Info', size=(500, 300))

        grid = wx.grid.Grid(fm, -1)

        grid.CreateGrid(len(data), 4)
        grid.SetColLabelValue(0, 'ID')
        grid.SetColLabelValue(1, 'Data')
        grid.SetColLabelValue(2, 'Nome')
        grid.SetColLabelValue(3, 'Mensagem')

        for row, x in enumerate(data):
            for col, value in enumerate(x):
                grid.SetCellValue(row, col, str(value))
        grid.AutoSize()
        grid.AutoSizeColumn(3)
        fm.Centre()
        fm.Show()


    def makeMenuBar(self):
        botMenu = wx.Menu()

        ligarItem = botMenu.Append(-1, "&Ligar")
        configItem = botMenu.Append(-1, "&Config")

        botMenu.AppendSeparator()
        exitItem = botMenu.Append(wx.ID_EXIT)

        menuBar = wx.MenuBar()
        menuBar.Append(botMenu, "&Bot")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnLigar, ligarItem)
        self.Bind(wx.EVT_MENU, self.OnConfig, configItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)

    def OnConfig(self, event):
        conf = utils.get_conf()

        dlg = wx.TextEntryDialog(self.pnl, 'Token de acesso do bot:', "acesso", "", style=wx.OK)
        dlg.SetValue(conf['token'])
        dlg.ShowModal()

        conf['token'] = dlg.GetValue()
        utils.save_conf(conf)
        dlg.Destroy()

    def OnExit(self, event):
        self.Close(True)


    def OnLigar(self, event):
        self.ini_bot()