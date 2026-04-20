class Tasks:
    def __init__(self, id, title, description,completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
    
    #Retorna as informações em formato dict
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description" : self.description,
            "completed" : self.completed
        }

