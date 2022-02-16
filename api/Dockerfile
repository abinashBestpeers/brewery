FROM python:3.8
ADD . /api
WORKDIR /api
RUN pip install flask gunicorn requests
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]