import wx


class Settings_Frame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1," Account Settings ",(300,300),(800,500))
		self.panel = wx.Panel(self,-1)
		self.is_error=False	
		wx.StaticText(self.panel,-1," Enter Your OAuth Details Here ",(300,100))
		wx.StaticText(self.panel,-1," Consumer Key     : ",(100,200))
		wx.StaticText(self.panel,-1," Consumer Secret :",(100,250))
		wx.StaticText(self.panel,-1,"Account Key/Token :",(100,300))
		wx.StaticText(self.panel,-1,"Account secret :",(100,350))
		self.ConsumerKey = wx.TextCtrl(self.panel,-1,"",(250,200),(300,30))
		self.ConsumerSecret = wx.TextCtrl(self.panel,-1,"",(250,250),(300,30))
		self.AccountKey = wx.TextCtrl(self.panel,-1,"",(250,300),(300,30))
		self.AccountSecret = wx.TextCtrl(self.panel,-1,"",(250,350),(300,30))
		self.Set = wx.Button(self.panel,-1,"Set Configuration",(330,400),(150,30))
		self.Bind(wx.EVT_BUTTON,self.OnSet,self.Set)

	def OnSet(self,event):
		fp = open("Account_Data.txt","w")
		Is_Ok=True
		y=200	
		for i in range(600,1000,50):
			wx.StaticText(self.panel,-1," ",(100,i)).SetForegroundColour("white")
		CKey,CSec,AKey,ASec = self.ConsumerKey.GetValue(),self.ConsumerSecret.GetValue(),self.AccountKey.GetValue(),self.AccountSecret.GetValue()
		if CKey=="":
			wx.StaticText(self.panel,-1,"*Consumer Key Ommitted ",(570,y)).SetForegroundColour("red")
			Is_Ok=False
			y=y+50
		if CSec=="":
			wx.StaticText(self.panel,-1,"*Consumer Secret Ommited",(570,y)).SetForegroundColour("red")
			Is_Ok=False
			y=y+50
		if AKey =="":
			wx.StaticText(self.panel,-1,"*Account Key Ommited",(570,y)).SetForegroundColour("red")
			Is_OK=False
			y=y+50	
		if ASec=="":
			wx.StaticText(self.panel,-1,"*Account Secret Ommited",(570,y)).SetForegroundColour("red")
			Is_Ok=False
			y=y+50
		if Is_Ok:	
			fp.write(CKey.strip()+"\n"+CSec.strip()+"\n"+AKey.strip()+"\n"+ASec.strip()+"\n")

			
		
class App(wx.App):
	def OnInit(self):
		frame= Settings_Frame()
		frame.Show()
		return True
if __name__ == '__main__':
	app = App()
	app.MainLoop()
		
