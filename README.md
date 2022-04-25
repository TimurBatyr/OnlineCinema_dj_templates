# Installation 
- To install the project, please, download it or clone this repository 
  
  - git clone
  
  https://github.com/TimurBatyr/OnlineShop_API
  
- Open repository directory

- Create virtual environment and activate virtual environment

  - python3 -m venv venv 
  
  - . ./venv/bin/activate

  - cd OnlineShop

  - pip install -r requirements.txt

- Do migrations | migrate | create superuser manage.py

  - python3 manage.py makemigrations
  
  - python3 manage.py migrate
  
  - python3 manage.py createsuperuser

  - python3 manage.py runserver
