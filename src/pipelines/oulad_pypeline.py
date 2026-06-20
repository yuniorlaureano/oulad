from util.database_operations import DataBaseOperation
from util.custom_path import get_path_to_csv
from util.csv_reader_helper import CsvReader, ValidationRuleBase
from pipelines.rule_validators import (
    AssessmentValidationRule,
    VleValidationRule,
    StudentInfoValidationRule,
    StudentRegistrationValidationRule,
    StudentAssessmentValidationRule,
    StudentVleValidationRule)
from pipelines.queries import DROP_TABLES, CREATE_TABLES

def bulk_copy(csv_file, table_name, validator: ValidationRuleBase = ValidationRuleBase()):
    db_operations = DataBaseOperation()
    csv_reader = CsvReader()
    csv_path = get_path_to_csv(csv_file)
    csv_header = csv_reader.get_csv_header(csv_path) 
    db_operations.bulk_copy_csv(
        csv_path=csv_path, 
        table_name=table_name,
        columns=list(csv_header),
        validator=validator,
        chunk_size=50_000
    )

def drop_tables():
    print("Dropping tables.....")
    db_operations = DataBaseOperation()
    db_operations.execute(
        query=DROP_TABLES
    )

def create_tables():
    print("Creating tables.....")
    db_operations = DataBaseOperation()
    db_operations.execute(
        query=CREATE_TABLES
    )
        
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

    drop_tables()

    create_tables()

    bulk_copy_courses()

    bulk_copy_assessments()

    bulk_copy_vle()

    bulk_copy_studentInfo()

    bulk_copy_studentRegistration()

    bulk_copy_studentAssessment()

    bulk_copy_studentVle()