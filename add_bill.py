# import Printing
import Python_Files.Backend as Backend
from utils.Databases import SELECT, UPDATE
from Python_Files.Requirments import *
from Python_Files.add_bill_py_ import Ui_add_bill
from utils.Qt_Dialogues import error_dialog,ask_dialog
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QGraphicsDropShadowEffect 
from PyQt5.Qt import Qt
class Add_Bill:
    def __init__(self,window) -> None:
        self.main_window = window
        self.Diary_No = Backend.Diary_No(SELECT,"100100")
        
        self.limit=self.total_bill_amount=self.qty_per_bill= None
        self.no_bills = 1
        self.total_list = []
        self.New_Bill_Window = Ui_add_bill()
        self.New_Bill_Window.setupUi(window)

        self.New_Bill_Window.diary_no.setText(self.Diary_No)
        
        # Setting up manage window
        for i in range(3):
            if i == 0:
                w = 300
            else:
                w = 150
            self.New_Bill_Window.manage_table.setColumnWidth(i,w)
        self.New_Bill_Window.managed_note.setText("")

        # Setting up total Window
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(55)
        self.New_Bill_Window.totals_frame.setGraphicsEffect(shadow)
        # Setting Button Commands
        btn_commands = [lambda btn="print": self.Save_Bill(btn),
        lambda btn="save": self.Save_Bill(btn)]
        # Buttons List
        self.btn_list = [self.New_Bill_Window.print,self.New_Bill_Window.save]
        x = 0
        for btn in self.btn_list:
            btn.clicked.connect(btn_commands[x])
            x += 1
        
        
        
        
        # Comboboxes and checkboxes
        self.checkboxes = [self.New_Bill_Window.checkBox,self.New_Bill_Window.checkBox_2,self.New_Bill_Window.checkBox_3,self.New_Bill_Window.checkBox_6,self.New_Bill_Window.checkBox_7,self.New_Bill_Window.checkBox_5,self.New_Bill_Window.checkBox_4]
        self.field_list = [self.New_Bill_Window.depart_names,self.New_Bill_Window.firm_names,self.New_Bill_Window.Sub_Item,self.New_Bill_Window.comp_1,self.New_Bill_Window.comp_2,self.New_Bill_Window.type_item]
        
        

        # setting up table
       
        self.table_entry = Tables(self.New_Bill_Window,self.checkboxes,self.field_list)
        self.table_entry.set_table()
        for checks in range(len(self.checkboxes)):
            if checks == 0 or checks == 3:
                self.checkboxes[checks].toggled.connect(lambda state = self.checkboxes[checks].isChecked(),check=checks:self.table_entry.change_state(state,check))
        
        # Setting Manage Spin
        spin_class = Spin(self.New_Bill_Window,self.table_entry)

    def Printed_Documents(self,selection,print_titles):
        print_mode = []
        comparator = False
        for i in range(len(selection)):
                if selection[i].get() == 1:
                    if i != 0:
                        if print_titles[i] == "Comparator":
                            comparator = True
                        else:
                           print_mode.append(print_titles[i])
        return print_mode,comparator
    def validate_table_data(self,table_data,comparator,selection):
        error = 0
        count = 0
        for i in table_data:
            if comparator == True and (i[9] == 0 or i[10] == 0):
                error = 1
                messagebox.showerror("Invalid Entry",f"پرنٹ کرنے سے پہلے موازنہ کرنے والی فرموں کی قیمت درست کریں۔[Line {count}]")
                return error
            elif (selection[0].get() == 1 or selection[-1].get() == 1) and (i[7] == "" or i[7] == "0" or i[7] == "0.0 (0%)"):
                error = 1
                messagebox.showerror("Invalid Entry",f"پرنٹ کرنے سے پہلے ٹیکس کی قیمت درست کریں۔ [Line {count}]")
                return error
            count += 1
        return error
    def validating_selected_firms(self,fields):
        if fields[2].get() == fields[4].get() or fields[2].get() == fields[5].get() or fields[4].get() == fields[5].get():
            error = 1
            messagebox.showerror("Invalid Entry","برائے مہربانی فرم کا انتخاب درست کیجیئے۔ ایک فرم کو دو دفعہ استعمال نہیں کیا جا سکتا")
        else:
            error = 0
        return error
    def Save_Bill(self,button):
        if self.table.get_children():
            print_mode,comparator = self.Printed_Documents(self.checkboxes,self.prints)
            table_data = fetch_table_data(self.table)
            error = 0
            if button == "print" and len(print_mode) == 0:
                error = 1
                messagebox.showerror("Invalid Selection","آپ کیا پرنٹ کرنا چاہتے ہیں؟ برائے مہربانی انتخاب کیجیئے")
            if error == 0:
                print_status,error = Backend.Validate_Print(self.field_list,print_mode,comparator)
            if error == 0 and button == "print":
                error = self.validate_table_data(table_data,comparator,self.checkboxes)
            if error == 0 and comparator == True:
                error = self.validating_selected_firms(self.field_list)
            if error == 0:
                cheque_no = ""
                status = "pending"
                response = Backend.Save_Bills(self.field_list,table_data,self.Diary_No,"None",print_mode,str(self.limit),status,cheque_no)
                if response == "Done" and button != "print":
                    messagebox.showinfo("Success Notification",f"This Work has been initiated with Diary number {str(self.Diary_No)}")
                elif button != "print":
                    error = 1
                    messagebox.showwarning("Data Maches","This Diary# is already registered in my database.")
                if button == "print":
                    Printing.printing(table_data,self.Diary_No,self.no_bills,self.qty_per_bill,print_mode,self.field_list,self.total_bill_amount,comparator,self.compare_rates)
                    self.Print_Done_Win(print_mode,comparator,self.field_list)
                if error == 0:
                    diary = int(self.Diary_No) + 1
                    Backend.Diary_No(UPDATE,str(diary))
                    self.bill_root.destroy()
                    return "Done"
                else:
                    return "Failed"
        else:
            messagebox.showerror("Invalid Attempt","There is no entry to save")
            return "Failed"
    def Print_Done_Win(self,print_mode,comparator,fields):
        doneWin = Tk()
        doneWin.geometry("500x320")
        doneWin.title("Print Information Window")
        done_frame = Frame(doneWin,bg=fg_color)
        done_frame.pack(fill=BOTH,expand=1)
        titles = ["Bills","Qoutations","Demands","Invoices","Estimate"]
        if comparator:
            loop = 3
            firms = [2,4,5]
        else:
            loop = 1
            firms = [2]
        qoute = 0
        bill = 0
        demand = 0
        invoice = 0
        estimate = 0
        for i in print_mode:
            if i == "Quotation":
                qoute = 1
            elif i == "Bill":
                bill = 1
            elif i == "Estimate":
                estimate = 1
            elif i == "Invoice":
                invoice = 1
            elif i == "Demand":
                demand = 1
        qty_list = [bill,qoute,demand,invoice,estimate]
        entry_values = [int(self.no_bills)*loop*value for value in qty_list]
        y = 40
        for n in range(loop):
            firm_name = Label(done_frame,text=str(fields[firms[n]].get()),bg=fg_color,fg=light_fg,font=font)
            firm_name.pack()
            firm_name.place(x=20,y=y)
            x = 150
            count = 0
            for i in titles:
                title_label = Label(done_frame,text=i,bg=fg_color,fg=bg_color,font=small_font)
                title_label.pack()
                title_label.place(x=x,y=y-20)
                
                entry = Entry(done_frame,bg=fg_color,fg=light_fg,font=font,width=5)
                entry.pack()
                entry.place(x=x,y=y)
                entry.insert(0,str(entry_values[count]))
                entry['state'] = DISABLED
                x += 100
                count += 1
        

    
   
