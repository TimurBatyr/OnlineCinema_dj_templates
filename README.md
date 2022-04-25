# Installation 
1. To install the project, please, download it or clone this repository 
  
  - git clone
  
  https://github.com/TimurBatyr/OnlineShop_API
  

2. Create virtual environment and activate virtual environment

  - python3 -m venv venv 
  
  - . ./venv/bin/activate

  - cd OnlineShop

3. Install moduls

  - pip install -r requirements.txt

4. Start project

  - python3 manage.py makemigrations
  
  - python3 manage.py migrate
  
  - python3 manage.py createsuperuser

  - python3 manage.py runserver
