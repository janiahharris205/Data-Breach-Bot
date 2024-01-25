# Author: JaNiah Harris
# Email: janiah.harris205@gmail.com
# Last updated: june 12, 2023
# Description: Educates the user on the dangers of Data Breaches, 
# and recommends solutions to protect their data.

breachYear = 2019

#Greets user
print("Hello! I'm Breach Bot.\n")
userName = input("What is your name?\n\n")
print("\nNice to meet you " + userName)

#Recounts year of breach
todaysYear = input("\nWhat year is it?\n\n")
timePassed = int(todaysYear) - breachYear
print("\nWow! That means it has been " + str(timePassed) + " years since the Facebook data breach!\n")

#Introduces breach
print("Would you like to learn about the 2019 Facebook Data Breach?")
giveInfo = input("\nType 'yes' or 'no'\n\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("\nWhat would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organizations response or, (c) I would like to hear your reflection.\n")
  topic = input()
  
  if topic.lower() == "a":
    print("\nIn 2019, 530 million facebook users had their names, phone numbers, gender, DOB, location, relationship, status, and employer through the abuse of the feature searching users by phone number.\n")
  
  elif topic.lower() == "b":
    print("\nTo help protect users who were affected in the data breach Facebook removed the feature that caused the breach and removed unprotected data, as well as recommending the affected users to make sure their passwords and information was secure.\n")
  
  elif topic.lower() == "c":
    break
  
  else:
    print("\nSorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue")

#Introduces my take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("\nType 'yes' or 'no'\n\n")

#Shares my take
while giveInfo.lower() == "yes":
  print("\nWhat would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to the CIA Triad, (b) my reaction, (c) my advice, or (d) none.\n")
  topic = input()
  
  if topic.lower() == "a":
    print("\nThis data breach connects to the CIA Triad of confidentiality due to the fact that 530 million Facebook users had their personal data leaked on some level.\n")
  
  elif topic.lower() == "b":
    print("\nI disagree with the organization’s response because they didn’t encourage users to change their passwords or be careful of the level of information they share within the platform, only removing the feature that caused the hack and personal data that may have been breached.\n")
  
  elif topic.lower() == "c":
    print("\nFor anyone who thinks they might have had their data leaked during this event, go to Haveibeenpwned and check your email and phone number. Whether your account was breached or not, you should make sure to remove any personal information from your account as well as making sure to create secure passwords for all your accounts.\n")

  elif topic.lower() == "d":
    break 

  else:
    print("\nSorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue")

#Chatbot ends conversation
print("\nThanks for chatting with me, and I hope you learned something new!")