# This file should be included in .gitignore to not store sensitive data in version control
import os
SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

database_setup = {
   "database_name" : "casting",
   "user_name" : "postgres", # Default postgres user name
   "password" : "postgres", # If applicable. If no password, just type in None
   "port" : "localhost:5432" # Default postgres port
}

auth0_config = {
    "AUTH0_DOMAIN" : "fsnds.eu.auth0.com", # The auth0 domain prefix
    "ALGORITHMS" : ["RS256"],
    "API_AUDIENCE" : "Casting", # The audience set for the auth0 app
    "clientId": 'reIq7tebc917ZSQZTmiKcHTbY4I8OTMf', # The client id generated for the auth0 app,
    "callbackURL": 'http://localhost:8100',  # The base url of the running ionic application.
}

pagination = {
    "example" : 10 # Limits returned rows of API
}

bearer_tokens = {
    "casting_assistant" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJERTFSVGM0TVRrek9VWTJOalJGTVRoR016RTRRamRGUWpKRFJUaEJRa0l3UVRZeU1qTkNOQSJ9.eyJpc3MiOiJodHRwczovL2ZzbmRzLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZTgwYzgzMjVkZTFhMzBjNWVjZjNkOTciLCJhdWQiOiJDYXN0aW5nIiwiaWF0IjoxNTg5Mjg0ODU3LCJleHAiOjE1ODkzNzEyNTcsImF6cCI6InJlSXE3dGViYzkxN1pTUVpUbWlLY0hUYlk0SThPVE1mIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJHRVQ6YWN0b3JzIiwiR0VUOm1vdmllcyJdfQ.JurEXIOnpXadiSJqePV3LBHTH5IFStl2NWaIdVu05GiQVcSoYmuuChJJd4tK4LLOHLkCqXpYQxVuc5NWM3xP9OkQzDAdOI9jTBzYpOayPr5UmE2_8dLwKoZK6VD3fOOCzRVV8fUF3rZBHbScySnKVvyrxxSOihFyjBrf8Yhfoqgv8XEZY-zdJkBU4uCncVuPDf7Cm3OoVclz-uDX3rz-KVtiDiNnzcGL8J4ILqvnGrQ6Zbq1KQoISxxF6k2JuPcmCITfgxtwwtiRTRGk5856iC8pZjchOa5U4WUZQqVb-JMUSNlOv4jacFXU1vSI-nmjc_yGce46mpHZT5y0ol18VQ",
    "executive_producer" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJERTFSVGM0TVRrek9VWTJOalJGTVRoR016RTRRamRGUWpKRFJUaEJRa0l3UVRZeU1qTkNOQSJ9.eyJpc3MiOiJodHRwczovL2ZzbmRzLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWFlZDVlMGVhZjg1MTBiZTdlYTQ2M2UiLCJhdWQiOiJDYXN0aW5nIiwiaWF0IjoxNTg5Mjg0NzkwLCJleHAiOjE1ODkzNzExOTAsImF6cCI6InJlSXE3dGViYzkxN1pTUVpUbWlLY0hUYlk0SThPVE1mIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJERUxFVEU6YWN0b3JzIiwiREVMRVRFOm1vdmllcyIsIkdFVDphY3RvcnMiLCJHRVQ6bW92aWVzIiwiUEFUQ0g6YWN0b3JzIiwiUEFUQ0g6bW92aWVzIiwiUE9TVDphY3RvcnMiLCJQT1NUOm1vdmllcyJdfQ.I00rsDguVUE1EBI1j0W6jj89N79cDgX_KP5shMDANdQgFVmd5Ll7rf5JS9Xx_tT1a1NYTFq-_9x04GGCBfEZEgXVLqiByrEGCTj7jj72giD0a1MK-eVMLoGfRjJTmoMzVvph_RwlE8M8cALD4W3Phv5jR5bfc-4tyc8vUoFr0aiwRABW4WC4KRZcCIhX0xB-5-XCVDlAxk83DkmlKxr61yuPXVVc66ZHCjHL45WkkXquB3tKx1Ts0aLs2YT717K9fibLntJu7bU9Cq_nr32iSZaIhpnSF5ZTi-Ya4i-Yg1ksl5D5KTlYxeCL2ueaWFLjAr7M2syVjhx5T451dmkd9g",
    "casting_director" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJERTFSVGM0TVRrek9VWTJOalJGTVRoR016RTRRamRGUWpKRFJUaEJRa0l3UVRZeU1qTkNOQSJ9.eyJpc3MiOiJodHRwczovL2ZzbmRzLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZTkwYTM5ZGY3NTk2MjBjMDhjN2JkYWYiLCJhdWQiOiJDYXN0aW5nIiwiaWF0IjoxNTg5Mjg0NzA0LCJleHAiOjE1ODkzNzExMDQsImF6cCI6InJlSXE3dGViYzkxN1pTUVpUbWlLY0hUYlk0SThPVE1mIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJERUxFVEU6YWN0b3JzIiwiR0VUOmFjdG9ycyIsIkdFVDptb3ZpZXMiLCJQQVRDSDphY3RvcnMiLCJQQVRDSDptb3ZpZXMiLCJQT1NUOmFjdG9ycyJdfQ.td9MZVy1vruzVkHYmbTM7pImsyKHTKgbsu3Km5DpEebriFZmTkWizwDytMyThFaNh1qeZzGcQH6bvPnP3R_H7t24mpvtsfvBue7Vbv1_w44vn4VuqdN4siCwuqcq9YWajb5DN0gHTJEaEqOdo3mMqJe2yORr9mugJWNY3Rt95Hg8kox9kBhE6zRcVhzAsDjXQW7P78hK8SfP0XBT1Q-POHJTyPsF8vDFupoQ11KVk18fV8sgGGQZPB3vHJqGkEv1qtwqAiwHgU6ca3hmUVQ7xYqO3njc1A3Pe2k5Eo6LHGyP_6kRdvAPq8fx86yi2UEIZiyN-RE4pAF-li5lVSSzwA"
}