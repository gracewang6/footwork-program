import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QGridLayout, QVBoxLayout, QStackedLayout, QSpacerItem
from PyQt6.QtCore import QTimer, Qt, QPoint, QSize, QRect, QRandomGenerator
from PyQt6.QtGui import QPixmap, QImage, QIcon

initial_size = (800, 800)
small_space = 10
med_space = 64
big_space = 500
bigger_space = 600

class FootworkApp(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Badminton Footwork Training App")
        self.setWindowIcon(QIcon('birdie.png'))
        self.setGeometry(0, 0, *initial_size)
        self.createCourt()
        self.createBirdies()
        self.createStartButton()

    def createCourt(self):
        self.court_rect = QRect()
        self.court_image = QPixmap('badminton_court.jpeg').scaled(*initial_size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.FastTransformation)
        self.court_rect.setSize(self.court_image.size())
        self.court_rect.moveCenter(self.rect().center())
        self.court_label = QLabel(self)
        self.court_label.setPixmap(self.court_image)
        self.court_label.setGeometry(self.court_rect)
        self.court_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def createBirdies(self):
        self.birdies = QWidget(self)
        self.birdie_layout = QGridLayout(self.birdies)
        self.birdies.setGeometry(self.court_rect)
        self.birdie_layout.setGeometry(self.court_rect)
        self.birdies.setLayout(self.birdie_layout)
        self.birdie_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.birdie_layout.setColumnMinimumWidth(0, 20)
        self.birdie_layout.setColumnMinimumWidth(2, 600)
        self.birdie_layout.setColumnMinimumWidth(4, 20)
        self.birdie_layout.setRowMinimumHeight(0, 20)
        self.birdie_layout.setRowMinimumHeight(2, 500)
        self.birdie_layout.setRowMinimumHeight(4, 20)
        for row_or_column in [0, 2, 4]:
            self.birdie_layout.setColumnStretch(row_or_column, 1)
            self.birdie_layout.setRowStretch(row_or_column, 1)

        birdie_image = QPixmap('birdie.png').scaled(initial_size[0]/12.5, initial_size[1]/12.5, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.FastTransformation)
        self.birdie_positions = [(1, 1), (1, 3), (3, 1), (3, 3)]
        for corner, position in enumerate(self.birdie_positions):
            birdie_label = QLabel()
            birdie_label.setPixmap(birdie_image)
            birdie_label.adjustSize()
            self.birdie_layout.addWidget(birdie_label, *position)

    def createStartButton(self):
        self.start_button = QPushButton("Start", self)
        self.button_rect = QRect(0, 0, 80, 20)
        self.button_rect.moveCenter(self.rect().center())
        self.start_button.setGeometry(self.button_rect)
        self.start_button.setStyleSheet("background-color : green")
        self.start_button.clicked.connect(self.startTraining)
        
    def resizeEvent(self, e):
        super().resizeEvent(e)
        window_size = e.size()

        # update court size
        self.new_court_image = QPixmap('badminton_court.jpeg').scaled(window_size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.FastTransformation)
        self.court_rect.setSize(self.new_court_image.size())
        self.court_rect.moveCenter(self.rect().center())
        self.court_label.setGeometry(self.court_rect)
        self.court_label.setPixmap(self.new_court_image)
        self.court_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # update birdie size
        self.birdies.setGeometry(self.court_rect)
        self.birdie_layout.setGeometry(self.court_rect)
        new_birdie_image = QPixmap('birdie.png').scaled(window_size.width()/12.5, window_size.height()/12.5, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.FastTransformation)
        for corner, position in enumerate(self.birdie_positions):
            new_birdie_label = QLabel()
            new_birdie_label.setPixmap(new_birdie_image)
            item = self.birdie_layout.itemAtPosition(*position)
            self.birdie_layout.replaceWidget(item.widget(), new_birdie_label)
            self.birdie_layout.removeWidget(item.widget())

        # update start button
        self.button_rect.moveCenter(self.rect().center())
        self.start_button.setGeometry(self.button_rect)
        
    def startTraining(self):
        random = QRandomGenerator()
        timer = QTimer(self)
        timer.setInterval(5000)
        print(random.bounded(3))



def main():
    app = QApplication([])
    window = FootworkApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
