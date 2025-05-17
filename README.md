# Asyncio Signal Bus Examples

This package contains examples for the use of [asyncio-signal-bus](https://github.com/OpenBuildRight/asyncio-signal-bus).

## Installation

Install with [python poetry](https://python-poetry.org/).

```shell
poetry install
```

## Running Examples
This package contains several examples. The intent of these examples is to provide 
code that you can inspect in order to understand how to use asyncio-signal-bus.

### Basic Example
Run the basic example as follows.

```shell
poetry run python -m asyncio_signal_bus_example.basic_example.example
```

### Order Example
The order example is a FastAPI HTTP application launched by uvicorn.

Start the order example as follows.
```shell
# Export Variables
export TELEMETRY_HOST=http://foo.localhost 
export TELEMETRY_PASSWORD=abc123 

# Start the API
poetry run uvicorn \
--log-config=log_config.yaml  \
asyncio_signal_bus_example.order_example.app:APP
```

Then you can visit the API Swagger docs at 
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

You can call the API with cURL.
```shell
curl -X 'POST' \
  'http://127.0.0.1:8000/order' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "customer_id": "string",
  "customer_name": "string",
  "items": [
    "string"
  ]
}'
```