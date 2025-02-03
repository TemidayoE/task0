# **HNG TASK0 API**

This is a simple Django RESTAPi that returns:
- Registered **Email Address**
- Current **datetime in ISO8601 format**
- the **Github repo URL** of the project's codebase

It supports **CORS** for cross-origin requests.
_____________________________________________________

## **SetUp Instructions**
### **1. Clone the repo**
```sh
git clone
https://github.com/TemidayoE/task0.git
cd basic_api
```

### **2. Create a venv & Install dependencies**
```sh
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```
### **3. Run Database migrations**
```sh
python manage.py migrate
```
### **4. Start the development server**
```sh
python manage.py runserver
```
_____________________________________________________
## **API Documentation**

### Endpoint
|Method|URL|Description|
|:----:|:-:|:---------:|
|GET | /api | Returns slack email, datetime and gitbug repo url |

### **Example JSON Response**
```json
{
  "slack_email": "example-email@email.com",
  "current_datetime": "2025-02-03T10:45:56.598299+00:00",
  "git_repo": "https://github.com/TemidayoE/task0"
}
```
______________________________________________________

## **CORS Support**

By default, this API allows requests from all origins. You can modify that in **setting.py**
______________________________________________________
## **Contributing**
Fork the repo, make improvements and submit a pull request.
_______________________________________________________
## **Hire Python Developers**
Looking for Django experts? [Hire Python Developers](https://hng.tech/hire/python-developer)
_______________________________________________________