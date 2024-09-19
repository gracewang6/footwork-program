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

        self.label = QLabel(self)
        self.court_image = QPixmap('badminton_court.jpeg').scaled(*initial_size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.FastTransformation)
        self.label.setPixmap(self.court_image)

        self.rect = QRect()
        self.rect.setSize(self.court_image.size())
        self.rect.moveCenter(self.rect().center())
        self.label.setGeometry(self.rect)

    def resizeEvent(self, e):
        super().resizeEvent(e)
        window_size = e.size()
        center = self.rect().center()
        print(center)

    def moveEvent(self, e):
        super().moveEvent(e)
        center = self.rect().center()
        print(center)
    
def main():
    app = QApplication([])
    window = FootworkApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
