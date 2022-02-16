FROM python:3.8
ADD . /warehouse
WORKDIR /warehouse
RUN pip install flask gunicorn
EXPOSE 5001
CMD ["gunicorn", "-b", "0.0.0.0:5001", "warehouse:app"]