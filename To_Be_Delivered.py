from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

#get color definitions
from color_definitions import *

class forgotPWWindow(QDialog):
    def __init__(self):
        windowName = "Forgot Password"

        super().__init__()

        self.setStyleSheet("background-color: " + RED + ";")
        self.setWindowTitle(windowName)
        layoutForgot = QGridLayout()

        #labels
        self.emailLabel = QLabel("<h1>Please enter in your email linked to your account:</h1>")

        #line edits
        self.recovEmail = QLineEdit()
        self.recovEmail.setPlaceholderText("Email")
        self.recovEmail.setStyleSheet("background-color: white;")

        #buttons
        self.nextButton = QPushButton(">")
        self.nextButton.setStyleSheet("background-color: white;")

        #button connections
        self.nextButton.clicked.connect(self.nextButton_Clicked)

        layoutForgot.addWidget(self.emailLabel, 0, 0)
        layoutForgot.addWidget(self.recovEmail, 1, 0)
        layoutForgot.addWidget(self.nextButton, 1, 1)

        self.setLayout(layoutForgot)

    def nextButton_Clicked(self):
        #TODO: implement password reset functionality
        email = self.recovEmail.text()
        if email == '':
            print("an email is needed")
        else:   
            print("reset password button clicked")
            self.close()

class resetPWWindow(QDialog):
    def __init__(self):
        windowName = "Reset Password"

        super().__init__()

        self.setWindowTitle(windowName)
        layoutResetPW = QGridLayout()

        # labels
        self.usernameLabel = QLabel("Enter in your email:")
        self.newPWLabel = QLabel("Enter new password:")
        self.newPWReenterLabel = QLabel("Reenter new password:")

        # line edits
        self.recovEmail = QLineEdit()
        self.newPWInput = QLineEdit()
        self.newPWReInput = QLineEdit()

        # buttons
        self.nextButton = QPushButton(">")

        # button connections
        
        self.recovEmail.setPlaceholderText("Email")
        self.newPWInput.setPlaceholderText("New password")
        self.newPWReInput.setPlaceholderText("Reenter new password")

        layoutResetPW.addWidget(self.usernameLabel, 0, 0)
        layoutResetPW.addWidget(self.recovEmail, 0, 1)
        layoutResetPW.addWidget(self.newPWLabel, 2, 0)
        layoutResetPW.addWidget(self.newPWInput, 2, 1)
        layoutResetPW.addWidget(self.newPWReenterLabel, 3, 0)
        layoutResetPW.addWidget(self.newPWReInput, 3, 1)
        layoutResetPW.addWidget(self.nextButton, 3, 2)

        self.setLayout(layoutResetPW)


class createAccountWindow(QDialog):
    def __init__(self):
        windowName = "Create New Account"

        super().__init__()

        self.setWindowTitle(windowName)
        self.setStyleSheet("background-color: " + LIGHT_GREEN + ";")
        layoutCreateAccount = QGridLayout()

        # labels
        createAccountWelcomeLabel = QLabel("<h1>Create an account:</h1>")
        createUsernameLabel = QLabel("Enter new username: ")
        createPWLabel = QLabel("Enter password: ")
        reenterPWLabel = QLabel("Reenter password: ")

        # line edits
        newUserName = QLineEdit()
        password = QLineEdit()
        reenterPW = QLineEdit()
        newUserName.setPlaceholderText("Username")
        password.setPlaceholderText("Password")
        reenterPW.setPlaceholderText("Reenter password")
        newUserName.setStyleSheet("background-color: white;")
        password.setStyleSheet("background-color: white;")
        reenterPW.setStyleSheet("background-color: white;")

        # buttons
        pwRequirements = QPushButton("i")
        nextButton = QPushButton(">")
        pwRequirements.setGeometry(100, 150, 100, 100)
        nextButton.setStyleSheet("background-color: white;")
        pwRequirements.setStyleSheet("background-color: white;")

        # button connections
        pwRequirements.clicked.connect(self.launchPWInfo)
        nextButton.clicked.connect(self.nextButton_Clicked)
        
        layoutCreateAccount.addWidget(createAccountWelcomeLabel, 0, 0)
        layoutCreateAccount.addWidget(createUsernameLabel, 1, 0)
        layoutCreateAccount.addWidget(newUserName, 1, 1)
        layoutCreateAccount.addWidget(createPWLabel, 2, 0)
        layoutCreateAccount.addWidget(password, 2, 1)
        layoutCreateAccount.addWidget(pwRequirements, 2, 2)
        layoutCreateAccount.addWidget(reenterPWLabel, 3, 0)
        layoutCreateAccount.addWidget(reenterPW, 3, 1)
        layoutCreateAccount.addWidget(nextButton, 3, 2)

        self.setLayout(layoutCreateAccount)

    def launchPWInfo(self):
        self.window = pwInfoWindow()
        self.window.show()

    def nextButton_Clicked(self):
        #TODO: Create account for user using input credentials
        self.close()

