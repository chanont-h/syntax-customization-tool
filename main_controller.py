class MainController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.setup_connections()

    def setup_connections(self):
        self.view.save_template_signal.connect(self.save_template)
        self.view.load_template_signal.connect(self.load_template)

    def save_template(self, template_data):
        if self.model.validate_template(template_data):
            self.model.save_template(template_data)
            self.view.show_message("Template saved successfully.")
        else:
            self.view.show_message("Invalid template data.")

    def load_template(self, template_name):
        template_data = self.model.load_template(template_name)
        if template_data:
            self.view.display_template(template_data)
        else:
            self.view.show_message("Template not found.")