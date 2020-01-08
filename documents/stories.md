# Parking Lot Stories
> This file is the story plans to make the projcet


## Content
* [Project Building](#pb)
* [Classes Implementation](#ci)
* [Application Interface](#ai)


<br/><a name="pb"></a>
## Project Building Epic

### Story: Project Building
* time: 0.5h
* acceptance criteria:
  - should create on a git repository
  - should build virtual environment(not really needed this time since the project requires no external libraries)
  - should have project, documentation, test directory
  - should have common folder directory
  - should have parking_lot.py


<br/><a name = "ci"></a>
## Classes Implementation

### Story: car class
* time: 0.5h
* acceptance criteria:
  - should have constructor with parameters plate_id and colour
  - should have a helper method to check if the plate_number is valid
  - should have tests

### Story: parking lot class
* time: 3h
* acceptance criteria:
  - should have constructor with parameter slot amount
  - should have function to park cars
  - should have function to leave cars
  - should have function to show status
  - should have function to get registration numbers for cars with certain colour
  - should have function to get slot numbers for cars with certain colour
  - should have function to get slot number for cars with certain registration number
  - should have tests


<br/><a name = "ai"></a>
## Application Interface Epic

### Story: finish with main interface
* time: 1h
* acceptance criteria:
  - should have parking_lot.py for non-interactive program
  - should have parking script to call parking_lot.py with parameters
  - should file_inputs.txt

### Documentation
* time: 0.5h
* acceptance criteria:
  - finish README