class Spin(QtWidgets.QSpinBox):
    def __init__(self,UI,table_class) -> None:
        super().__init__()
        self.table_entry = table_class
        self.UI = UI
        self.status = False
        self.Table = self.UI.manage_table
        self.Table.keyPressEvent = self.keyPress
    def keyPress(self,event):
        if event.key() == Qt.Key_Return:
            self.Manage_Event()
            print("Done Enter")
    
    def manage_done(self,table_data):
       
        self.UI.pushButton.setEnabled(True)
        data = []
        for i in range(self.no_bills):
            no = i + 1
            no_items = items = ""
            count = 0
            for item_num in self.qty_per_bill[i]:
                if item_num != 0:
                   no_items += str(item_num)
                   item = table_data[count][1]
                   items += str(item)
                if count != len(self.qty_per_bill):
                    items += ","
                    no_items += ","
                count += 1
            data.append([items,no_items,self.total_bill_amount[i]])
        self.insert_into_manage_table(data)


    def Manage_Event(self):
        data = self.table_entry.fetch_table_data()
        if len(data) > 1:
            self.limit = self.UI.limit_spin.value()
            totals = self.table_entry.Update_Total_Label()
            digit,char = Backend.Validate(self.limit)
            if digit == True and char == False and (self.limit != "" and int(self.limit) != 0) and int(self.limit) <= int(totals[2]):
                self.no_bills, self.qty_per_bill,self.final_above_rates,self.total_bill_amount = Backend.Find_Required_Bills(data,int(self.limit),totals)
                if self.no_bills != 0 and self.no_bills != "":
                    self.manage_done(data)
                else:
                    self.UI.managed_note.setText(f"This amount is not managable :( \n {self.final_above_rates[1]} is rated as Rs.{self.final_above_rates[5]} which is above Rs.{str(self.limit)}")
            else:
                error_dialog("Invalid Entery error","Please Enter a valid Number. Number should not be zero and should not greater than total amount","")
        else:
            error_dialog("Data Error","No Items to manage this bill. Please save items first.","NOTE: FIll in above table.")
    def insert_into_manage_table(self,data):
        for rows in range(len(data)):
           for cols in range(self.UI.manage_table.columnCount()):
                item = QtWidgets.QLabel()
                item.setText(data[rows][cols])
                item.setStyleSheet("color:white;\n"
                "background-color:rgb(60, 153, 85);\n")
                item.setAlignment(Qt.AlignCenter)
                self.UI.manage_table.setCellWidget(rows, cols, item)

