#!/usr/bin/python3
import uuid
import models
from datetime import datetime

""""class Base"""
class BaseModel:
    def __init__(self, *args, **kwargs):
        dat_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created = datetime.today()
        self.update = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.item():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, dat_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)
            
    def __str__(self):
        return "[{}] ({}) {}.format(self.__class__.__name__, self.id, self.__dict__)"
    
    def save(self):
        self.update_at = datetime.now()
        models.storage.save()
        
    
    
    