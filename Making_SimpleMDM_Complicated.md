# Keynote Presentation: Making SimpleMDM Complicated.key

## Slide 1

### Title: “Making SimpleMDM Complicated”

#### Body 



#### Presenter Notes: 



## Slide 2

### Title: “Making SimpleMDM Complicated”

#### Body 

Considerations in systematically managing your devices 
via a MDM vendor with a working API.


#### Presenter Notes: 



## Slide 3

### Title: “Making SimpleMDM Complicated”

#### Body 

Lucas J. Hall
@lucasjhall_@lucas

#### Presenter Notes: 



## Slide 4

### Title: SimpleMDM isn't just any MDM, but it can be any MDM. 


#### Body 

Extend these ideas generally 
🙈, MDM Specific first, SimpleMDM features Second
Context: AWS

#### Presenter Notes: 



## Slide 5

### Title: A few bad assumptions…


#### Body 

You're using mdm for... mdm
Your mdm vendor, or internal solution, has a robust basic any API 
You have an cloud environment with access to to perform basic logic via scripted actions or services
Be able to receive and process webhook (POST) payloads

#### Presenter Notes: 



## Slide 6

### Title: tl;dr


#### Body 

All the (MDMs | Enrollments)?
Overrides and Attribute Precedence
API Use and Abuse

#### Presenter Notes: 



## Slide 7

### Title: All the Enrollments?


#### Body 

Multiple auto assigning enrollments?
Inbound pipelines from ABM 👉🏻 MDM
Example: Systematic MDM Enrollment based on Platform

#### Presenter Notes: 



## Slide 8

### Title: macOS
iPadOS
iOS


#### Body 

multiple auto assigning enrollments 
inbound pipelines from ABM 👉🏻 MDM
Example: Systematic MDM Enrollment based on Platform

#### Presenter Notes: 

1:1 easy, mdms auto assignment is nice
Maybe throw some testing? Get crazy 

## Slide 9

### Title: All the Enrollments


#### Body 

multiple auto assigning enrollments 
inbound pipelines from ABM 👉🏻 MDM
Example: Systematic MDM Enrollment based on Platform

#### Presenter Notes: 

Per platform based MDM options, that’s where it stops. 
Which is fine if you only are using platforms for specific things- but lets look at some workflows 

## Slide 10

### Title: macOS
iPadOS
iOS


#### Body 

multiple auto assigning enrollments 
inbound pipelines from ABM 👉🏻 MDM
Example: Systematic MDM Enrollment based on Platform

#### Presenter Notes: 

So nice, but limiting, what each of these MDM’s looks like is dependent on your… MDM 

## Slide 11

### Title: macOS
iPadOS
iOS


#### Body 

multiple auto assigning enrollments 
inbound pipelines from ABM 👉🏻 MDM
Example: Systematic MDM Enrollment based on Platform

#### Presenter Notes: 

Enrollments within Simplemdm
But you can create as many of these as you wish…

## Slide 12

### Title: macOS
iPadOS
iOS


#### Body 

multiple auto assigning enrollments 
inbound pipelines from ABM 👉🏻 MDM
Example: Systematic MDM Enrollment based on Platform

#### Presenter Notes: 

Ends up looking more like this depending on your need, each of these MDM servers, or DEP enrollments in SimpleMDM can be configured with their own steps of initial settings and deployment properties, but would take a manual assignment 

## Slide 13

### Title: macOS
iPadOS
iOS


#### Body 

multiple auto assigning enrollments 
inbound pipelines from ABM 👉🏻 MDM
Example: Systematic MDM Enrollment based on Platform

#### Presenter Notes: 

Later

## Slide 14

### Title: macOS
iPadOS
iOS


#### Body 

multiple auto assigning enrollments 
inbound pipelines from ABM 👉🏻 MDM
Example: Systematic MDM Enrollment based on Platform

#### Presenter Notes: 

Later: Systematic Provisioning based on Device

## Slide 15

### Title: Overrides and Attribute Precedence

#### Body 

SimpleMDM Specific Examples 
What are custom attributes?
How is precedence determined?
Logically extend to any system that supports attributes, or attribute precedence 

#### Presenter Notes: 



## Slide 16

### Title: Attributes

#### Body 

SimpleMDM’s oob include:
name, model, phone number, serial number, UDID
Lock Screen Example:
Asset Name: {{device_name}}. Serial Number: {{serial_number}}.

#### Presenter Notes: 



## Slide 17

### Title: Custom Attributes

#### Body 

Key: value relationship
“screensaver_default”: “10”
Set within Configs > Attributes

#### Presenter Notes: 



## Slide 18

### Title: Custom Attribute Precedence

#### Body 

Key: value relationship
“screensaver_default”: “10”
Set within Configs > Attributes

#### Presenter Notes: 



## Slide 19

### Title: Custom Attribute Precedence

#### Body 

Key: value relationship
“screensaver_default”: “10”
Set within Configs > Attributes

#### Presenter Notes: 



## Slide 20

### Title: Custom Attribute Precedence

#### Body 

Key: value relationship
“screensaver_default”: “10”
Set within Configs > Attributes

#### Presenter Notes: 



## Slide 21

### Title: Custom Attribute Overrides and Precedence

#### Body 

Beneficial to Systematically Updating the Attribute’s for Enrollment, Group or Device
Not maintaining profiles per control, per device

#### Presenter Notes: 



## Slide 22

### Title: Custom Attribute Overrides and Precedence

#### Body 

Beneficial to Systematically Updating the Attribute’s for Enrollment, Group or Device
Not maintaining profiles per control, per device

#### Presenter Notes: 