class Tables(QtWidgets.QTableWidget):
    def __init__(self,UI,checkbox,fields) -> None:
        super().__init__()
        self.compare_rates = []
        self.Item_Count = 1
        self.press_count = 0
        self.Table = UI.table
        self.UI = UI
        self.checkboxes = checkbox
        self.field_list = fields
        self.Table.keyPressEvent = self.keyPress
        depart,Firms,Subject,item_names,specs,unit,types = Backend.Set_Billing_List()
        self.completion_list = [depart,Firms,Subject,Firms,Firms,types]
        self.table_completion = [item_names,specs,unit]

        index = 0
        for i in range(len(self.field_list)):
                count = 0
                for data in self.completion_list[index]:
                    self.field_list[i].addItem("")
                    self.field_list[i].setItemText(count,data)
                    count += 1
                index += 1
    def set_table(self):
        columns = self.Table.columnCount()
        for i in range(columns):
            if i == 0 or i == 1:
                w = 300
            else:
                w = 100
            self.Table.setColumnWidth(i,w)

        rowPosition = self.Table.rowCount()
        self.Table.setRowCount(rowPosition+1)
        self.Table.setColumnCount(columns)
        
        count = 0
        for i in range(columns):
            items_ = QtWidgets.QTableWidgetItem()
            self.Table.setItem(rowPosition, i, items_)
            self.Table.item(rowPosition, i).setForeground(QtGui.QColor(255,255,255))
            if i == 0 or i == 1 or i == 3:
                comboBox = QtWidgets.QComboBox()
                comboBox.setEditable(True)
                index = 0
                for names in self.table_completion[count]:
                        comboBox.addItem("")
                        comboBox.setItemText(index,names)
                        index += 1
                comboBox.setStyleSheet("color:white;")
                self.Table.setCellWidget(rowPosition, i, comboBox)
                count += 1
            else:
                if i >= 5:
                  
                    if (i == 6 and self.checkboxes[0].isChecked() == True) or ((i == 8 or i == 9) and self.checkboxes[3].isChecked() == True):
                        pass
                    elif i != 6 and i != 8 and i != 9:
                        item = QtWidgets.QLabel()
                        item.setStyleSheet("background-color:rgb(50,50,50)")
                        self.Table.setCellWidget(rowPosition, i, item)
                    else:
                        items_.setFlags(QtCore.Qt.ItemIsSelectable)
                        self.Table.setItem(rowPosition,i,items_)
                        self.Table.item(rowPosition, i).setBackground(QtGui.QColor(50,50,50))
            i += 1
    def keyPress(self,event):

        if event.key() == Qt.Key_N:
            self.set_table()
        
        elif event.key() == Qt.Key_Return:
            if self.press_count == 1:
                self.press_count = 0
                self.Add_Bill_Entry()
            else:
                self.press_count += 1
        elif event.key() == Qt.Key_D:
            ans = ask_dialog("Confirmation Dialogue","Do you want to delete the selected row(s)?","NOTE: on pressing yes, I'll delete the row(s)")
            if ans == Backend.QMessageBox.Yes:
                self.remove_rows()
        else:
            self.change_color()
        
        QtWidgets.QTableWidget.keyPressEvent(self.Table,event)
    
    def Add_Bill_Entry(self):
        item_data = self.fetch_row_data(self.Table.currentRow())
        stats,final_list = Backend.New_Item_Validation(self.checkboxes,item_data)
        if stats == 0:
            
            self.UI.limit_spin.setEnabled(True)
            
            if self.Match_Record():
                if item_data[8] != "":
                    self.compare_rates.append([int(item_data[8]),int(item_data[9])])
                else:
                    self.compare_rates.append([0,0])
                self.Item_Count += 1
                self.Insert_into_table(row_data=final_list)
                #self.change_row_color(self.Table.currentRow())
                data = self.Update_Total_Label()
                self.UI.comp1_amount.setText(str(data[3]))
                self.UI.comp2_amount.setText(str(data[4]))
                self.UI.amount_label.setText(str(data[0]))
                self.UI.tax_label.setText(str(data[1]))
                self.UI.grand_total.setText(str(data[2]))
            else:
                error_dialog("Record Matched","Same Item with this rate already exists","Note: Enter Unique item")
    
    def change_color(self):
        for cells in range(self.Table.columnCount()):
            if cells == 5 or cells == 7 or cells == 10 or cells == 11:
                text = self.Table.cellWidget(self.Table.currentRow(),cells)
                text.setStyleSheet("background-color:rgb(224, 114, 114);")
    
    
    def fetch_row_data(self,row):
        data = []
        for cells in range(self.Table.columnCount()):

            if cells == 0 or cells == 1 or cells == 3:
                
                text = self.Table.cellWidget(row,cells)
                value = text.currentText()
                if value == None:
                    value = ""
                data.append(value)
                
            elif cells != 5 and cells != 7 and cells != 10 and cells != 11:
                value = self.Table.item(row,cells)                
                if value.text() == None:
                    value = ""
                    print("None aagya")
                else:
                    value = value.text()
                data.append(value)
            else:
                text = self.Table.cellWidget(row,cells)
                value = text.text()
                if value == None:
                    value = ""
                data.append(value)
        return data
    
    def change_state(self,state,index):

        if index == 0:
            loop_count = 1
        else:
            loop_count = 2
        for count in range(loop_count):
            for rows in range(self.Table.rowCount()):
                items_ = QtWidgets.QTableWidgetItem()

                if index == 0:
                    column = 6
                    field = None
                elif count == 0:
                    column = 8
                    field = 3
                    self.UI.label_12.setText(self.UI.comp_1.currentText())
                    self.UI.label_13.setText(self.UI.comp_2.currentText())
                elif count == 1:
                    column = 9
                    field = 4

                if state:
                    items_.setFlags(QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    if column == 6:
                        self.Table.setItem(rows, column, QtWidgets.QTableWidgetItem("17"))
                    else:
                        self.Table.setItem(rows, column, items_)
                    self.Table.item(rows, column).setBackground(QtGui.QColor(32, 33, 36))
                    if field != None:
                        self.field_list[field].setEnabled(True)
                        self.field_list[field].setStyleSheet("background-color:rgb(50, 50, 50);\n"
                                                              "color:white;\n"
                                                              "border:1px solid white;\n"
                                                            "")
                else:
                    items_.setFlags( QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.Table.setItem(rows, column, items_)
                    self.Table.item(rows, column).setBackground(QtGui.QColor(50, 50, 50))
                    if field != None:
                        self.field_list[field].setEnabled(False)
                        self.field_list[field].setStyleSheet("background-color:rgb(50, 50, 50);\n"
                                                              "color:white;\n"
                                                              "border:1px solid rgb(50, 50, 50);\n"
                                                            "")
                self.Table.item(rows, column).setForeground(QtGui.QColor(255, 255, 255))
                

    def Match_Record(self):
        found = True
        row_list = []
        current_row = []
        for line in range(int(self.Table.rowCount())):
            
            if line == self.Table.currentRow():
                current_row.append(self.fetch_row_data(line))
            else:
                row_list.append(self.fetch_row_data(line))
        
        for rows in range(len(row_list)):
            if str(row_list[0]) == str(current_row[0]) and str(row_list[4]) == str(current_row[4]):
                found = False
                break
        return found
    
    def Insert_into_table(self,row_data):
        positions = [5,6,7,10,11]
        count = 0
        for cols in positions:
            if cols != 6:
                item = QtWidgets.QLabel()
                item.setText(row_data[count])
                item.setStyleSheet("color:white;\n"
                "background-color:rgb(60, 153, 85);\n")
                item.setAlignment(Qt.AlignCenter)
                self.Table.setCellWidget(self.Table.currentRow(), cols, item)
            else:
                self.Table.setItem(self.Table.currentRow(),cols,QtWidgets.QTableWidgetItem(row_data[count]))
            count += 1
        
    def fetch_table_data(self):
        data = []
        for rows in range(self.Table.rowCount()):
            data.append(self.fetch_row_data(rows))
        return data
    def Update_Total_Label(self):
        data = self.fetch_table_data()
        amount = tax = total = comp1 = comp2 = 0.0
        for i in data:
            if i[5] != "" and i[6] != "" and i[7] != "" and i[10] != "" and i[11] != "":
                amount += float(i[5])
                tax_string = str(i[6]).split(" ")
                tax += float(tax_string[0])
                total += float(i[7])
                comp1 += float(i[10])
                comp2 += float(i[11])
        return [amount,tax,total,comp1,comp2]
    def remove_rows(self):
        model = self.model
        indices = self.Table.selectionModel().currentRow() 
        for index in sorted(indices):
            model.removeRow(index.row())
        
