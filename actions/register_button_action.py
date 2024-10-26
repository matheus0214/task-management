class ButtonAction:
    def __init__(self, tasks, tasks_list_widget) -> None:
        self.tasks = tasks
        self.tasks_list_wg =  tasks_list_widget

    def register(self, input_label):
        task = input_label.get("1.0", "end-1c") 
        self.tasks.add(task)
        self.tasks_list_wg.draw(task)
