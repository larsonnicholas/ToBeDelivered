# CS 425 PA 3 GUI 
    # Using PyQt5 

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class forgotPWWindow(QDialog):
    def __init__(self):
        windowName = "Forgot Password"

        QDialog.__init__(self)

        layoutForgot = QGridLayout()

        emailLabel = QLabel("<h1>Please enter in your email linked to your account:</h1>")
        recovEmail = QLineEdit()
        nextButton = QPushButton(">")

        recovEmail.setPlaceholderText("Email")

        layoutForgot.addWidget(emailLabel, 0, 0)
        layoutForgot.addWidget(recovEmail, 1, 0)
        layoutForgot.addWidget(nextButton, 1, 1)

        self.setLayout(layoutForgot)

        self.setWindowTitle(windowName)

class resetPWWindow(QDialog):
    def __init__(self):
        windowName = "Reset Password"

        QDialog.__init__(self)

        layoutResetPW = QGridLayout()

        usernameLabel = QLabel("Enter in your email:")
        recovEmail = QLineEdit()
        newPWLabel = QLabel("Enter new password:")
        newPWInput = QLineEdit()
        newPWReenterLabel = QLabel("Reenter new password:")
        newPWReInput = QLineEdit()
        nextButton = QPushButton(">")

        recovEmail.setPlaceholderText("Email")
        newPWInput.setPlaceholderText("New password")
        newPWReInput.setPlaceholderText("Reenter new password")

        layoutResetPW.addWidget(usernameLabel, 0, 0)
        layoutResetPW.addWidget(recovEmail, 0, 1)
        layoutResetPW.addWidget(newPWLabel, 2, 0)
        layoutResetPW.addWidget(newPWInput, 2, 1)
        layoutResetPW.addWidget(newPWReenterLabel, 3, 0)
        layoutResetPW.addWidget(newPWReInput, 3, 1)
        layoutResetPW.addWidget(nextButton, 3, 2)

        self.setLayout(layoutResetPW)

        self.setWindowTitle(windowName)

class createAccountWindow(QDialog):
    def __init__(self):
        windowName = "Create New Account"

        QDialog.__init__(self)

        layoutCreateAccount = QGridLayout()

        createAccountWelcomeLabel = QLabel("<h1>Create an account:</h1>")
        createUsernameLabel = QLabel("Enter new username: ")
        newUserName = QLineEdit()
        createPWLabel = QLabel("Enter password: ")
        password = QLineEdit()
        pwRequirements = QPushButton("i")
        reenterPWLabel = QLabel("Reenter password: ")
        reenterPW = QLineEdit()
        nextButton = QPushButton(">")

        pwRequirements.setGeometry(100, 150, 100, 100)

        newUserName.setPlaceholderText("Username")
        password.setPlaceholderText("Password")
        reenterPW.setPlaceholderText("Reenter password")

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

        pwRequirements.clicked.connect(self.launchPWInfo)

        self.setWindowTitle(windowName)

    def launchPWInfo(self):
        self.window = pwInfoWindow()
        self.window.show()

class pwInfoWindow(QDialog):
    def __init__(self):
        windowName = "Password Requirements"

        QDialog.__init__(self)

        layoutPWInfo = QGridLayout()

        passwordRequirementLabel = QLabel("<h2>Your password must consist of the following:</h2>")
        PWReq1Label = QLabel("1. At least 12 characters in total")
        PWReq2Label = QLabel("2. At least one uppercase letter")
        PWReq3Label = QLabel("3. At least one lowercase letter")
        PWReq4Label = QLabel("4. At least one special character")
        PWReq5Label = QLabel("5. At least one number")

        layoutPWInfo.addWidget(passwordRequirementLabel, 0, 0)
        layoutPWInfo.addWidget(PWReq1Label, 1, 0)
        layoutPWInfo.addWidget(PWReq2Label, 2, 0)
        layoutPWInfo.addWidget(PWReq3Label, 3, 0)
        layoutPWInfo.addWidget(PWReq4Label, 4, 0)
        layoutPWInfo.addWidget(PWReq5Label, 5, 0)
        
        self.setLayout(layoutPWInfo)

        self.setWindowTitle(windowName)

