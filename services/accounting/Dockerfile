FROM python:3.8
ADD . /accounting
WORKDIR /accounting
RUN pip install flask gunicorn
EXPOSE 5002
CMD ["gunicorn", "-b", "0.0.0.0:5001", "accounting:app"]