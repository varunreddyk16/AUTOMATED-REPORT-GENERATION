# AUTOMATED-REPORT-GENERATION

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : K VARUN REDDY

*INTERN ID* : CT08SGE

*DOMAIN* : PYTHON PROGRAMMING

*DURATION* : 4 WEEKS

*MENTOR* : NEELA SANTHOSH

**
HERE THE MAIN PURPOSE OF THESE SCRIPT IS TO READ THE DATA FROM A CSV FILE AND TO GENERATE A PDF FILE USING REPORTLAB LIBRARY . THE MAIN PURPOSE OF REPORTLAB LIBRARY IN PYTHON IS TO READ DATA AND TO GENERATE A PDF FILE WHICH IS CUSTOMIZABLE AND IT PROVIDES LOT OF FUNCTIONS WHICH ENHANCES THE REPORT IN PDF FILE.
1) IMPORTING MODULES
   CSV MODULE IS IMPORTED TO READ CSV DATA , AND FROM REPORTLAB WE IMPORTED SOME CLASSES,SUB MODULES ETC..SUCH AS PAGESIZES.LETTER TO PROVIDE PAGE SIZE FOR PDF , .COLORS PROVIDE VARIOUS COLORS FOR STYLING THE PDF , GETSAMPLESTYLESHEET TO GET STYLES FOR TEXT IN PDF,AND PLAYTPUS TO CREATE TABLE IN PDF .SO EVERY MODULE HAVE THEIR UNIQUE FUNCTIONS ,WE CAN'T IMPORT ALL THOSE AT A TIME BECAUSE SUB MODULES MAY NOT BE INCLUDED THAT WAY.

2) READ CSV FUNCTION
   MAIN PURPOSE OF THIS FUNCTION IS TO READ DATA FROM A CSV FILE AND TO STORE THEM TO A LIST OF DICTIONARIES . HERE WE ARE PASSING THE FILE_PATH OF CSV FILE AS ARGUMENT . AND WE ARE CONSIDERING A EMPTY LIST AS DATA[] . NOW WE ARE OPENING THE CSV FILE IN READ MODE , CSV.DICTREADER READS EACH ROW AS DICTIONARY WHERE KEYS ARE THE COLUMN HEADERS ,WE ARE APPENDING EACH ROW TO THE DATA LIST AND RETURNING THE DATA .

3) GENERATE_PDF_REPORT FUNCTION
   THE MAIN PURPOSE OF THIS FUNCTION IS TO GENERATE A PDF REPORT FROM THE DATA RETURNED FROM READ_CSV FUNCTION AND SAVE THE REPORT TO A SPECIFIC OUTPUT FILE. HERE WE ARE PASSING 2 PARAMETERS ,ONE IS THE DATA FROM READ_CSV FUNCTION AND A PATH WHERE THE DATA WILL BE SAVED . FIRST WE ARE INITIALIZING A PDF DOCUMENT USING "SIMPLEDOCTEMPLATE " FUNCTION .WE ARE CONSIDERING AN EMPTY LIST CONTENT[] TO HOLD THE ELEMENTS TO ADD IT TO PDF. NOW USING "PARAGRAPH" WE ARE CREATING PARAGRAPH TITLE i.e "EMPLOYEE DATA REPORT" WITH "TITLE" STYLE , AND WE ARE APPENDING THE TITLE TO THE CONTENT LIST.IN ORDER TO CREATE A TABLE FIRST WE NEED TO GET TABLE DATA THAT NEED TO BE INSERTED SO "TABLE_DATA" IS A LIST OF LIST THAT CONTAIN COLUMNS NAME,AGE,CITY,SALARY AND FOLLOWING LISTS CONTAIN THE DATA.WE ARE APPENDING THE FOLLOWING ROWS BY ITERING THROUGH "DATA" THAT IS RETURNED BY "READ_CSV" FUNCTION . NOW THAT WE GOT THE TABLE DATA IN LIST OF LISTS ,WE CREATE A TABLE NOW. "TABLE(TABLE_DATA)" CREATES A TABLE WITH THE "TABLE_DATA[] []" TO MAKE THE TABLE LOOK GOOD WE ARE APPLYING SOME STYLING ."TABLE.SETSTYLE" , HEADER ROW HAS GREY BACKGROUND ,WHITE TEXT AND ALL CELLS ARE ALIGNED AT CENTER ,GRID LINES ARE ADDED TO TABLE .TO MAKE STLING I HAVE TRIED VARIOUS COLORS AND ALL TO GET CORRECT OADDING,ALIGNMENT ETC... NOW THE TABLE IS APPENDED TO CONTENT LIST .USING "DOC.BUILD(CONTENT)" WE ARE CREATING THE PDF


*OUTPUT* :
![Image](https://github.com/user-attachments/assets/47530edc-f341-475d-a540-8eb5909be40c)

5) IN MAIN FUNCTION
   IN MAIN FUNCTION WE ARE CALLING READ_CSV AND GENERATE_PDF_REPORT FUNCTION ,WE ARE PASSING DATA RETURNED BY READ_CSV FUNCTION TO GENERATE_PDF_REPORT FUNCTION AS ARGUMENT . NOW THAT PDF IS GENERATED ,TO VIEW THE PDF I USED PDF PREVIEW EXTENSION . 

THIS IS HOW I GOT TO CREATE THIS PDF USING REPORTLAB. THOUGH IT WAS CHALLENGING AS I WAS NEW TO REPORTLAB LIBRARY ,I HAVE TAKEN THE HELP OF ONLINE RESOURCES TO MAKE THIS . IT FEELS PRODUCTIVE TO LEARN NEW THINGS...
THANKYOU FOR READING...
