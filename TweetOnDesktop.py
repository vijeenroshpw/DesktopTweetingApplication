import wx
import Settings_Frame
import tweepy
import Credits_Frame
class TweetFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,"TweetOnDesktop",(200,200),(900,900))
		self.panel=wx.Panel(self,-1)
		menusetting = wx.Menu()
		menusetting.Append(1,"Configure Account ")
		menucredit = wx.Menu()
		menucredit.Append(2,"Credits")
		menubar = wx.MenuBar()
		menubar.Append(menusetting,"&Setting")
		menubar.Append(menucredit,"&Credits")
		self.SetMenuBar(menubar)
		self.Bind(wx.EVT_MENU,self.OnConfigure,id=1)
		wx.StaticText(self.panel,-1,"Enter Your Tweet Here :",(50,150))
		self.tweet_update = wx.TextCtrl(self.panel,-1,"",(50,170),(300,100),wx.TE_MULTILINE)
		self.tweet_button = wx.Button(self.panel,-1," Tweet",(50,300),(80,30))
		self.Bind(wx.EVT_BUTTON,self.OnTweet,self.tweet_button)
		wx.StaticText(self.panel,-1," Recent Tweets: ",(50,350))	
		self.statuses=wx.TextCtrl(self.panel,-1,"",(50,370),(600,200),wx.TE_MULTILINE)
		self.fetch = wx.Button(self.panel,-1,"Fetch Tweets",(50,580),(100,30))	
		self.Bind(wx.EVT_BUTTON,self.OnFetch,self.fetch)
		font = wx.Font(30,wx.ROMAN,wx.ITALIC,wx.NORMAL)
		wx.StaticText(self.panel,-1," Tweet On Desktop ",(220,50)).SetFont(font)
		self.Bind(wx.EVT_MENU,self.OnCredit,id=2)
	def OnCredit(self,event):
		frame = Credits_Frame.Credit_Frame()
		frame.Show()

	


	def OnTweet(self,event):
		fp = open("Account_Data.txt","r")
		CKey=fp.readline().strip()
		CSec=fp.readline().strip()
		AKey = fp.readline().strip()
		ASec = fp.readline().strip()
		dialog = wx.MessageDialog(None," Account Not Configured Or Bad Account Details . Please Refurnish Account Details.","Alert",wx.OK)
		#print CKey
		#print CSec
		#print AKey
		#print ASec
		#if CKey=="" or CSec=="" or AKey=="" or ASec=="":
		#	dialog.ShowModal()
		#else:
		try:	
			auth = tweepy.OAuthHandler(CKey, CSec)
			auth.set_access_token(AKey, ASec)
			api = tweepy.API(auth)
			api.update_status(self.tweet_update.GetValue())		
			wx.StaticText(self.panel,-1,"Tweeted Succesfully",(50,350))
		except tweepy.error.TweepError:
			dialog.ShowModal()
	def OnConfigure(self,event):
		frame=Settings_Frame.Settings_Frame()
		frame.Show()
	def OnFetch(self,event):
		fp = open("Account_Data.txt","r")
                CKey=fp.readline().strip()
                CSec=fp.readline().strip()
                AKey = fp.readline().strip()
                ASec = fp.readline().strip()
                dialog = wx.MessageDialog(None," Account Not Configured Or Bad Account Details . Please Refurnish Account Details.","Alert",wx.OK)
                #print CKey
                #print CSec
                #print AKey
                #print ASec
                #if CKey=="" or CSec=="" or AKey=="" or ASec=="":
                #       dialog.ShowModal()
                #else:
                try:    
                        auth = tweepy.OAuthHandler(CKey, CSec)
                        auth.set_access_token(AKey, ASec)
                        api = tweepy.API(auth)
                      	self.statuses.SetValue("") 
                        posts = api.home_timeline()
			
			for post in posts:
				author = post.author.name
				message=post.text
				self.statuses.AppendText("\n" + author + ":\n" + message + "\n\n\n")
                except tweepy.error.TweepError:
                        dialog.ShowModal()
				

class Twitter_App(wx.App):
	def OnInit(self):
		frame = TweetFrame()
		frame.Show()
		return True

app = Twitter_App()
app.MainLoop()

		
		
