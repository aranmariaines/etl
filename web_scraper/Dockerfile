FROM nickgryg/alpine-pandas
RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN apk update && apk add bash
RUN apk --no-cache add curl

COPY . /app
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /app
CMD ["python3", "electric_companies_data_scraper.py"]