class pwInfoWindow(QDialog):
    def __init__(self):
        windowName = "Password Requirements"

        super().__init__()

        self.setWindowTitle(windowName)
        layoutPWInfo = QGridLayout()

        # lables
        PWReq1Label = QLabel("1. At least 12 characters in total")
        PWReq2Label = QLabel("2. At least one uppercase letter")
        PWReq3Label = QLabel("3. At least one lowercase letter")
        PWReq4Label = QLabel("4. At least one special character")
        PWReq5Label = QLabel("5. At least one number")
        passwordRequirementLabel = QLabel("<h2>Your password must consist of the following:</h2>")

        layoutPWInfo.addWidget(passwordRequirementLabel, 0, 0)
        layoutPWInfo.addWidget(PWReq1Label, 1, 0)
        layoutPWInfo.addWidget(PWReq2Label, 2, 0)
        layoutPWInfo.addWidget(PWReq3Label, 3, 0)
        layoutPWInfo.addWidget(PWReq4Label, 4, 0)
        layoutPWInfo.addWidget(PWReq5Label, 5, 0)
        
        self.setLayout(layoutPWInfo)


class loggedInWindow(QDialog):
    def __init__(self):
        windowName = "Welcome user_name"

        super().__init__()

        self.setStyleSheet("background-color: " + LIGHT_PURPLE + ";")
        self.setWindowTitle(windowName)
        layoutLoggedIn = QGridLayout()

        # labels
        self.folderSection = QListWidget()
        self.folderSection.setMaximumSize(150, 500)
        QListWidgetItem("HW files", self.folderSection)
        QListWidgetItem("Pictures", self.folderSection)
        QListWidgetItem("Important Documents", self.folderSection)
        self.mainSection = QListWidget()
        self.mainSection.setMaximumSize(1000, 1000)
        self.folderSection.setStyleSheet("background-color: white;")
        self.mainSection.setStyleSheet("background-color: white;")
        
        # buttons
        self.newFolderSection = QPushButton("Create New Folder")
        self.uploadFileSection = QPushButton("Upload a File")
        self.uploadFileSection.setStyleSheet("background-color: white;")

        # button connections
        self.uploadFileSection.clicked.connect(self.launchUploadFile)
        self.newFolderSection.clicked.connect(self.launchCreateFolder)

        layoutLoggedIn.addWidget(self.folderSection, 0, 0)
        layoutLoggedIn.addWidget(self.newFolderSection, 1, 0)
        layoutLoggedIn.addWidget(self.mainSection, 0, 1)
        layoutLoggedIn.addWidget(self.uploadFileSection, 1, 1)

        self.setLayout(layoutLoggedIn)

    def launchUploadFile(self):
        self.window = uploadFileWindow()
        self.window.show()
    
    def launchCreateFolder(self):
        self.window = createFolderWindow()
        self.window.show()

class uploadFileWindow(QDialog):
    def __init__(self):
        windowName = "Upload File"

        super().__init__()

        self.layoutUploadFile = QGridLayout()
        self.setFixedWidth(500)

        # labels
        self.uploadFileLabel = QLabel("<h2>Upload a File<\h2>")
        self.deviceOption = QLabel("Target storage device:")
        self.filePath = QLabel("File path:")

        # line edits
        self.deviceOptionInput = QLineEdit()
        self.filePathInput = QLineEdit()
        self.deviceOptionInput.setPlaceholderText("Storage Device")
        self.filePathInput.setPlaceholderText("File path")
        self.deviceOptionInput.setStyleSheet("background-color: white;")
        self.filePathInput.setStyleSheet("background-color: white;")

        # buttons
        self.scheduleTransfer = QPushButton("Schedule")
        self.sendNow = QPushButton("Send Now")
        self.sendNow.setStyleSheet("background-color: " + PURPLE + "; color: white;")

        # button connections
        self.scheduleTransfer.clicked.connect(self.launchSchedule)        
        self.sendNow.clicked.connect(self.sendNow_Clicked)

        self.layoutUploadFile.addWidget(self.uploadFileLabel, 0, 0)
        self.layoutUploadFile.addWidget(self.deviceOption, 1, 0)
        self.layoutUploadFile.addWidget(self.deviceOptionInput, 1, 1)
        self.layoutUploadFile.addWidget(self.filePath, 2, 0)
        self.layoutUploadFile.addWidget(self.filePathInput, 2, 1)
        self.layoutUploadFile.addWidget(self.scheduleTransfer, 3, 0)
        self.layoutUploadFile.addWidget(self.sendNow, 3, 1)

        self.setLayout(self.layoutUploadFile)
        self.setWindowTitle(windowName)

        #open file explorer
        filePath = QFileDialog.getOpenFileName(self, "")
        self.filePathInput.setText(filePath[0])
        self.setStyleSheet("background-color: " + LIGHT_PURPLE + ";")

    def launchSchedule(self):
        self.window = uploadFileScheduleWindow()
        self.window.show()

    def sendNow_Clicked(self):
        #TODO: Implement code here to send file indicated by file path
        filePath = self.filePathInput.text()
        if filePath != '':
            self.close()

