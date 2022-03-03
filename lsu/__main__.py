# Import modules
import os, sys, stat, subprocess
from PyQt4 import QtGui

# print(subprocess.call("pwd"))

# Set the files right
os.chmod("bash/source_update.sh", stat.S_IRWXU)
os.chmod("bash/system_update.sh", stat.S_IRWXU)

# Import os-update script
def running_os_update_script():
    subprocess.call("bash/system_update.sh")

# Import source update
def running_source_update_script():
    subprocess.call("bash/source_update.sh")

# Application

def window():
   app = QtGui.QApplication(sys.argv)
   w = QtGui.QWidget()
   b = QtGui.QLabel(w)
   b.setText("Hello World!")
   w.setGeometry(100,100,200,50)
   b.move(50,20)
   w.setWindowTitle("Pyqt")
   w.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   window()