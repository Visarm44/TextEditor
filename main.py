# File: main.py
import sys
from PyQt6.QtWidgets import QApplication
from src.view.main_window import MainWindow

def main():
    # 1. Creiamo l'istanza dell'applicazione
    # sys.argv serve per passare argomenti da riga di comando (standard)
    app = QApplication(sys.argv)

    window = MainWindow()
    
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()