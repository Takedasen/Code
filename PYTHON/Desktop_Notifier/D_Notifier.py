
from plyer import notification

            #? Sets the title and message for the notification
title = 'Ronin Notifier'
message = 'Get things done, big boy'

            #? Uses the plyer library to display the notification
notification .notify(
    title = title,
    message = message,
    app_name = 'Ronin Notifier',
            #? Displays notification for * seconds
    timeout = 3 
)