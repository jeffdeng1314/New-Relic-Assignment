FROM python:3.7

WORKDIR /New-Relic-Assignment

COPY . /New-Relic-Assignment/

CMD [ "python", "./solution.py", "/text files/full_moby_dick.txt" ]

