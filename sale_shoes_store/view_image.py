from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout

class ImageViewer(QDialog):
    """Окно для просмотра изображений с возможностью переключения"""
    def __init__(self, image_paths):
        super().__init__()
        self.setWindowTitle("Просмотр изображений")
        self.setGeometry(200, 200, 800, 600)

        self.image_paths = image_paths
        self.current_index = 0

        self.layout = QVBoxLayout()

        # Отображение текущего изображения
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.image_label)

        # Кнопки переключения
        button_layout = QHBoxLayout()

        self.prev_button = QPushButton("⟵ Предыдущее", self)
        self.prev_button.clicked.connect(self.show_previous_image)
        button_layout.addWidget(self.prev_button)

        self.next_button = QPushButton("Следующее ⟶", self)
        self.next_button.clicked.connect(self.show_next_image)
        button_layout.addWidget(self.next_button)

        self.layout.addLayout(button_layout)
        self.setLayout(self.layout)

        # Установить стиль
        self.setStyleSheet("""
        QDialog {
            background-color: #121212; /* Темный фон */
            color: #FFFFFF;
        }
        QLabel {
            border: 1px solid #FFFFFF; /* Белая рамка */
        }
        QPushButton {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 8px 16px;
            font-size: 14px;
        }
        QPushButton:hover {
            background-color: #45A049;
        }
        """)

        # Отобразить первое изображение
        self.show_image(self.current_index)

    def show_image(self, index):
        """Показать изображение по индексу"""
        if 0 <= index < len(self.image_paths):
            image_path = self.image_paths[index]
            pixmap = QPixmap(image_path)
            self.image_label.setPixmap(
                pixmap.scaled(750, 550, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            )

    def show_previous_image(self):
        """Показать предыдущее изображение"""
        if self.current_index > 0:
            self.current_index -= 1
            self.show_image(self.current_index)

    def show_next_image(self):
        """Показать следующее изображение"""
        if self.current_index < len(self.image_paths) - 1:
            self.current_index += 1
            self.show_image(self.current_index)
