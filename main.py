import tkinter as tk
from views.report_view import ReportView


def main():
    root = tk.Tk()
    app = ReportView(root, language="en")  # Change "fr" to "en" for English or any other language code
    root.mainloop()


if __name__ == '__main__':
    main()
