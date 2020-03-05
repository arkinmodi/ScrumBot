## @file settings.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief 
#  @date Mar 5, 2020

import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')