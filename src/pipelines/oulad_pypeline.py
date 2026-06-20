from tkinter import INSERT

from util.database_operations import DataBaseOperation
from util.custom_path import get_path_to_csv
from util.csv_reader_helper import CsvReader, ValidationRuleBase
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
    
def bulk_copy(csv_file, table_name, validator: ValidationRuleBase = ValidationRuleBase()):
    db_operations = DataBaseOperation()
    csv_reader = CsvReader()
    csv_path = get_path_to_csv(csv_file)
    csv_header = csv_reader.get_csv_header(csv_path) 
    db_operations.bulk_copy_csv(
        csv_path=csv_path, 
        table_name=table_name,
        columns=list(csv_header),
        validator=validator
    )

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
        
def bulk_copy_courses():
    bulk_copy(csv_file="courses.csv", table_name="courses")

def bulk_copy_assessments():
    bulk_copy(csv_file="assessments.csv", table_name="assessments", validator=AssessmentValidationRule())

def bulk_copy_vle():
    bulk_copy(csv_file="vle.csv", table_name="vle", validator=VleValidationRule())

def bulk_copy_studentInfo():
    bulk_copy(csv_file="studentInfo.csv", table_name="studentInfo", validator=StudentInfoValidationRule())

def bulk_copy_studentRegistration():
    bulk_copy(csv_file="studentRegistration.csv", table_name="studentRegistration", validator=StudentRegistrationValidationRule())

def bulk_copy_studentAssessment():
    bulk_copy(csv_file="studentAssessment.csv", table_name="studentAssessment", validator=StudentAssessmentValidationRule())

def bulk_copy_studentVle():
    bulk_copy(csv_file="studentVle.csv", table_name="studentVle", validator=StudentVleValidationRule())

def bulk_copy_runner():

    # bulk_copy_courses()

    # bulk_copy_assessments()

    # bulk_copy_vle()

    # bulk_copy_studentInfo()

    # bulk_copy_studentRegistration()

    # bulk_copy_studentAssessment()

    bulk_copy_studentVle()