## Slide 23

### Title: API Use and Abuse


#### Body 

What is Supported?
API Libraries?
Webhooks
Examples:
Log Ingestion
Systematic Group Assignment 
Systematic Attribute Assignment

#### Presenter Notes: 



## Slide 24

### Title: /usr/bin/profiles


#### Body 

What is Supported?
API Libraries?
Webhooks
Examples:
Log Ingestion
Systematic Group Assignment 
Systematic Attribute Assignment

#### Presenter Notes: 



## Slide 25

### Title: What is supported?


#### Body 



#### Presenter Notes: 



## Slide 26

### Title: What is an MDM?


#### Body 

Probably a questioned that should be asked when considering an MDM.

#### Presenter Notes: 

What is an MDM? 

## Slide 27

### Title: What is the MDM specification?


#### Body 

Probably a questioned that should be asked when considering an MDM.

#### Presenter Notes: 

What is an MDM? 

## Slide 28

### Title: I APNS therefore I am?


#### Body 

Probably a questioned that should be asked when considering an MDM.

#### Presenter Notes: 

I asked a lot of folks these questions, but they just responded with- 

## Slide 29

### Title: Not now.


#### Body 

Probably a questioned that should be asked when considering an MDM.

#### Presenter Notes: 



## Slide 30

### Title: What is supported?


#### Body 

Probably a questioned that should be asked when considering an MDM.
What can / can’t you do from API?
How do those things align with your need?

#### Presenter Notes: 



## Slide 31

### Title: What is supported?


#### Body 

Probably a questioned that should be asked when considering an MDM.
What can / can’t you do from API?
How do those things align with your need?

#### Presenter Notes: 

The apis the limit. Any thing in the api, by extension, can be systematically manipulated with enough effort.

## Slide 32

### Title: API Libraries


#### Body 

Language specific libraries or SDKs to interact with your MDM
SimpleMDMpy

#### Presenter Notes: 



## Slide 33

### Title: API Libraries


#### Body 

Simplify the lift
Handle API calls, pagination, etc

#### Presenter Notes: 



## Slide 34

### Title: Example: Log Ingestion


#### Body 

GET the logs
Optionally pick up where youleft of in a past sync
Process / ship the logs asneeded for you

#### Presenter Notes: 



## Slide 35

### Title: SimpleMDM Webhooks


#### Body 

Events that trigger web hooks:
device:
enrolled
unenrolled
changed_group
These JSON payloads are sent to your API as a POST to be parsed within your system

#### Presenter Notes: 



## Slide 36

### Title: SimpleMDM Webhooks


#### Body 

Device enrolled:

#### Presenter Notes: 



## Slide 37

### Title: SimpleMDM Webhooks


#### Body 

Device enrolled:

#### Presenter Notes: 



## Slide 38

### Title: SimpleMDM Webhooks


#### Body 

Device enrolled:

#### Presenter Notes: 



## Slide 39

### Title: SimpleMDM Webhooks


#### Body 

Device enrolled:

#### Presenter Notes: 



## Slide 40

### Title: SimpleMDM Webhooks


#### Body 

Device enrolled:

#### Presenter Notes: 



## Slide 41

### Title: SimpleMDM Webhooks


#### Body 

Device enrolled:

#### Presenter Notes: 



## Slide 42

### Title: SimpleMDM Webhooks


#### Body 

Events that trigger web hooks:
device:
enrolled
unenrolled
changed_group
test_event

#### Presenter Notes: 



## Slide 43

### Title: Example: Systematic Group Assignment


#### Body 

We know dis:
Device serial number
Device’s ID within the MDM
Group ID of Device’s assignment

#### Presenter Notes: 



## Slide 44

### Title: Example: Systematic Group Assignment


#### Body 

We know dis:
Device serial number
Device’s ID within the MDM
Device’s ID of Group assignment

#### Presenter Notes: 



## Slide 45

### Title: Example: Systematic Attribute Assignment


#### Body 

We know dis:
Device serial number
Device’s ID within the MDM
Device’s ID of Group assignment

#### Presenter Notes: 



## Slide 46

### Title: Taking A Step Back


#### Body 

We know dis:
Device serial number
Device’s ID within the MDM
Device’s ID of Group assignment

#### Presenter Notes: 



## Slide 47

### Title: Taking A Step Back


#### Body 

We know dis:
Device serial number
Device’s ID within the MDM
Device’s ID of Group assignment

#### Presenter Notes: 



## Slide 48

### Title: Taking A Step Back


#### Body 

We know dis:
Device serial number
Device’s ID within the MDM
Device’s ID of Group assignment

#### Presenter Notes: 

Events are in events you care about 
Evaluation is the business logic of the events 
Action is the change coming from the evaluation of the logic

## Slide 49

### Title: Taking A Step Back


#### Body 

We know dis:
Device serial number
Device’s ID within the MDM
Device’s ID of Group assignment

#### Presenter Notes: 

Events are in events you care about 
Evaluation is the business logic of the events 
Action is the change coming from the evaluation of the logic

## Slide 50

### Title: tl;dr


#### Body 

Use the API
Ponder, What is MDM?
Complexity in increments as needed is 👌🏻

#### Presenter Notes: 



## Slide 51

### Title: Resources


#### Body 

SimpleMDMpy
SimpleMDM API Documentation
SimpleMDM on Macadmins
 Device Management Documentation 

#### Presenter Notes: 



## Slide 52

### Title: Resources


#### Body 

SimpleMDMpy
SimpleMDM API Documentation
SimpleMDM on Macadmins
 Device Management Documentation 

#### Presenter Notes: 




