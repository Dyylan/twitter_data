import pytz
import os
from twitter import Api
from datetime import datetime
from plots import time_plot_scatter_1d



api = Api(consumer_key = os.getenv('CONSUMER_KEY'),
          consumer_secret = os.getenv('CONSUMER_SECRET'),
          access_token_key = os.getenv('ACCESS_TOKEN_KEY'),
          access_token_secret = os.getenv('ACCESS_TOKEN_SECRET'))


def status_times(screen_name):
    statuses = api.GetUserTimeline(screen_name=screen_name, trim_user=True)
    status_times = []
    for status in statuses:
        status_datetime = datetime.strptime(status.created_at, '%a %b %d %H:%M:%S %z %Y') 
        status_times.append(status_datetime)
    return status_times


def filter_times(start_time, end_time=datetime.now(pytz.utc)):
    filtered_times = [status_time for status_time in status_times if status_time > start_time and status_time < end_time]
    return filtered_times


status_times = status_times(screen_name='aoc')


# Filter for approximately last day
start_time = 'Sun Nov 27 22:47:32 +0000 2019'
start_time = datetime.strptime(start_time, '%a %b %d %H:%M:%S %z %Y') 
filtered_times = filter_times(start_time)


# Plot using a function from the plots module
time_plot_scatter_1d(filtered_times)