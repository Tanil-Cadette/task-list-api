from app import db

class Goal(db.Model):
    goal_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    tasks = db.relationship("Task", back_populates="goal")
    
    def to_dict(self):
        goal_as_dict = {}
        goal_as_dict["id"]= self.goal_id
        goal_as_dict["title"]=self.title
    
        return goal_as_dict
    
    @classmethod   
    def from_dict(cls, goal_data):
        new_goal= Goal(title=goal_data["title"]
        )         
        return new_goal
    
    def update(self, req_body):
        try:
            self.title = req_body["title"]
        except KeyError as error:
            raise error
