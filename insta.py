from instagram_gui import *
from InstagramAPI import InstagramAPI
from datetime import datetime
from instagram_gui import *
import imageio
import time
import urllib.request
import json

class MainWindou(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.btnDownload.clicked.connect(self.download)
    def download(self):
        user = self.txtUser.text()
        password = self.txtPass.text()
        self.btnDownload.setEnabled(False)
        insta = InstagramAPI(user, password)
        insta.login()
        QCoreApplication.processEvents() #This line returns the execution to the main window so it be Not Responding.

        insta.getProfileData()
        data = insta.LastJson
        self.lblProgress.setText('Connected successfully.')
        QCoreApplication.processEvents()
        urllib.request.urlretrieve(data['user']['profile_pic_url'], 'avatar.jpg') #Download avatar
        self.lblProgress.setText('Avatar downloaded.')
        QCoreApplication.processEvents()

        myposts=[]
        has_more_posts = True
        max_id=""

        while has_more_posts:
            QCoreApplication.processEvents()
            insta.getSelfUserFeed(maxid=max_id)
            if insta.LastJson['more_available'] is not True:
                has_more_posts = False
                self.lblProgress.setText("Parsing finished")
            
            max_id = insta.LastJson.get('next_max_id','')
            myposts.extend(insta.LastJson['items'])
            time.sleep(2)

        i = 0
        for p in myposts:
            QCoreApplication.processEvents()
            self.lblProgress.setText("Downloading photo {} of {}".format(i + 1, len(myposts)))
            imageURL = p['image_versions2']['candidates'][0]['url']
            imageDate = datetime.fromtimestamp(p['caption']['created_at']).strftime("%Y-%m-%d")+'.jpg'
            urllib.request.urlretrieve( imageURL, imageDate )
            i += 1
            

        self.lblProgress.setText("Finished.")
        self.btnDownload.setEnabled(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindou()
    window.show()
    app.exec_()

