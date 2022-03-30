#!/usr/bin/env python

'''These modules find out the next two scheduled trains and returns their 
information, ordered from soonest to latest'''

import requests

URL = 'https://api.tfl.gov.uk/'

def query_maker(origin):
  ''' Returns a query URL for the TFL ArrivalDepartures API, which only 
  works for the overground'''
  query = '/'.join([URL,
                  'StopPoint',
                  origin,
                  'ArrivalDepartures?lineIds=london-overground'
                  ])
        
  return query


def train_finder(origin, destination, all_data=False):
    '''Returns a list of train  that are running between the 
    origin an destination stations, sorted by which arrives soonest'''
    
    query = query_maker(origin)
    
    train_request = requests.get(query)
    
    trains = sorted(
                    [train for train in train_request.json()
                    if train['destinationNaptanId'] == destination
                    and train['minutesAndSecondsToDeparture']!=''],
                    key=lambda d: d['scheduledTimeOfDeparture']
                    )


    if all_data == True:
      return trains

    else:
      return [train['minutesAndSecondsToDeparture'] for train in trains]
      