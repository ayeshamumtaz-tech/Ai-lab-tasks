# Lab 2 -- Intelligent Agents

## Introduction

This lab is about intelligent agents and how they make decisions based
on the information they receive from their environment.

The main case study is a smart classroom energy agent which controls
cooling based on room temperature and occupancy. The aim is to maintain
comfort while saving energy when the room is empty.

## Tasks

### Task 1 -- PEAS Specifications

Created PEAS specifications for two intelligent agents: - Delivery
Robot - LLM-Based Student Support Agent

Each specification includes Performance Measure, Environment, Actuators
and Sensors, along with a performance trade-off.

### Task 2 -- Environment Classification

Both agents were classified based on: - Observability (Fully Observable
/ Partially Observable) - Determinism (Deterministic / Stochastic)

Examples of observable variables, hidden variables and uncertain
outcomes were also discussed. Real environments were compared with
simplified simulators.

### Task 3 -- Stateful Classroom Agent

A Python program was developed to control the classroom operating mode
based on temperature and occupancy.

The program: - Checks whether the room is occupied. - Selects ECO, COOL,
WARM or IDLE mode. - Remembers the previous target mode. - Avoids
sending the same command repeatedly. - Tests repeated inputs,
temperature boundaries, mode transitions and empty-room conditions.

## Files

  File                 Description
  -------------------- ----------------------------------------------
  `lab2_model.py`      Python code for the stateful classroom agent
  `README.md`          Project description and running instructions
  `Lab2_Report.docx`   Complete lab report covering all three tasks

## Requirements

-   Python 3.x
-   No external libraries required.

## How to Run

1.  Download or clone the repository.
2.  Open the project folder in VS Code or any Python editor.
3.  Run the following command in the terminal:

``` bash
python lab2_model.py
```

The program will display the previous mode, current percept, target mode
and whether a command should be sent.

## Assumptions and Limitations

-   Temperature is measured in degrees Celsius.
-   Occupancy is represented using Boolean values (`True` or `False`).
-   An empty room always gets ECO mode.
-   The temperature thresholds are below 20°C for WARM and above 26°C
    for COOL.
-   At exactly 20°C and 26°C, the agent selects IDLE.
-   The program only simulates operating modes. It does not control
    actual AC hardware.
-   The agent remembers its previous mode but does not learn from data.
-   It does not implement hysteresis, so temperature changes around a
    threshold may cause mode switching.

## Conclusion

This lab helped in understanding intelligent agents, PEAS
specifications, environment classification and stateful decision-making.
The classroom agent also shows how remembering previous actions can help
avoid unnecessary repeated commands.
