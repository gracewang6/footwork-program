import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QGridLayout, QVBoxLayout, QStackedLayout
from PyQt6.QtCore import QTimer, Qt, QPoint, QSize, QRect
from PyQt6.QtGui import QPixmap, QImage, QIcon

# main GUI window

initial_size = (1000, 1000)

class FootworkApp(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Badminton Footwork Training App")
        self.setWindowIcon(QIcon('birdie.png'))
        self.setGeometry(0, 0, *initial_size)

        # create court
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.label = QLabel(self.central_widget)
        self.court_image = QPixmap('badminton_court.jpeg').scaled(*initial_size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.FastTransformation)
        self.label.setPixmap(self.court_image)
        self.label.resize(1000, 1000)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.central_widget.resize(*initial_size)

        # create layers
        central_layout = QVBoxLayout()
        self.central_widget.setLayout(central_layout)
        self.birdies = QWidget(self.central_widget)
        self.birdie_layout = QGridLayout()
        self.birdies.setLayout(self.birdie_layout)
        central_layout.addWidget(self.birdies)
        central_layout.setAlignment(self.birdies, Qt.AlignmentFlag.AlignCenter)

        birdie_image = QPixmap('birdie.png').scaled(initial_size[0]/12.5, initial_size[1]/12.5, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.FastTransformation)
        self.birdie_positions = [(0, 0), (0, 1), (1, 0), (1, 1)]
        for corner, position in enumerate(self.birdie_positions):
            birdie_label = QLabel()
            birdie_label.setPixmap(birdie_image)
            birdie_label.adjustSize()
            self.birdie_layout.addWidget(birdie_label, *position)

        # create start button
        self.start_button = QPushButton("Start", self.central_widget)
        self.button_rect = QRect(0, 0, 100, 40)
        self.button_rect.moveCenter(self.central_widget.rect().center())
        self.start_button.setGeometry(self.button_rect)
        self.start_button.setStyleSheet("background-color : green")
        self.start_button.clicked.connect(self.startTraining)
        
    def resizeEvent(self, e):
        super().resizeEvent(e)
        window_size = e.size()

        # update court size
        self.label.resize(window_size)        
        new_court_image = QPixmap('badminton_court.jpeg').scaled(window_size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.FastTransformation)
        self.label.setPixmap(new_court_image)
        
        # update bird size
        new_birdie_image = QPixmap('birdie.png').scaled(window_size.width()/12.5, window_size.height()/12.5, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.FastTransformation)
        for corner, position in enumerate(self.birdie_positions):
            new_birdie_label = QLabel()
            new_birdie_label.setPixmap(new_birdie_image)
            item = self.birdie_layout.itemAtPosition(*position)
            self.birdie_layout.replaceWidget(item.widget(), new_birdie_label)
            self.birdie_layout.removeWidget(item.widget())
        
        self.central_widget.resize(window_size)
        self.birdies.resize(new_court_image.size())
        self.button_rect.moveCenter(self.central_widget.rect().center())
        self.start_button.setGeometry(self.button_rect)
        
    def startTraining(self):
        print("training")

        
def main():
    app = QApplication([])
    window = FootworkApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
