# Catalyst

## Contents

1. [Short description](#short-description)
1. [Demo video](#demo-video)
1. [The architecture](#the-architecture)
1. [Long description](#long-description)
1. [Project roadmap](#project-roadmap)
1. [Getting started](#getting-started)

## Short description

### What's the problem?

Part of the World Health Organization's guidance on limiting further spread of COVID-19 is to practice social distancing norms. As a result, places like offices, schools, hospitals, banks and super markets etc. need to manually monitor if each person is practicing the social distancing norms like wearing a PPE face mask, maintaining a minimum distance of 6feet, and avoiding crowd. This is a labourious task.

### How can technology help?

Technology can help crowded public places like hospitals,banks and super markets etc. to offer a virtual queue management portal, where a person can book a slot online and visit the place in the scheduled appointment.

Places like offices and schools have to manually monitor and make sure a person is always wearing a face mask.
Cutting edge technologies like ML/AI plays a vital role in automating this process of identifying the person who is not wearing a face mask and notifying him/her.

### The idea

We have designed a ML/AI driven novel solution backed by IBM Cloud foundry:
* A digital queuing system to avoid crowding in public places and allow only people who wear a face mask inside the premises.
* In workplace and schools, identify a person who is not wearing a face mask and notify him/her.
## Demo video

{}

## The architecture
![Alt text](/hackathon_archi5.png)
## Long description

### USE CASE 1: Digital-Kataar (Digi-Kataar)
 
Mekhala wants to visit a hospital to see her relative. She logs in to Digital-Kataar , a Web App , where she books a slot for herself and receives a confirmation in the form of a QR code.
 
Now, Mekhala reaches the hospital at the time of her slot. At the very entry of the hospital, she is screened by a CCTV camera which detects whether she has worn a PPE face mask or not. She is allowed inside the hospital premises only when the camera detects her wearing a mask. Once allowed, she now enters the premises and meets the receptionist, who confirms her slot and lets her visit her relative in the ward.
 
In this time of COVID crisis, when more people are not allowed to enter any premises at a particular time, Digi-Kataar helped Mekhala to avoid a long queue, visit her relative in a timely manner and ensure an effective use of time, with a mask.
 
This application can be extended/relevant places like supermarkets, various famous shops, boutiques, clothing emporiums, Post offices, and other Government offices where general public frequently visits.

#### Future Enhancements
- CCTV cameras enabled with intelligent mask detection to be integrated with a toll gate which automatically opens only when a   person is detected with mask.

#### Key Features
- Virtual Queuing system
- Flexible slot booking facility
- QR code based token for easy and faster verification
- AI powered CCTV camera 
- Accurate face recognition and face mask prediction 

### USE CASE 2: Animisha
 
This is an office/workplace specific solution where we are sure that each employee has an ID associated to him/her.
 
Manyu is an employee of Aapta Global Solutions. His office is equipped with multiple CCTV cameras at every other significant place like bay area, cafeteria, workstation and walkways. These CCTV footages are fed to an intelligent mask detection system which detects a person’s face and predicts whether he/she is wearing a PPE face mask or not.
 
Suppose Manyu moves around the office without wearing a face mask, one of the cameras detect him, captures his face and compares  it with the photographs in the Employee Database. This database consists of all relevant details of an employee including photograph, email address, contact information and manager. Once his face matches with one of the photos, all his details are retrieved and he is notified via email/phone which prompts him to wear a face mask. Upon exceeding the maximum number of notifications to Manyu, his details are escalated to the security compliance team which would take further necessary actions.
 
This not only ensures that Manyu always wears a mask in the office premises but also maintains a safe environment to other employees from catching any infections or exposures to the virus, which is very crucial during the time of this pandemic.
 
Our intelligent face mask detection system hence assists a workplace in enforcing strict social distancing norms (not sure if it’s a perfect word) along with ensuring the safety of its staff, vigilantly.

#### Future Enhancements
- More accuracy for face recognition and face matching algorithms.

#### Key Features 
- AI powered CCTV camera
- Detects a person's face with greater accuracy
- Meticulously detects a person not wearing a facemask
- Retrives the details of a person not wearing a facemask 
- Sends notification to a person in mere few seconds

### Why is Catalyst a novel solution?
The pandemic COVID19 has pushed humanity to adjust to the new normal, which requires assistance from technology.Catalyst offers a set a solutions to live with the pandemic easily and efficiently. Enforcing people to follow WHO guidelines with the help of Artifical intelligence, assists people adjust to the new normal and reduces the risk of spreading the pandemic.
 
### Future Roadmaps
<img src="/future_roadmap_part1.png"  width="400" height="700"><img src="/future_roadmap_part2.png"  width="400" height="700">

## Getting started for mask detection and face comparison

### Prerequisites

Python 3.6.8

### Installation and running the code

pip install -r requirements.txt

python app.py

Launch http://0.0.0.0:5000 in your browser

## Getting started for Queuing system

### Prerequisites

Node.JS

### Installation and running the code

npm install

npm run

## Built with
- IBM Cloud Foundry App
- IBM Toolchain
- IBM Continuous Delivery
- IBM GitRepos and Issue Tracking
- IBM Eclipse Orion Web IDE
