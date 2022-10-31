FROM python:3

RUN adduser --system --no-create-home nonroot

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown nonroot:users .
CMD [ "python", "./generate_csv.py" ]
