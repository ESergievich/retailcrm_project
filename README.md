<div align="center">

<h1>RetailCRM FastAPI Integration</h1>

<p>
This project is a FastAPI-based integration with RetailCRM, enabling easy access to common CRM functionality like creating and retrieving customers, orders, and payments.
</p>

</div>


### Features

The project offers the following API endpoints:

**Customers**
* POST /customers/create: Create a new customer.
* GET /customers/: Get a list of customers.

**Orders**
* POST /orders/orders/create: Create a new order.
* GET /orders/{customer_id}: Get orders by customer ID.

**Payments**
* POST /payments/payments/create: Create a new payment.

### Technology Stack

* FastAPI: Web framework for building APIs.
* Pydantic: Data validation and settings management.
* Uvicorn: ASGI server for running FastAPI applications.
* HTTPX: Asynchronous HTTP client for making requests.
* Pydantic-Settings: Managing application settings with Pydantic.

### Installation
**1. To install and run the project locally, follow these steps:**

- Register for RetailCRM Test System:
- Go to RetailCRM and generate an API key for integration:
  - Go to Settings → Integration → Add.
  - Generate a new API key for authenticating requests.

**2. Clone the project and navigate to the project directory:**

```shell
git clone https://github.com/ESergievich/retailcrm_project.git && cd retailcrm_project && cp .env.template .env
```
**Replace the following environment variables with your actual RetailCRM credentials in .env file:**

```dotenv
APP_CONFIG__RETAILCRM__CRM_URL=https://my_domain.retailcrm.ru
APP_CONFIG__RETAILCRM__API_KEY=my_api_key
```

Then run the application using Docker Compose:

```shell
docker-compose up - d
```

The project should now be running on http://localhost:8000.
