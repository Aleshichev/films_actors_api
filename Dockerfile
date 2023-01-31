FROM python:3.10

RUN useradd --create-home userapi
WORKDIR /example_pip

RUN pip install -U pipenv
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy --system
COPY ./ .
RUN chown -R userapi:userapi ./
USER userapi

EXPOSE 5000
CMD ["python", "./wsgi.py"]
