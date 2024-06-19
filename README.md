# BMI Calculator: a body mass index calculation app

'BMI Calculator' is a command-line-interface (CLI) health app hosted as an app on Heroku, written in Python.

## Purpose 
The objective of this app is to provide the user with a guidence to reach and maintain healthy body weight. Through calculation of
body mass index, the application will update the user about the current body weight range and let's the user track the changes over 
time.

## Requirement Gathering and Planning

Before starting the coding for this project, I took the time to think about how to set up the architecture of this app, the layout of the output on the console and the functionality required to provide a good user experience. As the CI study material advised, I kept it simple,
and I tried to follow a 'linear' logic.

![Wireframe logic](documentation/wireframelogic.png)

## User Demographics, Stories and Needs

### Target Demographic
This app is useful for anyone wanting to track and control their body mass index and through that, their health.
Abnormal bodyweight is linked with several illness and disases, when one decides to make change for the better, the use of this application
could be the first step towards a healthier lifestyle.

 Some examples of such people are: 

- Family hiatory: people who's family has a history of diabetes, heart disease, obesity.
- Sendentary lifestyle: People at full time work and with familiy duties who won't have time for their own activities, always low
on energy. 
- Eating disorder/ body image issues: people who are follow extreme diets, trends, pursuing the lowest possible body weight.

### User Stories

|As a body mass index calculator user, I want to... | So that... |
|--------|--------|
| ...check my body mass index. | ...I will have an indicator of my generic health. |
| ...know that in what weight category do I fall. | ...I would know if I have to gain, maintain or lose weight.|
| ...receive specific information with regards of my weight. | ...I will have a clear number to gain or lose. |
| ...I want to save my calculation. | ...I can start tracking my weight change, bmi change over time. |
| ...to be able to re-do the calculation. | ...in case any of my details were not accurate, I could repeat the calculation. |
| ...to be able to delete my last calculation, results. | ...noone else could access my details, or I just want to repeat it at a different time. |
| ...have a clear and intuitive method of navigating through the app via the command line. | ...I can easily navigate and use the app. |

## Technologies Used

### Language Used

+ Python


### Frameworks, Libraries & Programs Used

1. Google Sheet: 
+ Google sheet was used to connect with the app in order to store data on a spreadsheet.

2. Google Cloud Platform
- to set up API's.

3. Google Sheets API

4. Google Drive API

5. GitHub
- Github was used to store the project after being pushed

6. VS Code Editor
- To write and run the code VS Code editor was used which is Code Institute's cloud based IDE platform.

### Data Model

The data model and the use of 'CRUD' operations are central to the functioning of this CLI app. The data is stored in a Google Sheet and is not lost between sessions. 

### Validation
- There are different types of validation depending on the user input type: 

![Data Validation](documentation/datavalidation1.png)

![Data Validation](documentation/datavalidation2.png)

1. Validation of negative values 
    - This checks whether the user has entered a positive value
2. Validation for string
    - This checks if the users' input is a string
3. Validation for blank
    - This checks if the user did put any value at all


#### To be implemented
- Determining a range of input both for weight and height values to avoid extreme results at the calculation

## Features

1. Main Menu
2. Weight input - with example
3. Height input - with example
4. BMI Result
5. BMI Category
6. Weight to lose/gain - if applies
7. Delete last entry
8. End program/ restart calculation

### Main Menu

![Main menu](documentation/programstart.png)

### Weight, height input - with example

![Weight input](documentation/userinputfields.png)

### BMI Result, category

![Bmi result](documentation/processeddata.png)

### Weight to lose/gain - if applies

![Weight loss](documentation/weighttolose.png)

### Delete last entry, end program

![Last entry](documentation/laststep.png)



## Testing

I took a test-as-you-go approach - testing after each change to ensure that my desired outcome was achieved. 

I also completed an end-to-end test covering these aspects, at milestones throughout the project:

- Test each user journey from start to finish
- Test going home from every input possible
- Test every input with invalid inputs, empty inputs and extreme values (where applicable)



| Feature | Action | Outcome |
|----------|----------|----------|
| Weight input    | Correct value    | Program moves to next step   |
| Weight input    | Negative value   | Error message displayed, program back to start   |
| Weight input    | Blank/ string   | Error message displayed, program back to start   |
| Height input    | Correct value   | Program moves to next step, calculation triggered   |
| Height input    | Negative value   | Error message displayed, program asks to re-enter data   |
| Height input    | Blank/ string   | Error message displayed, program asks to re-enter data   |
| Last entry     | Delete last entry - no   | Last entry and result will be saved in google sheets   |
| Last entry    | Delete last entry - yes  | Last entry and result will be deleted from google sheets    |
| Recalculate    | Calculate again - yes   | Program returns to the start point   |
| Recalculate   | Calculate again - no  | Program ends  |


### Important
- At this stage there still now high or low values set to avoid extreme, non realistic results.
- The calculation will go ahead even if someone would put in 500 kg's as body weight or 3.78 as height.
![Extreme values](documentation/extremevalues.png)

- For future improvement I'm looking for the pricipal that could be implemented to avoid extreme results.

## Code Validation
PEP8 validation using the Code Institute Python Linter was completed at milestones throughout the project and once right at the end. All errors given were resolved each time. 






