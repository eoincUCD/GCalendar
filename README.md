# GCalendar
Create a Sankey Diagram from Google Calendar: A quick project to refresh my coding skills

GCalendar.py - Converts .ics into csv data frame

Graph_db4.py - Converts csv data frame into Sankey formar for http://sankeymatic.com/


Steps to make Sankey diagram from Google Calendar:
1.	Export from Google: https://calendar.google.com/calendar/r/settings/export

2.	Python to parse data from .ics calendar file to csv:

  Sample text from .ics file:
  BEGIN:VEVENT
  DTSTART:20171203T153000Z
  DTEND:20171203T160000Z
  DTSTAMP:20180912T201829Z
  CREATED:20171203T124026Z
  DESCRIPTION:
  LAST-MODIFIED:20171203T160736Z
  LOCATION:
  SEQUENCE:1
  STATUS:CONFIRMED
  SUMMARY:Gym
  TRANSP:OPAQUE
  END:VEVENT

  a.	Extract event elements – name, start, end time, repeat variable
  b.	Translate string dates to datetime format and calculate duration
  c.	Save to Pandas data frame
  d.	Export to csv

3.	Manually tag events by category
  a.	3 Category levels used for simple visual
  b.	A clustering algorithm could be possible based on calendar, colours, naming etc

4.	Add estimated drive and sleep time

5.	Import CSV to Python data frame and manipulate for Sankey format:
  a.	Total [1000hrs] Category_level_1
  b.	Category_level _1 [200hrs] Category_level _2
  c.	Category_level _2 [150hrs] Category_level _3

6.	Output format as text file and upload to Sankey website
  a.	Python Sankey could be used for more customisation
