# Observer Package

## Overview

The `observer` package provides a simple implementation of the Observer design pattern in Python, under the `bennet` namespace. This package consists of two modules: `observable.py` and `observer.py`. The `Observable` class manages event subscriptions and notifications, while the `Observer` class is an abstract base class for creating observer objects that respond to events.

## Installation

To use the `observer` package, ensure the directory structure matches the following:

```
observer/
├── bennet/
│   └── observer/
│       ├── __init__.py
│       ├── observable.py
│       └── observer.py
```

Then, you can import the package in your Python code.

## Usage

### Observable

The `Observable` class allows objects to subscribe to and unsubscribe from events, and to notify all subscribers when an event occurs.

#### Example

```python
from bennet.observer import Observable

class MyObservable(Observable):
    def __init__(self):
        super().__init__()

observable = MyObservable()

def event_handler(event, *args, **kwargs):
    print(f"Event: {event}, Args: {args}, Kwargs: {kwargs}")

observable.subscribe_to_event('my_event', event_handler)
observable.trigger_event('my_event', 42, key='value')  # Output: Event: my_event, Args: (42,), Kwargs: {'key': 'value'}
```

### Observer

The `Observer` class is an abstract base class for observers in the Observer pattern. Observers subscribe to events from an `Observable` object and define an `update` method to respond to events.

#### Example

```python
from bennet.observer import Observer, Observable


class MyObserver(Observer):
    def update(self, event, *args, **kwargs):
        print(f"Received event: {event}, Args: {args}, Kwargs: {kwargs}")

observable = Observable()
observer = MyObserver(observable, 'my_event')

observable.trigger_event('my_event', 42, key='value')  # Output: Received event: my_event, Args: (42,), Kwargs: {'key': 'value'}
```

## Modules

### `observable.py`

#### Classes

- **Observable**
  - `__init__(self)`: Initialize the `Observable` with an empty dictionary of event subscriptions.
  - `subscribe_to_event(self, event, func)`: Subscribe a function to an event.
  - `unsubscribe_from_event(self, event, func)`: Unsubscribe a function from an event.
  - `trigger_event(self, event, *args, **kwargs)`: Notify all subscribers of an event.

### `observer.py`

#### Classes

- **Observer**
  - `__init__(self, observable: Observable, event, func=None)`: Initialize the `Observer` by subscribing to an event from the `Observable`.
  - `update(self, event, *args, **kwargs)`: Respond to an event. This method must be implemented by subclasses.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to create an issue or submit a pull request.

## License

This project is licensed under the MIT License.
```

This `README.md` file provides a comprehensive overview of the package, installation instructions, usage examples, and descriptions of the classes and their methods. Adjust the content as needed to better fit your project's specific requirements.