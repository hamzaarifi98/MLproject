# main.py
import sys
from exception import CustomException

def trigger_error():
    try:
        a = 1 / 0
    except Exception as e:
        raise CustomException("A division error occurred", sys)

trigger_error()
