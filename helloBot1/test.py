import slack_sdk as slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter
import math

def hello():
    print("yar har har with a bottle of rum")
    print("why is git not working")