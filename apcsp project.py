
import wx

# code using wx library was written by the student with help from the wx documentation
# https://docs.wxpython.org/index.html
# this excludes the AI generated piece which is specifically labeled in the code below
class ToDoItem(wx.Panel):
    def __init__(self, parent, task, priority, delete):
        super().__init__(parent)
        self.task = task
        self.priority = priority
        self.delete = delete

        # creating checkbox and priority list for To Do List
        self.checkbox = wx.CheckBox(self, label=task)
        self.priority_label = wx.StaticText(self, label=self.get_priority(priority))

        self.checkbox.Bind(wx.EVT_CHECKBOX, self.get_checkbox_checked)

        # creating horizontal sizers for UI 
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.checkbox, 0, wx.ALL, 5)
        sizer.Add(self.priority_label, 0, wx.ALL, 5)

        self.SetSizer(sizer)
        self.Layout()

    # returns priority list given to user
    def get_priority(self, priority):
        if priority == 0:
            return "High Priority"
        elif priority == 1:
            return "Medium Priority"
        else:
            return "Low Priority"

    # this function is called when the checkbox is checked
    def get_checkbox_checked(self, event): 
        if self.checkbox.GetValue(): # this loop deletes a task when its checkbox is clicked.
            self.Destroy()  
            self.delete(self) 

class ToDoListFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="To-Do List", size=(600, 400))

        # the code in the segment (lines 50-72) responsible for setting up the UI application was generated by ChatGPT  
        # this code creates vertical and horizontal spacers for the user inputs and To Do List UI
        # this is in charge of creating and spacing the list and all inputs properly
        self.panel = wx.Panel(self)
        self.high_priority_sizer = wx.BoxSizer(wx.VERTICAL)
        self.medium_priority_sizer = wx.BoxSizer(wx.VERTICAL)
        self.low_priority_sizer = wx.BoxSizer(wx.VERTICAL)

        self.task_text_ctrl = wx.TextCtrl(self.panel, style=wx.TE_PROCESS_ENTER)
        self.priority_choice = wx.Choice(self.panel, choices=["High Priority", "Medium Priority", "Low Priority"])
        self.priority_choice.SetSelection(0)
        self.add_button = wx.Button(self.panel, label="Add Task")
        self.add_button.Bind(wx.EVT_BUTTON, self.add_task) # add_task() is called when the user clicks the button labeled "Add Task"

        input_sizer = wx.BoxSizer(wx.HORIZONTAL)
        input_sizer.Add(self.task_text_ctrl, 1, wx.ALL | wx.EXPAND, 5)
        input_sizer.Add(self.priority_choice, 0, wx.ALL | wx.EXPAND, 5)
        input_sizer.Add(self.add_button, 0, wx.ALL | wx.EXPAND, 5)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(input_sizer, 0, wx.EXPAND|wx.ALL, 10)
        main_sizer.Add(self.high_priority_sizer, 1, wx.EXPAND|wx.ALL, 10)
        main_sizer.Add(self.medium_priority_sizer, 1, wx.EXPAND|wx.ALL, 10)
        main_sizer.Add(self.low_priority_sizer, 1, wx.EXPAND|wx.ALL, 10)

        self.panel.SetSizer(main_sizer)
       
    # this function creates a task based on the users input and displays it on the UI application
    def add_task(self, event): 
        # add_task() with the parameters of self (the class ToDoListFrame) and event (the user interacting with the list) 
        # is what manages the users input, adding tasks to the to-do list in a designated order
        task = self.task_text_ctrl.GetValue() # sets the variable task to the users input from the UI textbox
        priority = self.priority_choice.GetSelection() # sets variable priority to the users input from 

        # this loop organizes the tasks added by the user, selecting which task belongs in which list. it does this by storing the 
        # tasks inputted by the user in three different lists based on their priority level. the code iterates through the 
        # priority lists, sequencing each task and displaying it on the to-do list in order to allow the program to output 
        # an organized to-do list, showing the users tasks from high priority to low priority, in order to help the user 
        # complete their work accordingly.
        if task:
            todo_item = ToDoItem(self.panel, task, priority, self.delete_task)
            if priority == 0:
                self.high_priority_sizer.Add(todo_item, 0, wx.ALL | wx.EXPAND| wx.ALIGN_TOP, 5)
            elif priority == 1:
                self.medium_priority_sizer.Add(todo_item, 0, wx.ALL | wx.EXPAND| wx.ALIGN_TOP, 5)
            else:
                self.low_priority_sizer.Add(todo_item, 0, wx.ALL | wx.EXPAND| wx.ALIGN_TOP, 5)
            self.panel.Layout()
            self.task_text_ctrl.SetValue("")

    # this function updates the UI when a task is deleted
    def delete_task(self, task_item): 
        for sizer in [self.high_priority_sizer, self.medium_priority_sizer, self.low_priority_sizer]:
            if sizer.FindItem(task_item) != wx.NOT_FOUND:
                sizer.Remove(task_item)
                break
        self.panel.Layout()

# main
if __name__ == "__main__":
    app = wx.App(False)
    frame = ToDoListFrame()
    frame.Show(True)
    app.MainLoop()
