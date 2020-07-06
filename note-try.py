import Note_Try
import os
import wx
import codecs 

class show_Main_Frame ( Note_Try.Main_Frame ):

    def __init__(self, parent, current_File=None): #初始化
        super().__init__(parent) #先去跑Main_Frame的初始化
        self.current_File = current_File #新增一個物件－self.current_File，初始值為None

    def menu_Function_Build( self, event ): #按鈕名稱:建立檔案
        self.textCtrl.Clear() #清空
        event.Skip()    
    
    def menuItem_Function_OpenFile( self, event ):  #按鈕名稱:開啟檔案
        try:
            #PDF檔第26頁【呼叫檔案選擇器】(開啟文字檔)
            self.current_File=wx.FileSelector("請選擇要開啟的檔案　　ファイルを選びます",wildcard="文字檔案（もじ）|*.txt",flags=wx.FD_OPEN) 
            print("路徑位置（いち）：",self.current_File) #取得路徑"絕對"位置
            with codecs.open(self.current_File,mode="r",encoding="utf8") as file: #讀取檔案，因為文字檔，採用"utf-8"解碼
                # print(file.read()) #讀到的文字檔內容
                self.textCtrl.SetValue(file.read()) #PDF檔第19頁(輸入方塊的內容設定)
            Last_Name=(self.current_File.split("\\")[-1]) #取得檔名
            print("目前開啟的檔案　ファイルを開けています：",Last_Name) 
            windows.SetTitle("記事本（ノート）－"+Last_Name) #更改視窗標題
        
        except FileNotFoundError: #若跳出FileSelector檔案選擇器後，卻未選擇路徑，則會顯示「未輸入儲存指定位置」
            print("未輸入儲存指定位置\n何もないです")
            
        event.Skip()
        
    def menuItem_Function_SaveFile( self, event ): #按鈕名稱:儲存檔案
        if self.current_File==None: #當目前打開文件的路徑為None時，則可以跳出FileSelector檔案選擇器；換言之，若按「檔案開啟」取得檔案路徑後，則跳不出FileSelector檔案選擇器
            self.current_File=wx.FileSelector("請選擇要儲存的檔名　　ファイルの名前を入力してください",wildcard="文字檔案（もじ）|*.txt",flags=wx.FD_SAVE) #PDF檔第26頁【呼叫檔案選擇器】(儲存成文字檔)
        elif self.current_File=="": #當目前打開文件的路徑未輸入(空白)時，則可以跳出FileSelector檔案選擇器；換言之，若按「檔案開啟」取得檔案路徑後，則跳不出FileSelector檔案選擇器
            self.current_File=wx.FileSelector("請選擇要儲存的檔名　　ファイルの名前を入力してください",wildcard="文字檔案（もじ）|*.txt",flags=wx.FD_SAVE) #PDF檔第26頁【呼叫檔案選擇器】(儲存成文字檔)
        
        
        print("路徑位置（いち）:",self.current_File) #取得路徑"絕對"位置
        Last_Name=(self.current_File.split("\\")[-1]) #取得檔名
        # print(Last_Name) #儲存的檔名

        try:
            if os.path.exists(self.current_File)==False: #判斷如果檔案不存在(False)，則建立檔案     
                with codecs.open(self.current_File,mode="w",encoding="utf-8") as file: #寫入檔案，位置:s("絕對"位置)，因為文字檔，採用"utf-8"解碼
                    file.write(self.textCtrl.GetValue()) #寫入textCtrl內容
                windows.SetTitle("記事本（ノート）－"+Last_Name) #當寫入的時候，也改設定視窗標題

            elif os.path.exists(self.current_File)==True: #如果判斷如果檔案存在(True)，則覆寫資料夾     
                with codecs.open(self.current_File,mode="a",encoding="utf-8") as file: #複寫檔案，位置:s("絕對"位置)，因為文字檔，採用"utf-8"解碼
                    file.write(self.textCtrl.GetValue()) #覆寫textCtrl內容
                windows.SetTitle("記事本（ノート）－"+Last_Name) #當覆寫的時候，也改設定視窗標題

        except FileNotFoundError: #若跳出FileSelector檔案選擇器後，卻未選擇路徑，則會顯示「未輸入儲存指定位置」
            print("未輸入儲存指定位置\n何もないです")

        event.Skip()
        
    def menuItem_Function_Exit( self, event ): #按鈕名稱:關閉程式
        os.system("cls") #畫面清空
        wx.Exit() #關閉視窗程式
        event.Skip()

    def menuItem_Functione_Author( self, event ): #按鈕名稱:關於
        wind=Note_Try.Frame_Author(None) #秀出MyFrame5視窗
        wind.Show()
        wind.SetTitle("關於作者  作者に関する") #設定視窗標題
        event.Skip()

    def FrameSize( self, event ): #設定textCtrl文字編輯器的尺寸
        # print(windows.GetSize())
        size=windows.GetSize() #先取得視窗的大小
        width=size[0]-25 #些微調整，讓捲軸可以顯示
        tall=size[1]-60
        self.textCtrl.SetSize(width,tall) #設定textCtrl文字編輯器的尺寸
        event.Skip()


app=wx.App() #建立應用
windows=show_Main_Frame(None)  #設定視窗標數
windows.Show() #顯示視窗
windows.SetTitle("記事本　　ノート") #設定視窗標題－"記事本　　ノート"
app.MainLoop() #讓視窗持續顯示
