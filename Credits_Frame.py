import wx
class Credit_Frame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1," Credits ",(300,300),(550,300))
		panel = wx.Panel(self,-1)
		font=wx.Font(20,wx.ROMAN,wx.ITALIC,wx.NORMAL)
		font2 = wx.Font(15,wx.ROMAN,wx.ITALIC,wx.NORMAL)
		wx.StaticText(panel,-1,"Tweet From Desktop",(100,20)).SetFont(font)
		wx.StaticText(panel,-1,"Developed By :",(160,60)).SetFont(font2)
		wx.StaticText(panel,-1,"Vijeenrosh P.W",(160,100)).SetFont(font2)
		wx.StaticText(panel,-1,"Email: hsorhteeniv@gmail.com",(100,140)).SetFont(font2)
		wx.StaticText(panel,-1,"http://www.BlackJackVijeen.blogspot.com",(70,180)).SetFont(font2)


class App(wx.App):
	def OnInit(self):
		frame=Credit_Frame()
		frame.Show()
		return True
if __name__=='__main__':		
	app = App()
	app.MainLoop()
