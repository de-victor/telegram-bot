from Frame import BotFrame
import wx

if __name__ == '__main__':
    app = wx.App()

    frm = BotFrame(None, title='Mayuri Bot 0.0.1a')
    frm.Show()
    app.MainLoop()