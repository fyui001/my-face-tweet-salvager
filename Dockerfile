FROM python:3.10

WORKDIR /code

RUN pip install --upgrade pip && pip install pipenv

CMD ["/bin/bash"]