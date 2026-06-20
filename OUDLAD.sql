-- =========================================
-- Table: courses
-- =========================================
CREATE TABLE courses (
    code_module NVARCHAR(20),
    code_presentation NVARCHAR(20),
    module_presentation_length INT,
    CONSTRAINT PK_courses PRIMARY KEY (code_module, code_presentation)
);
GO
-- =========================================
-- Table: assessments
-- =========================================
CREATE TABLE assessments (
    code_module NVARCHAR(20),
    code_presentation NVARCHAR(20),
    id_assessment INT,
    assessment_type NVARCHAR(50),
    date INT,
    weight FLOAT,
    CONSTRAINT PK_assessments PRIMARY KEY (id_assessment),
    CONSTRAINT FK_assessments_courses FOREIGN KEY (code_module, code_presentation)
        REFERENCES courses(code_module, code_presentation)
);
GO
-- =========================================
-- Table: vle
-- =========================================
CREATE TABLE vle (
    id_site INT PRIMARY KEY,
    code_module NVARCHAR(20),
    code_presentation NVARCHAR(20),
    activity_type NVARCHAR(50),
    week_from INT,
    week_to INT,
    CONSTRAINT FK_vle_courses FOREIGN KEY (code_module, code_presentation)
        REFERENCES courses(code_module, code_presentation)
);
GO
-- =========================================
-- Table: studentInfo
-- =========================================
CREATE TABLE studentInfo (
    code_module NVARCHAR(20),
    code_presentation NVARCHAR(20),
    id_student INT,
    gender NVARCHAR(10),
    region NVARCHAR(50),
    highest_education NVARCHAR(50),
    imd_band NVARCHAR(20),
    age_band NVARCHAR(20),
    num_of_prev_attempts INT,
    studied_credits INT,
    disability NVARCHAR(10),
    final_result NVARCHAR(20),
    CONSTRAINT PK_studentInfo PRIMARY KEY (id_student),
    CONSTRAINT FK_studentInfo_courses FOREIGN KEY (code_module, code_presentation)
        REFERENCES courses(code_module, code_presentation)
);
GO
-- =========================================
-- Table: studentRegistration
-- =========================================
CREATE TABLE studentRegistration (
    code_module NVARCHAR(20),
    code_presentation NVARCHAR(20),
    id_student INT,
    date_registration INT,
    date_unregistration INT NULL,
    CONSTRAINT PK_studentRegistration PRIMARY KEY (code_module, code_presentation, id_student),
    CONSTRAINT FK_studentRegistration_courses FOREIGN KEY (code_module, code_presentation)
        REFERENCES courses(code_module, code_presentation),
    CONSTRAINT FK_studentRegistration_studentInfo FOREIGN KEY (id_student)
        REFERENCES studentInfo(id_student)
);
GO
-- =========================================
-- Table: studentAssessment
-- =========================================
CREATE TABLE studentAssessment (
    id_assessment INT,
    id_student INT,
    date_submitted INT,
    is_banked BIT,
    score FLOAT,
    CONSTRAINT PK_studentAssessment PRIMARY KEY (id_assessment, id_student),
    CONSTRAINT FK_studentAssessment_assessments FOREIGN KEY (id_assessment)
        REFERENCES assessments(id_assessment),
    CONSTRAINT FK_studentAssessment_studentInfo FOREIGN KEY (id_student)
        REFERENCES studentInfo(id_student)
);
GO
-- =========================================
-- Table: studentVle
-- =========================================
CREATE TABLE studentVle (
    code_module NVARCHAR(20),
    code_presentation NVARCHAR(20),
    id_student INT,
    id_site INT,
    date INT,
    sum_click INT,
    CONSTRAINT PK_studentVle PRIMARY KEY (code_module, code_presentation, id_student, id_site, date),
    CONSTRAINT FK_studentVle_courses FOREIGN KEY (code_module, code_presentation)
        REFERENCES courses(code_module, code_presentation),
    CONSTRAINT FK_studentVle_studentInfo FOREIGN KEY (id_student)
        REFERENCES studentInfo(id_student),
    CONSTRAINT FK_studentVle_vle FOREIGN KEY (id_site)
        REFERENCES vle(id_site)
);
GO


----------------

--DROPT TABLES
DROP TABLE studentVle 
DROP TABLE studentAssessment
DROP TABLE studentRegistration 
DROP TABLE studentInfo
DROP TABLE vle 
DROP TABLE assessments 
DROP TABLE courses 