class uploadFileScheduleWindow(QDialog):
    def __init__(self):
        windowName = "Schedule File Transfer"

        super().__init__()

        self.setWindowTitle(windowName)
        layoutUploadFileSch = QGridLayout()
        choicesBox = QVBoxLayout()

        # labels
        scheduleLabel = QLabel("<h1>Schedule file transfer:<\h1>")
        schedulingChoicesBox = QGroupBox("Scheduling Options:")
        schedulingChoicesBox.setCheckable(True)
        schedulingChoicesBox.setLayout(choicesBox)

        # buttons
        schOption1 = QRadioButton("Immediately")
        schOption2 = QRadioButton("30 minutes")
        schOption3 = QRadioButton("1 hour")
        schOption4 = QRadioButton("5 hours")
        schOption5 = QRadioButton("Custom")
        applyButton = QPushButton("Apply")

        # Button connections
        applyButton.clicked.connect(self.applyButton_Clicked)

        choicesBox.addWidget(schOption1)
        choicesBox.addWidget(schOption2)
        choicesBox.addWidget(schOption3)
        choicesBox.addWidget(schOption4)
        choicesBox.addWidget(schOption5)

        layoutUploadFileSch.addWidget(scheduleLabel, 0, 0)
        layoutUploadFileSch.addWidget(schedulingChoicesBox, 1, 0)
        layoutUploadFileSch.addWidget(applyButton, 2, 0)

        self.setLayout(layoutUploadFileSch)
    
    def applyButton_Clicked(self):
        #TODO: Actually implment logic to send file at appropriate time, close uploadFileWindow as well
        print("Sent file")
        self.close()

class createFolderWindow(QDialog):
    def __init__(self):
        windowName = "Create Folder"

        super().__init__()

        self.setStyleSheet("background-color: " + LIGHT_PURPLE + ";")
        self.setWindowTitle(windowName)
        layoutCreateFolder = QGridLayout()

        # labels
        createFoldLabel = QLabel("<h2>Create a folder:</h2>")
        filePath = QLabel("Folder location:")
        folderName = QLabel("Folder name:")

        # line edits
        filePathInput = QLineEdit()
        folderNameInput = QLineEdit()
        filePathInput.setPlaceholderText("Folder Path")
        folderNameInput.setPlaceholderText("Folder name")
        filePathInput.setStyleSheet("background-color: white;")
        folderNameInput.setStyleSheet("background-color: white;")

        # buttons
        addFolderButton = QPushButton("Add New Folder")
        addFolderButton.setStyleSheet("background-color: " + PURPLE + "; color: white")

        # button connections
        addFolderButton.clicked.connect(self.addFolderButton_Clicked)

        layoutCreateFolder.addWidget(createFoldLabel, 0, 0)
        layoutCreateFolder.addWidget(filePath, 1, 0)
        layoutCreateFolder.addWidget(filePathInput, 1, 1)
        layoutCreateFolder.addWidget(folderName, 2, 0)
        layoutCreateFolder.addWidget(folderNameInput, 2, 1)
        layoutCreateFolder.addWidget(addFolderButton, 2, 2)

        self.setLayout(layoutCreateFolder)
    
    def addFolderButton_Clicked(self):
        #TODO: Add folder to folders list
        print("Folder created")
        self.close()

