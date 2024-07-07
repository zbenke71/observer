from abc import ABC, abstractmethod
from .observable import Observable


class Observer(ABC):
    """
    An abstract base class for observers in the Observer pattern.
    
    Observers subscribe to events from an Observable object and define
    an update method to respond to events.

    https://bennet.hu
    """
    
    def __init__(self, observable: Observable, event, func=None):
        """
        Initialize the Observer by subscribing to an event from the Observable.
        
        :param observable: The Observable object to subscribe to.
        :param event: The event to subscribe to.
        :param func: The function to call when the event occurs. If None, the 'update' method is used.
        """
        observable.subscribe_to_event(event, func or self.update)

    @abstractmethod
    def update(self, event, *args, **kwargs):
        """
        Respond to an event.
        
        This method must be implemented by subclasses.
        
        :param event: The event that occurred.
        :param args: Additional positional arguments for the event.
        :param kwargs: Additional keyword arguments for the event.
        """
        pass
