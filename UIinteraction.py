import os

from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox, QTableWidgetItem, QPushButton
from PyQt5.QtCore import Qt, QDate, QTime
from PyQt5.QtGui import QColor, QFont, QPixmap

from MainFrameUI import UI_MainWindow
from AddEventUI import UI_AddEvent
from CalendarUI import UI_Calendar
from AccountUI import UI_Account
import EventsDBControl


class MainWindow(QMainWindow, UI_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.calendarBtn.clicked.connect(self.open_calendar)
        self.addEventBtn.clicked.connect(self.open_add_event_dialog)
        self.accountBtn.clicked.connect(self.open_account)
        self.calendarWindow = None
        self.accountWindow = None
        self.db = EventsDBControl.EventDatabase()
        self.populate_event_tables()
        self.set_column_widths(self.activeEventsTable)
        self.set_column_widths(self.inactiveEventsTable)

        # Load user image and setup dialogue panel
        self.user_info_file = "UserInfo.txt"
        self.load_and_set_user_image()
        self.load_and_set_dialogue_panel()
        self.load_and_set_dialogue_label()

    def showEvent(self, event):
        """Called each time the window is shown"""
        self.load_and_set_user_image()
        self.load_and_set_dialogue_label()
        super().showEvent(event)

    def load_and_set_user_image(self):
        image_path = "static/img/cute_penguin.jpg"  # Default if no index in file
        image_index = 0
        if os.path.exists(self.user_info_file):
            with open(self.user_info_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                if len(lines) >= 3:
                    image_index_str = lines[2].strip()
                    try:
                        image_index = int(image_index_str)
                    except ValueError:
                        print("Некорректный индекс картинки в файле.")
        image_paths = [
            "static/img/cute_penguin.jpg",
            "static/img/cute_fox.jpg",
            "static/img/cute_corgi.jpg"
        ]

        if image_index >= 0 and image_index < len(image_paths):
            image_path = image_paths[image_index]
        else:
            image_path = "static/img/cute_penguin.jpg"
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaled(140, 140, Qt.KeepAspectRatio)
            self.accountImage.setPixmap(scaled_pixmap)
        else:
            self.accountImage.setText("Не удалось загрузить изображение")

    def load_and_set_dialogue_panel(self):
        dialogue_panel_path = "static/img/dialogue_thing.png"
        pixmap = QPixmap(dialogue_panel_path)
        if not pixmap.isNull():
            label_width = self.dialoguePanel.width()
            label_height = self.dialoguePanel.height()
            scaled_pixmap = pixmap.scaled(label_width, label_height, Qt.KeepAspectRatio)
            self.dialoguePanel.setPixmap(scaled_pixmap)
        else:
            self.dialoguePanel.setText("Не удалось загрузить изображение диалога")

    def load_and_set_dialogue_label(self):
        name = ""
        birthdate_str = ""
        if os.path.exists(self.user_info_file):
            with open(self.user_info_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                if len(lines) >= 1:
                    name = lines[0].strip()
                if len(lines) >= 2:
                    birthdate_str = lines[1].strip()

        dialogue_text = "Привет!"
        if name:
            dialogue_text = f"Привет, {name}!"

        today = QDate.currentDate()  # Используем QDate.currentDate()
        try:
            birth_date = QDate.fromString(birthdate_str, "dd.MM")
            if birth_date.month() == today.month() and birth_date.day() == today.day():
                dialogue_text += "\nС днюшкой!"
        except ValueError:
            pass  # Ignore invalid date format

        self.dialogueLabel.setText(dialogue_text)

    def populate_event_tables(self):
        self.populate_table(self.activeEventsTable, 1)
        self.populate_table(self.inactiveEventsTable, 0)

    def set_column_widths(self, table):
        table.setColumnWidth(0, 200)
        table.setColumnWidth(1, 150)
        table.setColumnWidth(2, 100)
        table.setColumnWidth(3, 100)
        table.setColumnWidth(4, 200)  # Ширина колонки с кнопкой

    def populate_table(self, table, is_active):
        table.clearContents()
        table.setRowCount(0)
        table.setColumnCount(5)  # Добавлено для кнопки "Изменить"
        events = self.db.get_events_by_status(is_active)

        if events:
            for event in events:
                row_position = table.rowCount()
                table.insertRow(row_position)

                name_item = QTableWidgetItem(event[1])
                name_item.setFlags(name_item.flags() & ~Qt.ItemIsEditable)
                table.setItem(row_position, 0, name_item)

                table.setItem(row_position, 1, QTableWidgetItem(event[2]))
                table.setItem(row_position, 2, QTableWidgetItem(event[3]))
                table.setItem(row_position, 3, QTableWidgetItem(event[4]))

                table.item(row_position, 1).setFlags(table.item(row_position, 1).flags() & ~Qt.ItemIsEditable)
                table.item(row_position, 2).setFlags(table.item(row_position, 2).flags() & ~Qt.ItemIsEditable)
                table.item(row_position, 3).setFlags(table.item(row_position, 3).flags() & ~Qt.ItemIsEditable)

                # Add a button to each row - using functools.partial
                import functools
                edit_button = QPushButton("Изменить")
                edit_button.setStyleSheet("""
                           QPushButton {
                               background-color: white;
                               border-radius: 20%;
                           }
                           QPushButton:hover' {
                               background-color: #f0f0f0;
                           }
                           QPushButton:pressed {
                               background-color: #e0e0e0;
                           }""")
                edit_button.clicked.connect(functools.partial(self.open_edit_dialog, event[0], table, row_position))
                table.setCellWidget(row_position, 4, edit_button)

        else:
            row_position = table.rowCount()
            table.insertRow(row_position)
            table.setItem(row_position, 0, QTableWidgetItem("Мероприятий этого типа нет"))
            # Disable other columns for better visual clarity
            for i in range(1, 5):
                table.setItem(row_position, i, QTableWidgetItem(""))
            table.setSpan(row_position, 0, 1, 5)  # Span message across all columns

    def open_edit_dialog(self, event_id, table, row):
        event = self.db.get_event_by_id(event_id)
        if event:
            dialog = AddEventDialog(self, event)  # Pass event data to the dialog
            if dialog.exec_() == QDialog.Accepted:
                self.populate_event_tables()

    def open_add_event_dialog(self):
        current_date = QDate.currentDate()  # Get today's date
        dialog = AddEventDialog(self, event=None, date=current_date)  # Pass today's date to the dialog
        if dialog.exec_() == QDialog.Accepted:
            self.populate_event_tables()

    def open_calendar(self):
        if self.calendarWindow is None:
            self.calendarWindow = Calendar(self)
        self.calendarWindow.show()
        self.hide()

    def open_account(self):
        if self.accountWindow is None:
            self.accountWindow = Account(self)  # Pass self as parent
        self.accountWindow.show()
        self.hide()

    def closeEvent(self, event):
        self.db.close()
        super().closeEvent(event)


class Calendar(QMainWindow, UI_Calendar):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)  # Load the UI file
        self.main_window = main_window
        self.eventsBtn.clicked.connect(self.return_to_main)
        self.accountBtn.clicked.connect(self.open_account)
        self.accountWindow = None
        self.db = EventsDBControl.EventDatabase()
        self.highlight_today()

        # VERY IMPORTANT: Connect the signal!
        self.calendarWidget.clicked.connect(self.update_chosen_date)
        self.add_listeners_to_buttons()

    def add_listeners_to_buttons(self):
        self.showEventButton1.clicked.connect(lambda: self.open_event_details(0))
        self.showEventButton2.clicked.connect(lambda: self.open_event_details(1))
        self.showEventButton3.clicked.connect(lambda: self.open_event_details(2))
        self.showEventButton4.clicked.connect(lambda: self.open_event_details(3))
        self.showEventButton5.clicked.connect(lambda: self.open_event_details(4))
        self.addEventBtn.clicked.connect(self.open_add_event_dialog)

    def open_account(self):
        if self.accountWindow is None:
            self.accountWindow = Account(self.main_window)
        self.accountWindow.show()
        self.hide()

    def closeEvent(self, event):
        self.db.close()  # Close the database connection when the window is closed
        event.accept()

    def highlight_today(self):
        today = QDate.currentDate()
        current_format = self.calendarWidget.dateTextFormat(today)  # Get current format
        current_format.setForeground(QColor("#000000"))  # Set text color
        current_format.setFont(QFont("Roboto", 9, QFont.Bold))  # Set font
        self.calendarWidget.setDateTextFormat(today, current_format)
        today_str = today.toString("dd-MM-yyyy")
        self.update_chosen_date()
        self.check_events_for_date(today_str)

    def update_chosen_date(self):
        selected_date = self.calendarWidget.selectedDate()
        formatted_date = selected_date.toString("dd-MM-yyyy")
        self.ChosenDate.setText(formatted_date)
        self.check_events_for_date(formatted_date)

    def return_to_main(self):
        self.main_window.show()
        self.hide()

    def check_events_for_date(self, selected_date):
        events = self.db.get_events_by_date(selected_date)
        self.hide_all_event_buttons()
        if events:
            self.NoEventsLabel.hide()
            self.show_necessary_buttons(len(events), events)

        else:
            self.NoEventsLabel.setText("На текущую дату мероприятий нет")
            self.NoEventsLabel.show()  # Show no events label
        self.current_selected_date = selected_date

    def show_necessary_buttons(self, count, events):
        for i in range(5):  # Перебираем все возможные кнопки
            if i < count:  # если кнопка должна быть видна
                event_name = events[i][1]
                match i:
                    case 0:
                        self.showEventButton1.setText(event_name)
                        self.showEventButton1.show()
                    case 1:
                        self.showEventButton2.setText(event_name)
                        self.showEventButton2.show()
                    case 2:
                        self.showEventButton4.setText(event_name)
                        self.showEventButton3.show()
                    case 3:
                        self.showEventButton4.setText(event_name)
                        self.showEventButton4.show()
                    case 4:
                        self.showEventButton4.setText(event_name)
                        self.showEventButton5.show()

    def hide_all_event_buttons(self):
        self.showEventButton1.hide()
        self.showEventButton2.hide()
        self.showEventButton3.hide()
        self.showEventButton4.hide()
        self.showEventButton5.hide()

    def open_event_details(self, event_index):
        events = self.db.get_events_by_date(self.current_selected_date)
        if events and len(events) > event_index:
            event_data = events[event_index]
            # Create and show the AddEventDialog with event data
            event_dialog = AddEventDialog(self, event_data)  # Pass event_data
            result = event_dialog.exec_()  # Open dialog as modal
            if result == 1:  # If dialog was accepted, refresh data
                self.update_chosen_date()

        else:
            print("Не найдено данных о событии.")

    def open_add_event_dialog(self):
        selected_date = self.calendarWidget.selectedDate()

        event_dialog = AddEventDialog(self, event=None, date=selected_date)  # No event, but pass date
        result = event_dialog.exec_()
        if result == 1:
            self.update_chosen_date()


class AddEventDialog(QDialog, UI_AddEvent):
    def __init__(self, parent=None, event=None, date=None):  # Accept event data and optional date
        super().__init__(parent)
        self.setupUi(self)
        self.db = EventsDBControl.EventDatabase()
        self.saveEventDataBtn.clicked.connect(self.save_event)
        self.deleteEventDataBtn.clicked.connect(self.delete_event)
        self.event_id = None  # to track existing event ID

        if event:
            self.headerLabelText.setText("Изменить мероприятие")
            self.deleteEventDataBtn.show()
        else:
            self.headerLabelText.setText("Добавить мероприятие")
            self.deleteEventDataBtn.hide()

        if event:  # Populate fields if event is passed
            self.event_id = event[0]
            self.eventDate.setDate(QDate.fromString(event[2], "dd-MM-yyyy"))  # corrected index
            self.eventName.setText(event[1])  # corrected index
            self.eventTime.setTime(QTime.fromString(event[3], "HH:mm"))
            self.eventBudget.setText(str(event[4]))
            is_active = event[5] == 1
            self.radioBtnIsActive.setChecked(is_active)
            self.radioBtnIsPlanned.setChecked(not is_active)
        if date:
            self.eventDate.setDate(date)

    def save_event(self):
        event_name = self.eventName.text()
        event_date = self.eventDate.date().toString("dd-MM-yyyy")
        event_time = self.eventTime.time().toString("HH:mm")
        event_budget = self.eventBudget.text()
        event_is_active = 1 if self.radioBtnIsActive.isChecked() else 0

        if not event_name:
            QMessageBox.warning(self, "Ошибка", "Поле 'Название' не может быть пустым.")
            return

        try:
            event_budget = float(event_budget)
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Неверный формат бюджета.")
            return
        if self.event_id:
            self.db.update_event(self.event_id, event_name, event_date, event_time, event_budget, event_is_active)
        else:
            self.db.add_event(event_name, event_date, event_time, event_budget, event_is_active)

        self.accept()

    def delete_event(self):
        if QMessageBox.question(self, "Подтверждение удаления",
                                "Вы действительно хотите удалить это мероприятие?",
                                QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            self.db.delete_event(self.event_id)
            self.accept()  # Закрываем диалог после успешного удаления


class Account(QMainWindow, UI_Account):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        self.eventsBtn.clicked.connect(self.return_to_main)
        self.calendarBtn.clicked.connect(self.open_calendar)
        self.calendarWindow = None
        self.image_paths = [
            "static/img/cute_penguin.jpg",
            "static/img/cute_fox.jpg",
            "static/img/cute_corgi.jpg"
        ]
        self.current_index = 0
        self.load_image()
        self.previousButton.clicked.connect(self.show_previous_image)
        self.nextButton.clicked.connect(self.show_next_image)
        self.saveUserDataBtn.clicked.connect(self.save_user_info)  # Подключаем кнопку "Сохранить"
        self.userBirthdate.setDate(QDate.fromString("", "dd.MM"))

        self.user_info_file = "UserInfo.txt"
        self.load_user_info()

    def open_calendar(self):
        if self.calendarWindow is None:
            self.calendarWindow = Calendar(self.main_window)
        self.calendarWindow.show()
        self.hide()

    def load_image(self):
        if not self.image_paths:
            return

        image_path = self.image_paths[self.current_index]
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            self.imageLabel.setText(f"Файл {image_path} не найден")
            return
        scaled_pixmap = pixmap.scaled(250, 250, Qt.KeepAspectRatio)
        self.imageLabel.setPixmap(scaled_pixmap)

    def show_previous_image(self):
        if self.image_paths:
            self.current_index = (self.current_index - 1) % len(self.image_paths)
            self.load_image()

    def show_next_image(self):
        if self.image_paths:
            self.current_index = (self.current_index + 1) % len(self.image_paths)
            self.load_image()

    def return_to_main(self):
        self.main_window.show()
        self.hide()

    def load_user_info(self):
        if os.path.exists(self.user_info_file):
            with open(self.user_info_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                if not lines:  # Check if file is empty
                    self.current_index = 0
                    self.load_image()
                    return
                if len(lines) >= 3:
                    name = lines[0].strip()
                    birthdate_str = lines[1].strip()
                    image_index_str = lines[2].strip()
                    self.userName.setText(name)
                    try:
                        birth_date = QDate.fromString(birthdate_str, "dd.MM")
                        self.userBirthdate.setDate(birth_date)
                    except ValueError:
                        print("Некорректный формат даты в файле.")
                    try:
                        self.current_index = int(image_index_str)
                        if self.current_index < 0 or self.current_index >= len(self.image_paths):
                            self.current_index = 0
                    except ValueError:
                        print("Некорректный индекс картинки в файле.")
                        self.current_index = 0
                    finally:
                        self.load_image()
                else:
                    self.load_image()  # Load default image

    def save_user_info(self):
        name = self.userName.text().strip()
        birthdate = self.userBirthdate.date().toString("dd.MM")
        with open(self.user_info_file, 'w', encoding='utf-8') as f:
            f.write(name + "\n")
            f.write(birthdate + "\n")
            f.write(str(self.current_index) + "\n")
