from util.csv_reader_helper import ValidationRuleBase
from typing import List

class AssessmentValidationRule(ValidationRuleBase):
    def transform(self, row: List[str]) -> List:
        return [
            row[0],
            row[1],
            row[2],
            row[3],
            row[4] if row[4].strip() != '' else None,
            row[5]
        ]

class VleValidationRule(ValidationRuleBase):
    def transform(self, row: List[str]) -> List:
        return [
            row[0],
            row[1],
            row[2],
            row[3],
            row[4] if row[4].strip() != '' else None,
            row[5] if row[5].strip() != '' else None,
        ]
    
class StudentInfoValidationRule(ValidationRuleBase):
    def __init__(self):
        super().__init__()
        self.inserted = {}
    
    def validate(self, row):
        if row[2] in self.inserted:
            return False
        
        self.inserted[row[2]] = True
        return True

class StudentRegistrationValidationRule(ValidationRuleBase):
    def __init__(self):
        super().__init__()
        self.inserted = {}
        self.key = ''
    
    def validate(self, row):
        self.key = f"{row[0]}{row[1]}{row[2]}".lower()
        if self.key in self.inserted:
            return False
        
        self.inserted[self.key] = True
        return True
    
    def transform(self, row: List[str]) -> List:
        return [
            row[0],
            row[1],
            row[2],
            row[3] if row[3].strip() != '' else None,
            row[4] if row[4].strip() != '' else None
        ]
    
class StudentAssessmentValidationRule(ValidationRuleBase):
    
    def transform(self, row: List[str]) -> List:
        return [
            row[0],
            row[1],
            row[2],
            row[3],
            row[4] if row[4].strip() != '' else None
        ]
    
class StudentVleValidationRule(ValidationRuleBase):
    def __init__(self):
        super().__init__()
        self.inserted = {}
        self.key = ''
    
    def validate(self, row):
        self.key = f"{row[0]}{row[1]}{row[2]}{row[3]}".lower()
        if self.key in self.inserted:
            return False
        
        self.inserted[self.key] = True
        return True