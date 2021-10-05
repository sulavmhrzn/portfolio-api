# Portfolio RestAPI
RestAPI for your portfolio project. 

## Setup locally
1. Clone the repo
    ```bash
    git clone https://github.com/sulavmhrzn/portfolio-api.git
    ```
2. Install requirements
    ```bash
    pip install -r requirements.txt
    ```
3. Setting environment variables :
    > Rename .env.sample to .env and fill up the required values.
4. Run development server
    ```bash
    python manage.py runserver
    ```

## Media files
Media files are served by [cloudinary](https://cloudinary.com/) therefore you are required to signup for an account.


## Schema
```json
GET http://localhost:8000
{
  "name": "Sulav Maharjan",
  "label": "CEO @ something",
  "image": "https://res.cloudinary.com/dlelhsxgc/image/upload/v1/media/profile/img-01_vedepf",
  "email": "sulav291@gmail.com",
  "phone": "9840033004",
  "summary": "I am sulav",
  "blog": "",
  "education": [
    {
      "institution": "South Western State College",
      "area": "Computer Science",
      "description": "Learn computer science",
      "study_type": "Bachelors In Computer Applications",
      "score": "3.24",
      "start_date": "2021-10-02",
      "end_date": null
    }
  ],
  "skill": [
    {
      "name": "Python",
      "level": "Beginner",
      "years_of_exp": 2
    },
    {
      "name": "Javascript",
      "level": "Beginner",
      "years_of_exp": 1
    }
  ],
  "project": [
    {
      "name": "Portfolio web",
      "description": "asd",
      "languages": "django, drf",
      "summary": "asd",
      "repo_url": "",
      "live_url": "",
      "start_date": "2021-10-02",
      "end_date": "2021-10-02"
    }
  ],
  "work": [
    {
      "name": "LeapFrog",
      "position": "Senior Devs",
      "start_date": "2021-10-02",
      "end_date": "2021-10-02",
      "summary": "asd"
    }
  ],
  "certificate": [
    {
      "name": "Python Cert"
    }
  ],
  "profile": [
    {
      "network": "github",
      "username": "sulavmhrzn",
      "url": "http://gihub.com/sulavmhrzn"
    },
    {
      "network": "Linkedin",
      "username": "sulavmhrzn",
      "url": "http://linkedin.com/sulavmhrzn"
    }
  ]
}
```