class loggedInWindow(QDialog):
    def __init__(self):
        windowName = "Welcome user_name"

        QDialog.__init__(self)

        layoutLoggedIn = QGridLayout()

        folderSection = QListWidget()
        folderSection.setMaximumSize(150, 500)
        QListWidgetItem("HW files", folderSection)
        QListWidgetItem("Pictures", folderSection)
        QListWidgetItem("Important Documents", folderSection)
        
        newFolderSection = QPushButton("Create New Folder")
        uploadFileSection = QPushButton("Upload a File")

        mainSection = QListWidget()
        mainSection.setMaximumSize(1000, 1000)

        layoutLoggedIn.addWidget(folderSection, 0, 0)
        layoutLoggedIn.addWidget(newFolderSection, 1, 0)
        layoutLoggedIn.addWidget(mainSection, 0, 1)
        layoutLoggedIn.addWidget(uploadFileSection, 1, 1)

        self.setLayout(layoutLoggedIn)

        self.setWindowTitle(windowName)

class uploadFileWindow(QDialog):
    def __init__(self):
        windowName = "Upload File"

        QDialog.__init__(self)

        layoutUploadFile = QGridLayout()

        uploadFileLabel = QLabel("<h2>Upload a File<\h2>")
        deviceOption = QLabel("Target storage device:")
        deviceOptionInput = QLineEdit()
        filePath = QLabel("File path:")
        filePathInput = QLineEdit()
        scheduleTransfer = QPushButton("Schedule")

        deviceOptionInput.setPlaceholderText("Storage Device")
        filePathInput.setPlaceholderText("File path")

        layoutUploadFile.addWidget(uploadFileLabel, 0, 0)
        layoutUploadFile.addWidget(deviceOption, 1, 0)
        layoutUploadFile.addWidget(deviceOptionInput, 1, 1)
        layoutUploadFile.addWidget(filePath, 2, 0)
        layoutUploadFile.addWidget(filePathInput, 2, 1)
        layoutUploadFile.addWidget(scheduleTransfer, 3, 0)

        self.setLayout(layoutUploadFile)

        self.setWindowTitle(windowName)

class uploadFileScheduleWindow(QDialog):
    def __init__(self):
        windowName = "Schedule File Transfer"

        QDialog.__init__(self)

        layoutUploadFileSch = QGridLayout()
        choicesBox = QVBoxLayout()

        scheduleLabel = QLabel("<h1>Schedule file transfer:<\h1>")
        applyButton = QPushButton("Apply")

        schedulingChoicesBox = QGroupBox("Scheduling Options:")
        schedulingChoicesBox.setCheckable(True)
        schOption1 = QRadioButton("Immediately")
        schOption2 = QRadioButton("30 minutes")
        schOption3 = QRadioButton("1 hour")
        schOption4 = QRadioButton("5 hours")
        schOption5 = QRadioButton("Custom")
        schedulingChoicesBox.setLayout(choicesBox)
        choicesBox.addWidget(schOption1)
        choicesBox.addWidget(schOption2)
        choicesBox.addWidget(schOption3)
        choicesBox.addWidget(schOption4)
        choicesBox.addWidget(schOption5)

        layoutUploadFileSch.addWidget(scheduleLabel, 0, 0)
        layoutUploadFileSch.addWidget(schedulingChoicesBox, 1, 0)
        layoutUploadFileSch.addWidget(applyButton, 2, 0)

        self.setLayout(layoutUploadFileSch)

        self.setWindowTitle(windowName)