class fileDeleteWarningWindow(QDialog):
    def __init__(self):
        windowName = "Delete Warning"

        super().__init__()

        self.setWindowTitle(windowName)
        layoutFileDeleteWarning = QGridLayout()

        # labels
        warningLabel = QLabel("<h2>WARNING:</h2>")
        warningMessage = QLabel("Be aware that the file you are deleting will not be recoverable unless recovery date is set.")

        # line edits
        recoveryTime = QLineEdit()
        recoveryTime.setPlaceholderText("Number of days to recover file")

        # buttons
        nextButton = QPushButton(">")

        layoutFileDeleteWarning.addWidget(warningLabel, 0, 0)
        layoutFileDeleteWarning.addWidget(warningMessage, 1, 0)
        layoutFileDeleteWarning.addWidget(recoveryTime, 2, 0)
        layoutFileDeleteWarning.addWidget(nextButton, 2, 1)
        
        self.setLayout(layoutFileDeleteWarning)

class storageOrUserDeviceWiindow(QDialog):
    def __init__(self):   # override constructor method
        windowName = "To Be Delivered"   # sets the window name

        super().__init__()   # call QDialog's constructor method (parent)

        self.setStyleSheet("background-color: " + LIGHT_PURPLE + ";") #sets background color, very similar to CSS
        self.layoutStorageOrUserComputer = QGridLayout()   # add layout for how QWidget should be displayed on screen

        # labels
        self.storageOrUserLabel = QLabel("<h1>Are you on the storage or user computer?</h1>")

        # buttons
        self.storageButton = QPushButton("Storage")   # create a push button widget
        self.userButton = QPushButton("User")

        # button connections
        self.storageButton.clicked.connect(self.launchStorageComputerSigninWindow)
        self.userButton.clicked.connect(self.launchUserComputerSigninWindow)

        # add widgets to layout
        self.layoutStorageOrUserComputer.addWidget(self.storageOrUserLabel, 0, 0)  # row, column
        self.layoutStorageOrUserComputer.addWidget(self.storageButton, 1, 0)
        self.layoutStorageOrUserComputer.addWidget(self.userButton, 2, 0)

        # tell QDialog constructor method to use layout to display the elements on the screen
        self.setLayout(self.layoutStorageOrUserComputer)

        # sets name of the window
        self.setWindowTitle(windowName)

    # launches the user sign in window if user is on user computer 
    def launchUserComputerSigninWindow(self):
        self.window = mainWindow()
        self.window.show()
    
    def launchStorageComputerSigninWindow(self):
        self.window = storageComputerSigninWindow()
        self.window.show()

class storageComputerSigninWindow(QDialog):
    def __init__(self):   # override constructor method
        windowName = "To Be Delivered"   # sets the window name

        super().__init__()   # call QDialog's constructor method (parent)

        self.setStyleSheet("background-color: " + LIGHT_PURPLE + ";") #sets background color, very similar to CSS
        self.layoutStorageComputerSignin = QGridLayout()   # add layout for how QWidget should be displayed on screen

        # labels
        self.signInLabel = QLabel("<h1>Sign In</h1>")   # create a label widget
        self.forgotPWLabel = QLabel("Forward Password?")   
        self.createNewAccountLabel = QLabel("Don't have an account?")

        # line edits
        self.userName = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        # set placeholder text
        self.userName.setPlaceholderText("Username")
        self.password.setPlaceholderText("Password")
        #set background color
        self.userName.setStyleSheet("background-color: white;")
        self.password.setStyleSheet("background-color: white;")

        # buttons
        self.nextButtonSignIn = QPushButton(">")   # create a push button widget
        self.warningSymbolButton = QPushButton("⚠")
        self.createNewAccountButton = QPushButton("Create an account")
        self.showPWButton = QPushButton("<0>")
        self.password_revealed = False

        # button connections
        self.nextButtonSignIn.clicked.connect(self.nextButtonSignIn_Clicked)
        self.warningSymbolButton.clicked.connect(self.launchForgotPW)
        self.createNewAccountButton.clicked.connect(self.launchCreateAccount)
        self.showPWButton.clicked.connect(self.revealPW)

        # add widgets to layout
        self.layoutStorageComputerSignin.addWidget(self.signInLabel, 0, 0)  # row, column
        self.layoutStorageComputerSignin.addWidget(self.userName, 1, 0)
        self.layoutStorageComputerSignin.addWidget(self.password, 2, 0)
        self.layoutStorageComputerSignin.addWidget(self.nextButtonSignIn, 2, 2)
        self.layoutStorageComputerSignin.addWidget(self.forgotPWLabel, 3, 0)
        self.layoutStorageComputerSignin.addWidget(self.warningSymbolButton, 3, 1)
        self.layoutStorageComputerSignin.addWidget(self.createNewAccountLabel, 4, 0)
        self.layoutStorageComputerSignin.addWidget(self.createNewAccountButton, 4, 1)
        self.layoutStorageComputerSignin.addWidget(self.showPWButton, 2, 1)

        # tell QDialog constructor method to use layout to display the elements on the screen
        self.setLayout(self.layoutStorageComputerSignin)

        # sets name of the window
        self.setWindowTitle(windowName)

    # need to check for correct password and username to be able to launch logged in window. 
    def launchLoggedIn(self):
        self.window = loggedInWindow()
        self.window.show()

    def launchForgotPW(self):
        self.window = forgotPWWindow()
        self.window.show()

    def launchCreateAccount(self):
        self.window = createAccountWindow()
        self.window.show()

    def nextButtonSignIn_Clicked(self):
        email = self.userName.text()
        password = self.password.text()
        # if email == "admin" and password == "pass":
        #     self.close()
        #     self.launchLoggedIn()
        self.close()
        self.launchLoggedIn()

    def revealPW(self):
        if self.password_revealed == False:
            self.password.setEchoMode(QLineEdit.Normal)
        else:
            self.password.setEchoMode(QLineEdit.Password)
        #toggle password_revealed
        self.password_revealed = (self.password_revealed == False)

