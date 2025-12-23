# File: src/view/main_window.py
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 1. Window setup
        self.setWindowTitle("Modern Text Editor")
        self.resize(800, 600)

        # 2. Central container
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 3. Layout
        self.main_layout = QVBoxLayout()
        central_widget.setLayout(self.main_layout)

        # 4. Aggiungiamo l'Editor di Testo
        self.text_editor = QTextEdit()
        self.text_editor.setPlaceholderText("Scrivi qui il tuo capolavoro...")
        
        # Aggiungiamo l'editor al layout
        self.main_layout.addWidget(self.text_editor)