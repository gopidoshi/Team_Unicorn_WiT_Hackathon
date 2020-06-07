# Catalyst

## Contents

1. [Short description](#short-description)
1. [Demo video](#demo-video)
1. [The architecture](#the-architecture)
1. [Long description](#long-description)
1. [Project roadmap](#project-roadmap)
1. [Getting started](#getting-started)
1. [Built with](built-with)

## Short description

### What's the problem?

Part of the World Health Organization's guidance on limiting further spread of COVID-19 is to practice social distancing norms. As a result, places like offices, schools, hospitals, banks and super markets etc. need to manually monitor if each person is practicing the social distancing norms like wearing a PPE face mask, maintaining a minimum distance of 6feet, and avoiding crowd. This is a labourious task.

### How can technology help?

Technology can help crowded public places like hospitals,banks and super markets etc. to offer a virtual queue scheduling portal. Here a buisiness/hospital can register in this portal and provide the operational timings.A customer/ hospital visitor can book a slot online and visit the place in the scheduled appointment.

Places like offices and schools have to manually monitor and make sure a person is always wearing a face mask.
Cutting edge technologies like ML/AI plays a vital role in automating this process of identifying the person who is not wearing a face mask and notifying him/her swiftly.

### The idea

Catalyst presents two ML/AI driven novel products backed by IBM services to accelerate new normal.

* FastPass: A digital queue scheduling service by slot booking that avoids crowding and maximizes store/business occupancy without putting people at risk of COVID-19.
* AI powered Mask Detection: Individuals not following health guidelines around the use of protective face masks
can be detected and identified using AI-enabled edge intelligence and analytics running on fixed video security cameras. 

## Demo video

[![Watch the video](https://i.imgur.com/vKb2F1B.png)](https://youtu.be/ddgFhE_B66Y)

## The architecture
  ![Alt text](/hackathon_archi_part2.png)


![Alt text](/hackathon_archi5.png)

## Long description

### USE CASE 1:

Apolo hospital being a super speciality hospital usually has a lot of patients visiting doctors. However in this COVID-19 crisis, to avoid queuing of waiting patients,it has registered for Fastpass from Catalyst for queue scheduling and has put up the link of slot booking on it's website. Also to ensure safety of patients as well as staff, Apolo has embeded their CCTV cameras with automatic mask detection by Catalyst.

Mekhala is feeling sick today and wants to visit Apolo. Using Apolo's fastpass link, Mekhala books a slot for herself and receives a pass with QR code in her google pay wallet without installing any app.
 
Now, Mekhala reaches the hospital at the time of her slot. At the very entry of the hospital, she is screened by a CCTV camera  which detects whether she has worn a PPE face mask or not. She is allowed inside the hospital premises only when the camera detects her wearing a mask. Once allowed, she now enters the premises and gets her fastpass scanned by the receptionist, who confirms her slot and lets her visits the doctor seamlessly.
 
Catalyst helped Apolo manage their queue of patients, while ensuring safety protocols for patients. Melakha saved her time from standing in queue and visited hospital in a timely manner. She later rates Apolo 5 stars for handling the COVID-19 conditions with utmost efficiency.

#### Scalability
The application of this use case can be extended to relevant places like supermarkets, retailers, banks, religious shrines, theatres, public places of attraction, post offices and other government offices where general public frequently visits.

#### Future Enhancements
- CCTV cameras enabled with intelligent mask detection to be integrated with a toll gate which automatically opens only when a   person is detected with mask.

#### Key Features
- Virtual Queue scheduling system
- Flexible slot booking facility
- QR code based pass in common mobile wallets for easy and faster verification
- Contactless fast Scanning of pass ensures hygine
- Incase of government audit of COVID-19, data available of people who visited on a particular day
- AI powered CCTV camera for mask prediction

#### Solution URL
The solution has been deployed on the IBM cloud :
https://managerial.eu-gb.cf.appdomain.cloud/

### USE CASE 2:
 
This is an office/workplace specific solution where we are sure that each employee has an ID associated to him/her.

Aapta Global Solutions wanted to ensure safety of their employees during this Covid crisis and registered for getting their  CCTV cameras of bay area, cafeteria, workstation and walkways embeded with intelligent mask detection system by Catalyst. This system detects a person’s face and predicts whether he/she is wearing a PPE face mask or not in real time.
 
Manyu,an employee of Aapta Global Solutions moves around the office without wearing a face mask, one of the cameras detect him, captures his face and compares it with the photographs in the Employee Database. This database consists of all relevant details of an employee including photograph, email address, contact information and manager. Once his face matches with one of the photos, his details are retrieved and he is notified via email/phone which prompts him to wear a face mask. Upon exceeding the maximum number of notifications to Manyu, his details are escalated to the security compliance team which would take further necessary actions.
 
This not only ensures that Manyu always wears a mask in the office premises but also maintains a safe environment to other employees from catching any infections or exposures to the virus, which is very crucial during the time of this pandemic.
 
Our intelligent face mask detection system hence assists a workplace in enforcing safety protocol for the safety of its staff, vigilantly.

#### Future Enhancements
- Increase accuracy for face recognition and face matching algorithms.

#### Key Features 
- AI powered CCTV camera
- Detects a person's face with greater accuracy
- Meticulously detects a person not wearing a facemask
- Retrives the details of a person not wearing a facemask 
- Sends notification to a person in mere few seconds

#### Solution URL
The solution has been deployed on the IBM cloud:
https://managerial.eu-gb.cf.appdomain.cloud/

#### Scalability
The application of this use case can be extended to relevant places like airports, schools, hospitals where business owner wants to ensure the safety protocols for their employees.

### What makes Catalyst different?
Catalyst offeres solution to help busineses to follow WHO guidelines of avoid crowding and wearing a mask. With the help of artifical intelligence and queue scheduling software it assists businesses let their customers and employees adjust to the new normal and reduces the risk of spreading the pandemic.

### Features which make solutions by Catalyst novel
- Contactless passes in mobile wallets for queue schedulling without any additional apps.
- Real time protective face mask detection.
- Identification of person from facial detection,tag him by his ID and sending notification on the go in cases of non-compliace, asking him to wear a mask and in repetitive cases, escalating notification to authorities.
- Technologies enabling businesses to allow a person inside the premises only if he/she has a pass and is wearing a face mask does not yet exist currently.
 
### Project roadmap
<img src="/future_roadmap_mask_detection.jpg"  width="400" height="700"><img src="/future_roadmap_fastpass.jpg"  width="400" height="700">


## Getting started for mask detection and face comparison

### Prerequisites

Python 3.6.8

### Installation and running the code
```
git clone https://github.com/gopidoshi/Team_Unicorn_WiT_Hackathon.git
```
```
cd mask_detection
```
```
pip install -r requirements.txt
```
```
python app.py
```
Launch http://0.0.0.0:5000 in your browser

For the application to recognise your face: Add your recent photograph in the *"actual_faces"* folder and update your relevant  information in *"employee_database.xlsx"* 

## Getting started for Fastpass Queue Scheduling system

### Prerequisites

Node.JS

### Installation and running the code
```
git clone https://github.com/gopidoshi/Team_Unicorn_WiT_Hackathon.git
```
```
cd fastpass_and_UI
```
```
npm install --registry=https://registry.npmjs.org
```
```
live-server --entry-file=./index.html --port=3000 --registry=https://registry.npmjs.org
```
Launch http://0.0.0.0:3000 in your browser


## IBM Services used
- IBM Cloud Foundry App
- IBM Toolchain
- IBM Continuous Delivery
- IBM GitRepos and Issue Tracking
- IBM Eclipse Orion Web IDE
