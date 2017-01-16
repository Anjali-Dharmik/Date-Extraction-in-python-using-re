# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 11:13:45 2017

@author: anjalidharmik
"""
import re
from datetime import datetime

#Date 'DD/M/YY', 'DD/MM/YYYY', 'D/MM/YYYY' extraction
match = re.search(r'\d{1,2}/\d{1,2}/\d{2,4}', "11/8/16")
print match.group()

#Date 'DD/MM' extraction
match = re.search(r'\d{1,2}/\d{1,2}', "11/21")
print match.group()


#Date 'DD MM YYYY' extraction
match = re.search(r'\d{1,2} \d{1,2} \d{2,4}', "1 8 2016")
print match.group()

#Date 'MON DD, YYYY' extraction
mon = '(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|(Nov|Dec)(?:ember)?)'
match_pattern = r' \d{1,2}, \d{2,4}' 
match = re.search(mon + match_pattern, "Nov 4, 2016")
print match.group()

#Date 'MON. DD. YYYY' extraction
match_pattern = r'. \d{1,2}. \d{2,4}' 
match = re.search(mon + match_pattern, "Nov. 18. 2016")
print match.group()

#Date 'MON. DD. YYYY' extraction
match_pattern = r' \d{1,2} \d{2,4}' 
match = re.search(mon + match_pattern, "Nov 18 2016")
print match.group()