class createFolderWindow(QDialog):
    def __init__(self):
        windowName = "Create Folder"

        QDialog.__init__(self)

        layoutCreateFolder = QGridLayout()

        createFoldLabel = QLabel("<h2>Create a folder:</h2>")
        filePath = QLabel("Folder location:")
        filePathInput = QLineEdit()
        folderName = QLabel("Folder name:")
        folderNameInput = QLineEdit()
        addFolderButton = QPushButton("Add New Folder")

        filePathInput.setPlaceholderText("Folder Path")
        folderNameInput.setPlaceholderText("Folder name")

        layoutCreateFolder.addWidget(createFoldLabel, 0, 0)
        layoutCreateFolder.addWidget(filePath, 1, 0)
        layoutCreateFolder.addWidget(filePathInput, 1, 1)
        layoutCreateFolder.addWidget(folderName, 2, 0)
        layoutCreateFolder.addWidget(folderNameInput, 2, 1)
        layoutCreateFolder.addWidget(addFolderButton, 2, 2)

        self.setLayout(layoutCreateFolder)

        self.setWindowTitle(windowName)

class fileDeleteWarningWindow(QDialog):
    def __init__(self):
        windowName = "Delete Warning"

        QDialog.__init__(self)

        layoutFileDeleteWarning = QGridLayout()

        warningLabel = QLabel("<h2>WARNING:</h2>")
        warningMessage = QLabel("Be aware that the file you are deleting will not be recoverable unless recovery date is set.")
        recoveryTime = QLineEdit()
        recoveryTime.setPlaceholderText("Number of days to recover file")
        nextButton = QPushButton(">")

        layoutFileDeleteWarning.addWidget(warningLabel, 0, 0)
        layoutFileDeleteWarning.addWidget(warningMessage, 1, 0)
        layoutFileDeleteWarning.addWidget(recoveryTime, 2, 0)
        layoutFileDeleteWarning.addWidget(nextButton, 2, 1)
        
        self.setLayout(layoutFileDeleteWarning)

        self.setWindowTitle(windowName)

class mainWindow(QDialog):  # class inherits from QDialog

    def __init__(self):   # override constructor method
        windowName = "To Be Delivered"   # sets the window name

        QDialog.__init__(self)   # call QDialog's constructor method (parent)

        layoutHome = QGridLayout()   # add layout for how QWidget should be displayed on screen

        signInLabel = QLabel("<h1>Sign In</h1>")   # create a label widget
        userName = QLineEdit()  # blank line edit
        password = QLineEdit()
        nextButtonSignIn = QPushButton(">")   # create a push button widget
        forgotPWLabel = QLabel("Forward Password?")   
        warningSymbolButton = QPushButton("⚠")
        createNewAccountLabel = QLabel("Don't have an account?")
        createNewAccountButton = QPushButton("Create an account")

        # add placeholder text 
        userName.setPlaceholderText("Username")   # places text that can be overwritten in the ine edit widget
        password.setPlaceholderText("Password")

        # add widgets to layout
        layoutHome.addWidget(signInLabel, 0, 0)  # row, column
        layoutHome.addWidget(userName, 1, 0)
        layoutHome.addWidget(password, 2, 0)
        layoutHome.addWidget(nextButtonSignIn, 2, 1)
        layoutHome.addWidget(forgotPWLabel, 3, 0)
        layoutHome.addWidget(warningSymbolButton, 3, 1)
        layoutHome.addWidget(createNewAccountLabel, 4, 0)
        layoutHome.addWidget(createNewAccountButton, 4, 1)

        # tell QDialog constructor method to use layout to display the elements on the screen
        self.setLayout(layoutHome)

        # connect the widgets with events and handlers
        warningSymbolButton.clicked.connect(self.launchForgotPW)

        # sets name of the window
        self.setWindowTitle(windowName)

    def launchForgotPW(self):
        self.window = forgotPWWindow()
        self.window.show()


app = QApplication(sys.argv)
fileApp = mainWindow()
fileApp.show()
sys.exit(app.exec_())


