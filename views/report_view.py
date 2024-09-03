import tkinter as tk
from tkinter import messagebox, simpledialog
from controllers.report_controller import ReportController
from utils.language_loader import LanguageLoader


class ReportView:
    def __init__(self, root, language="en"):
        self.root = root
        self.controller = ReportController()
        self.language_loader = LanguageLoader(language)

        self.root.title(self.language_loader.get_translation("title"))
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')

        # Styling variables
        self.label_font = ("Arial", 12, "bold")
        self.entry_font = ("Arial", 12)
        self.bg_color = "#f0f0f0"
        self.fg_color = "#333333"
        self.button_bg = "#4CAF50"
        self.button_fg = "#ffffff"
        self.padx = 10
        self.pady = 5

        # Title
        self.title_label = tk.Label(root, text=self.language_loader.get_translation("title"), font=self.label_font, bg=self.bg_color, fg=self.fg_color)
        self.title_label.pack(pady=self.pady)
        self.title_entry = tk.Entry(root, font=self.entry_font, width=50)
        self.title_entry.pack(pady=self.pady)

        # Description
        self.desc_label = tk.Label(root, text=self.language_loader.get_translation("description"), font=self.label_font, bg=self.bg_color, fg=self.fg_color)
        self.desc_label.pack(pady=self.pady)
        self.desc_entry = tk.Text(root, height=5, font=self.entry_font, width=50)
        self.desc_entry.pack(pady=self.pady)

        # Impact
        self.impact_label = tk.Label(root, text=self.language_loader.get_translation("impact"), font=self.label_font, bg=self.bg_color, fg=self.fg_color)
        self.impact_label.pack(pady=self.pady)
        self.impact_entry = tk.Entry(root, font=self.entry_font, width=50)
        self.impact_entry.pack(pady=self.pady)

        # Actions Taken
        self.actions_label = tk.Label(root, text=self.language_loader.get_translation("actions_taken"), font=self.label_font, bg=self.bg_color, fg=self.fg_color)
        self.actions_label.pack(pady=self.pady)
        self.actions_entry = tk.Entry(root, font=self.entry_font, width=50)
        self.actions_entry.pack(pady=self.pady)

        # Severity Level
        self.severity_label = tk.Label(root, text=self.language_loader.get_translation("severity_level"), font=self.label_font, bg=self.bg_color, fg=self.fg_color)
        self.severity_label.pack(pady=self.pady)
        self.severity_entry = tk.Entry(root, font=self.entry_font, width=50)
        self.severity_entry.pack(pady=self.pady)

        # Reported By
        self.reporter_label = tk.Label(root, text=self.language_loader.get_translation("reported_by"), font=self.label_font, bg=self.bg_color, fg=self.fg_color)
        self.reporter_label.pack(pady=self.pady)
        self.reporter_entry = tk.Entry(root, font=self.entry_font, width=50)
        self.reporter_entry.pack(pady=self.pady)

        # Buttons
        self.submit_button = tk.Button(root, text=self.language_loader.get_translation("submit_report"), command=self.submit_report,
                                       font=self.label_font, bg=self.button_bg, fg=self.button_fg, width=20)
        self.submit_button.pack(pady=self.pady)

        self.view_button = tk.Button(root, text=self.language_loader.get_translation("view_reports"), command=self.view_reports,
                                     font=self.label_font, bg=self.button_bg, fg=self.button_fg, width=20)
        self.view_button.pack(pady=self.pady)

        self.update_button = tk.Button(root, text=self.language_loader.get_translation("update_report"), command=self.update_report,
                                       font=self.label_font, bg=self.button_bg, fg=self.button_fg, width=20)
        self.update_button.pack(pady=self.pady)

        self.delete_button = tk.Button(root, text=self.language_loader.get_translation("delete_report"), command=self.delete_report,
                                       font=self.label_font, bg=self.button_bg, fg=self.button_fg, width=20)
        self.delete_button.pack(pady=self.pady)

    def submit_report(self):
        title = self.title_entry.get()
        description = self.desc_entry.get("1.0", tk.END)
        impact = self.impact_entry.get()
        actions = self.actions_entry.get()
        severity = self.severity_entry.get()
        reporter = self.reporter_entry.get()

        self.controller.create_report(title, description, impact, actions, severity, reporter)
        messagebox.showinfo("Success", self.language_loader.get_translation("success_submit"))

    def view_reports(self):
        reports = self.controller.get_reports()
        report_list = ""
        for report in reports:
            report_list += f"ID: {report.id}\nTitle: {report.title}\nReported By: {report.reported_by}\n\n"

        messagebox.showinfo(self.language_loader.get_translation("view_reports"), report_list)

    def update_report(self):
        report_id = simpledialog.askinteger("Input", "Enter Report ID to Update:")
        report = self.controller.get_report_by_id(report_id)
        if report:
            title = simpledialog.askstring("Input", "Enter new title:", initialvalue=report.title)
            description = simpledialog.askstring("Input", "Enter new description:", initialvalue=report.description)
            impact = simpledialog.askstring("Input", "Enter new impact:", initialvalue=report.impact)
            actions_taken = simpledialog.askstring("Input", "Enter new actions taken:", initialvalue=report.actions_taken)
            severity_level = simpledialog.askstring("Input", "Enter new severity level:", initialvalue=report.severity_level)
            reported_by = simpledialog.askstring("Input", "Enter new reporter name:", initialvalue=report.reported_by)

            self.controller.update_report(report_id, title=title, description=description, impact=impact, actions_taken=actions_taken, severity_level=severity_level, reported_by=reported_by)
            messagebox.showinfo("Success", self.language_loader.get_translation("success_update"))
        else:
            messagebox.showwarning("Error", self.language_loader.get_translation("error_report_not_found"))

    def delete_report(self):
        report_id = simpledialog.askinteger("Input", "Enter Report ID to Delete:")
        if self.controller.get_report_by_id(report_id):
            self.controller.delete_report(report_id)
            messagebox.showinfo("Success", self.language_loader.get_translation("success_delete"))
        else:
            messagebox.showwarning("Error", self.language_loader.get_translation("error_report_not_found"))