class mainWindow(QDialog):  # class inherits from QDialog

    def __init__(self):   # override constructor method
        windowName = "To Be Delivered"   # sets the window name

        super().__init__()   # call QDialog's constructor method (parent)

        self.setStyleSheet("background-color: " + LIGHT_PURPLE + ";") #sets background color, very similar to CSS
        self.layoutHome = QGridLayout()   # add layout for how QWidget should be displayed on screen

        # labels
        self.signInLabel = QLabel("<h1>Sign In</h1>")   # create a label widget
        self.forgotPWLabel = QLabel("Forward Password?")   
        self.createNewAccountLabel = QLabel("Don't have an account?")

        # line edits
        self.userName = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        # set placeholder text
        self.userName.setPlaceholderText("Username")
        self.password.setPlaceholderText("Password")
        #set background color
        self.userName.setStyleSheet("background-color: white;")
        self.password.setStyleSheet("background-color: white;")

        # buttons
        self.nextButtonSignIn = QPushButton(">")   # create a push button widget
        self.warningSymbolButton = QPushButton("⚠")
        self.createNewAccountButton = QPushButton("Create an account")
        self.showPWButton = QPushButton("<0>")
        self.password_revealed = False

        # button connections
        self.nextButtonSignIn.clicked.connect(self.nextButtonSignIn_Clicked)
        self.warningSymbolButton.clicked.connect(self.launchForgotPW)
        self.createNewAccountButton.clicked.connect(self.launchCreateAccount)
        self.showPWButton.clicked.connect(self.revealPW)

        # add widgets to layout
        self.layoutHome.addWidget(self.signInLabel, 0, 0)  # row, column
        self.layoutHome.addWidget(self.userName, 1, 0)
        self.layoutHome.addWidget(self.password, 2, 0)
        self.layoutHome.addWidget(self.nextButtonSignIn, 2, 2)
        self.layoutHome.addWidget(self.forgotPWLabel, 3, 0)
        self.layoutHome.addWidget(self.warningSymbolButton, 3, 1)
        self.layoutHome.addWidget(self.createNewAccountLabel, 4, 0)
        self.layoutHome.addWidget(self.createNewAccountButton, 4, 1)
        self.layoutHome.addWidget(self.showPWButton, 2, 1)

        # tell QDialog constructor method to use layout to display the elements on the screen
        self.setLayout(self.layoutHome)

        # sets name of the window
        self.setWindowTitle(windowName)

    # need to check for correct password and username to be able to launch logged in window. 
    def launchLoggedIn(self):
        self.window = loggedInWindow()
        self.window.show()

    def launchForgotPW(self):
        self.window = forgotPWWindow()
        self.window.show()

    def launchCreateAccount(self):
        self.window = createAccountWindow()
        self.window.show()

    def nextButtonSignIn_Clicked(self):
        email = self.userName.text()
        password = self.password.text()
        # if email == "admin" and password == "pass":
        #     self.close()
        #     self.launchLoggedIn()
        self.close()
        self.launchLoggedIn()

    def revealPW(self):
        if self.password_revealed == False:
            self.password.setEchoMode(QLineEdit.Normal)
        else:
            self.password.setEchoMode(QLineEdit.Password)
        #toggle password_revealed
        self.password_revealed = (self.password_revealed == False)

app = QApplication(sys.argv)
fileApp = storageOrUserDeviceWiindow()
fileApp.show()
sys.exit(app.exec_())