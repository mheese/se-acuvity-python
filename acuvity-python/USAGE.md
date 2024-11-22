<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from acuvity import Acuvity

s = Acuvity()

res = s.apex.list_analyzers()

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
from acuvity import Acuvity
import asyncio

async def main():
    s = Acuvity()
    res = await s.apex.list_analyzers_async()
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->