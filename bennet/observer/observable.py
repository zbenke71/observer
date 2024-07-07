class Observable:
    """
    A class to manage event subscriptions and notifications.
    
    The Observable class allows objects to subscribe to and unsubscribe from
    events, and to notify all subscribers when an event occurs.

    https://bennet.hu
    """
    
    def __init__(self):
        """
        Initialize the Observable with an empty dictionary of event subscriptions.
        """
        self.event_subscriptions = {}

    def subscribe_to_event(self, event, func):
        """
        Subscribe a function to an event.
        
        :param event: The event to subscribe to.
        :param func: The function to call when the event occurs.
        """
        if event not in self.event_subscriptions:
            self.event_subscriptions[event] = []
        self.event_subscriptions[event].append(func)

    def unsubscribe_from_event(self, event, func):
        """
        Unsubscribe a function from an event.
        
        :param event: The event to unsubscribe from.
        :param func: The function to remove from the subscription list.
        """
        if event in self.event_subscriptions:
            self.event_subscriptions[event].remove(func)

    def trigger_event(self, event, *args, **kwargs):
        """
        Notify all subscribers of an event.
        
        :param event: The event that occurred.
        :param args: Additional positional arguments to pass to the subscriber functions.
        :param kwargs: Additional keyword arguments to pass to the subscriber functions.
        """
        if event in self.event_subscriptions:
            for func in self.event_subscriptions[event]:
                func(event, *args, **kwargs)

